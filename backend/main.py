from flask import Flask, jsonify, request, redirect, session
from datetime import datetime
from flask_jwt_extended import create_access_token, JWTManager
from flask_cors import CORS
from flask_security import login_required, current_user, verify_and_update_password
from config import LocalDevelopmentConfig
from models import db, User, Role, Campaign, CampaignInfluencers, Sponsor, UserRoles, Influencer, AdRequest
from flask_security import Security, SQLAlchemyUserDatastore, hash_password

def createApp():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)

    CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, 
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"])
    db.init_app(app)

    datastore = SQLAlchemyUserDatastore(db, User, Role)
    # app.security = Security(app, datastore=datastore, )
    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.app_context().push()

    from route import auth
    app.register_blueprint(auth)
    from admin import admin_bp
    app.register_blueprint(admin_bp)

    return app



app = createApp()
import create_initial_data




    
if __name__=="__main__":
    app.run(debug=True,
        port=5000
    )