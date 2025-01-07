from flask import current_app as app
from models import db, Influencer
from flask_security import SQLAlchemyUserDatastore, hash_password

with app.app_context():
    db.create_all()

    userdatastore: SQLAlchemyUserDatastore = app.security.datastore

    userdatastore.find_or_create_role(name = "admin", description = "super user")
    userdatastore.find_or_create_role(name = "influencer", description = "campaigners, general users")
    userdatastore.find_or_create_role(name = "sponsor", description = "campaign creator and organisers")

    if (not userdatastore.find_user(email="admin@study.iitm.ac.in")):
        user = userdatastore.create_user(email = "admin@study.iitm.ac.in", password = hash_password("adminpass"), roles = ['admin'])
        db.session.commit()
    if (not userdatastore.find_user(email="inf01@study.iitm.ac.in")):
        user = userdatastore.create_user(email = "inf01@study.iitm.ac.in", password = hash_password("infpass"), roles = ['influencer'])
        db.session.commit()

        influencer = Influencer(
            id=user.id,
            full_name="inf01",
            email="inf01@study.iitm.ac.in",
        )
        db.session.add(influencer)
        db.session.commit()
    
