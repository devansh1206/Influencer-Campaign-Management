from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # name = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    # flask-security specific
    fs_uniquifier = db.Column(db.String, unique = True, nullable = False)
    active = db.Column(db.Boolean, default = False)
    flagged = db.Column(db.Boolean, default = False)
    roles = db.Relationship('Role', backref=db.backref('users', lazy='dynamic'), secondary='user_roles')


    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_active': self.active,
        }
    
    # influencer = db.relationship('Influencer', uselist=False, backref='user', lazy=True)
    # sponsor = db.relationship('Sponsor', uselist=False, backref='user', lazy=True)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable  = False)
    description = db.Column(db.String(100), nullable = False)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))

class Influencer(db.Model):
    __tablename__ = "influencer"
    id = db.Column(db.Integer, primary_key=True) # removed
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    category = db.Column(db.String(50))
    niche = db.Column(db.String(200))
    profile_picture = db.Column(db.String(100), default='default.jpg')
    twitter_handle = db.Column(db.String(50))
    twitter_followers = db.Column(db.Integer)
    instagram_handle = db.Column(db.String(50))
    instagram_followers = db.Column(db.Integer)
    facebook_handle = db.Column(db.String(50))
    facebook_followers = db.Column(db.Integer)

    def _repr_(self):
        return f'<Influencer {self.full_name}>'
    
    
class Sponsor(db.Model):
    __tablename__ = "sponsor"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    industry = db.Column(db.String(50))
    profile_picture = db.Column(db.String(100), default='default.jpg')
    website = db.Column(db.String(50))
    budget = db.Column(db.Integer)

    def _repr_(self):
        return f'<Sponsor {self.full_name}>'
    
    
    
class Campaign(db.Model):
    __tablename__ = "campaign"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.String(10), nullable=False)  # 'public' or 'private'
    goals = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    flagged = db.Column(db.Boolean, default=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=False)
    sponsor = db.relationship('Sponsor', backref=db.backref('campaigns', lazy=True))
    ad_requests = db.relationship('AdRequest', backref='campaign', lazy=True)

    def _repr_(self):
        return f'<Campaign {self.name}>'

    def campaign_progress(self):
        total_ad_requests = len(self.ad_requests)
        if total_ad_requests == 0:
            return 0.0
        completed_ad_requests = len([ad_request for ad_request in self.ad_requests if ad_request.completion_status == 'Complete'])
        return completed_ad_requests / total_ad_requests
    
    def to_dict(self):
        # return {
        #     "id": self.id,
        #     "name": self.name,
        #     "description": self.description,
        #     "start_date": self.start_date,
        #     "end_date": self.end_date,
        #     "budget" : self.budget,
        #     "visibility": self.visibility,
        #     "goals": self.goals,
        #     "active": self.active,
        #     "flagged": self.flagged,
        #     "sponsor_id" : self.sponsor_id,
        #     # Add more fields as necessary
        # }
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "budget": self.budget,
            "visibility": self.visibility,
            "goals": self.goals,
            "flagged": self.flagged,
            "sponsor_id": self.sponsor_id,
            # Add other serializable fields if necessary
        }

class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.Column(db.Text)
    requirements = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='Pending')  # 'Pending', 'Accepted', 'Rejected'
    offer_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    completion_status = db.Column(db.String(20), nullable=False, default='Incomplete')
    
    def _repr_(self):
        return f"AdRequest('{self.campaign_id}', '{self.influencer_id}', '{self.status}')"
    
    def to_dict(self):
        return {
            "id": self.id,
            "campaign_id": self.campaign_id,
            "influecer_id": self.influencer_id,
            "messages": self.messages,
            "requirements": self.requirements,
            "status" : self.status,
            "offer_amount": self.offer_amount,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "completion_status" : self.completion_status,
            # Add more fields as necessary
        }
    
# Association tables for many-to-many relationships
class CampaignInfluencers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'))

# campaign_sponsors = db.Table('campaign_sponsors',
#     db.Column('campaign_id', db.Integer, db.ForeignKey('campaign.id')),
#     db.Column('sponsor_id', db.Integer, db.ForeignKey('sponsor.id'))
# )



# User and Role Relationship
# UserRoles: This is an association table that links users and roles. It has foreign keys to both the User and Role tables.
# User: The User model has a many-to-many relationship with the Role model through the UserRoles table. This is defined using the roles attribute in the User model.
# User and Influencer/Sponsor Relationship
# User: The User model has one-to-one relationships with both the Influencer and Sponsor models. This is defined using the influencer and sponsor attributes in the User model.
# Influencer: The Influencer model has a foreign key user_id that references the User model. This establishes a one-to-one relationship.
# Sponsor: Similarly, the Sponsor model has a foreign key user_id that references the User model, establishing a one-to-one relationship.
# Campaign and Sponsor Relationship
# Campaign: The Campaign model has a foreign key sponsor_id that references the Sponsor model. This establishes a many-to-one relationship, where a sponsor can have multiple campaigns.
# Campaign and AdRequest Relationship
# Campaign: The Campaign model has a one-to-many relationship with the AdRequest model. This is defined using the ad_requests attribute in the Campaign model.
# AdRequest: The AdRequest model has a foreign key campaign_id that references the Campaign model, establishing a many-to-one relationship.
# AdRequest and User Relationship
# AdRequest: The AdRequest model has a foreign key influencer_id that references the User model. This establishes a many-to-one relationship, where a user (influencer) can have multiple ad requests.
# Summary of Relationships
# User <-> Role: Many-to-Many (via UserRoles)
# User <-> Influencer: One-to-One
# User <-> Sponsor: One-to-One
# Sponsor <-> Campaign: One-to-Many
# Campaign <-> AdRequest: One-to-Many
# User (Influencer) <-> AdRequest: Many-to-One
# These relationships are formed using SQLAlchemy's db.relationship and db.ForeignKey constructs, which help in defining how the tables are linked together in the database.