from flask import Flask, jsonify, request, redirect, session
from datetime import datetime
from models import db, User, Role, Campaign, CampaignInfluencers, Sponsor, UserRoles, Influencer, AdRequest
from flask import Blueprint, render_template, current_app as app
from flask_security import verify_password, hash_password, auth_required, current_user
from functools import wraps



datastore = app.security.datastore

# from maven.api.auth import auth
# app.register_blueprint()
auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET'])
def greeting():
    return "hello world"

@auth.route('/shark', methods=['GET'])
def shark():
    return ("Shark ! my friend")


@auth.get('/protected')
@auth_required('token')
def protected():
    return "<h1> only accessible by authenticated user </h1>"

# app.security.login_manager.login_view = 'auth.login'  # Map to your login blueprint
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"success": False, "message": "Email and password are required"}), 404

    user = datastore.find_user(email=email)
    
    if user and verify_password(password, user.password):
        # Set up user session
        role = user.roles[0].name
        session['user_id'] = user.id
        session['user_roles'] = role
        
        # Generate token using Flask-Security
        token = user.get_auth_token()

        user_data = {}
        if(role=='influencer'):
            print(db.session.query(Influencer).all())  # To check if the query works outside the function

            influencer = Influencer.query.filter_by(id=user.id).first()
            inf_campaigns = CampaignInfluencers.query.filter_by(influencer_id=influencer.id).all()
            inf_campaigns = [Campaign.query.filter_by(id=inf_campaign.campaign_id).first() for inf_campaign in inf_campaigns]
            active_campaigns = [inf_campaign for inf_campaign in inf_campaigns if(inf_campaign.end_date >= datetime.now().date())]
            past_campaigns = [inf_campaign for inf_campaign in inf_campaigns if(inf_campaign.end_date < datetime.now().date())]
            new_requests = AdRequest.query.filter_by(influencer_id=user.id).all()
            user_data = {
                "role": 2,
                "influencer": {
                    "id" : influencer.id,
                    "full_name": influencer.full_name,
                    "email": influencer.email,
                    "phone": influencer.phone,
                    "address": influencer.address,
                    "category": influencer.category,
                    "niche": influencer.niche,
                    "profile_picture": influencer.profile_picture,
                    "twitter_handle": influencer.twitter_handle,
                    "twitter_followers": influencer.twitter_followers,
                    "instagram_handle": influencer.instagram_handle,
                    "instagram_followers": influencer.instagram_followers,
                    "facebook_handle": influencer.facebook_handle,
                    "facebook_followers": influencer.facebook_followers
                },   
                "inf_campaigns": [campaign.to_dict() for campaign in inf_campaigns if campaign],  # Assuming the Campaign model has a to_dict() method
                "active_campaigns": [campaign.to_dict() for campaign in active_campaigns],
                "past_campaigns": [campaign.to_dict() for campaign in past_campaigns],
                "new_requests": [request.to_dict() for request in new_requests],
            }

        elif(role=='sponsor'):
            sponsor = Sponsor.query.filter_by(id=user.id).first()
            sps_campaigns = Campaign.query.filter_by(sponsor_id=user.id).all()
            user_data = {
                "role": 3,
                "sponsor" : {
                    "id" : sponsor.id,
                    "full_name" : sponsor.full_name,
                    "email" : sponsor.email,
                    "phone" : sponsor.phone,
                    "address": sponsor.address,
                    "industry": sponsor.industry,
                    "profile_picture": sponsor.profile_picture,
                    "website": sponsor.website,
                    "budget": sponsor.budget
                },
                "sponsor_campaign" : [campaign.to_dict() for campaign in sps_campaigns if campaign]
            }
        else:
            user_data = {
                "role" : 1,
                "email": email
            }

        return jsonify({"token": token, "user_data" : user_data, "message": "Login Successful!"})
    
    return jsonify({'error': 'Invalid credentials'}), 401


#         # gather all the data needed to render user dashboard
#         role = UserRoles.query.filter_by(user_id=user.id).first()
#         if(role.role_id==1): #admin

#             user_data = {
#                 "role": 1,
#                 # "admin" : Admin.query.filter_by(id=user.id).first(),
#                 # "sponsor_campaign" : Campaign.query.filter_by(sponsor_id=user.id).all()
#             }
#         elif(role.role_id==2): #influencer
#             influencer = Influencer.query.filter_by(id=user.id).first()
#             inf_campaigns = campaign_influencers.query.filter_by(influencer_id=influencer.id).all()
#             user_data = {
#                 "role":2,
#                 "influencer" : influencer,
#                 "inf_campaigns" : [Campaign.query.filter_by(id=inf_campaign.campaign_id).first() for inf_campaign in inf_campaigns],
#                 "active_campaigns" : [inf_campaign for inf_campaign in inf_campaigns if(inf_campaign.end_date >= datetime.now().date())],
#                 "past_campaigns" : [inf_campaign for inf_campaign in inf_campaigns if(inf_campaign.end_date < datetime.now().date())],
#                 "new_requests" : AdRequest.query.filter_by(influencer_id=user.id).all(),
#             }

#         else: #sponsor
#             user_data = {
#                 "role": 3,
#                 "sponsor" : Sponsor.query.filter_by(id=user.id).first(),
#                 "sponsor_campaign" : Campaign.query.filter_by(sponsor_id=user.id).all()
#             }


#         # Return the token and a success message
#         return jsonify({"success": True, "message": "Login successful", "access_token": access_token, "user_data":user_data}), 200

#     except Exception as e:
#         return jsonify({"success": False , 'message':e})


#influencer registration
@auth.route('/influencerRegister', methods=['POST'])
def register_influencer():
    data = request.get_json()
    # print(data)
    #check for existig user
    email = data.get("email")
    password = data.get("password")

    existing_user = datastore.find_user(email=email)
    if(existing_user):
        return jsonify({"success":False, "message":"Email already registerd"}), 404
    
    # Create user first
    user = datastore.create_user(
        email=email,
        password=hash_password(password),
        roles=['influencer'],
        active=False
    )
    db.session.commit()
    # print(f"Created user with ID: {user.id}")
    # # Convert niche list to comma-separated string
    # niche_string = ','.join(data.get('niche', []))
    
    # Create influencer profile
    try :
        influencer = Influencer(
            id=user.id,
            full_name=data.get("full_name"),
            email=email,
            phone=data.get('phone'),
            address=data.get('address'),
            category=data.get('category'),
            niche=data.get('niche'),
            profile_picture = data.get("profile_picture"),
            twitter_handle=data.get('twitter_handle'),
            twitter_followers=data.get('twitter_followers'),
            instagram_handle=data.get('instagram_handle'),
            instagram_followers=data.get('instagram_followers'),
            facebook_handle=data.get('facebook_handle'),
            facebook_followers=data.get('facebook_followers')
        )
        db.session.add(influencer)
        db.session.commit()
        token = user.get_auth_token()
        return jsonify({
            'message': 'Influencer registered successfully',
            'token': token,
            'user': {
                'id': user.id,
                'email': user.email,
                'roles': ['influencer']
            }
        }), 201
    except Exception as e:
        return jsonify({"success":False, "message": "could not register influencer", "error": e})

    
# sponsor registration
@auth.route('/sponsorRegister', methods=['POST'])
def register_sponsor():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    existing_user = datastore.find_user(email=email)
    if(existing_user):
        return jsonify({"success":False, "message":"Email already registerd"}), 404
    # Create user first
    user = datastore.create_user(
        email=email,
        password=hash_password(password),
        roles=['sponsor'],
        active=False
    )
    db.session.commit()
    
    # Convert niche list to comma-separated string
    # niche_string = ','.join(data.get('niche', []))
    
    # Create influencer profile
    try:
        sponsor = Sponsor(
            id=user.id,
            full_name=data['full_name'],
            email=email,
            phone=data.get('phone'),
            address=data.get('address'),
            industry=data.get('induustry'),
            # niche=niche_string,
            website=data.get('website'),
            budget=data.get('budget'),
            
        )
        db.session.add(sponsor)
        db.session.commit()
        token = user.get_auth_token()
        return jsonify({
            'message': 'Influencer registered successfully',
            'token': token,
            'user': {
                'id': user.id,
                'email': user.email,
                'roles': ['influencer']
            }
        }), 201
    except Exception as e:
        return jsonify({"success":False, "message": "could not register sponsor", "error": e})
    

@auth.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    # Fetch all campaigns from the database
    campaigns = Campaign.query.all()

    # Convert the campaigns to a list of dictionaries
    campaign_list = []
    print("before creating campaign list****************************************")
    for campaign in campaigns:
        campaign_data = {
            "id": campaign.id,
            "name": campaign.name,
            "description": campaign.description,
            "start_date": campaign.start_date,  # Adjust if image URL or path is required
            "end_date": campaign.end_date,  # Adjust if image URL or path is required
            "budget": campaign.budget,
            "visibility": campaign.visibility,
            "goals": campaign.goals,  # Adjust if necessary
            "flagged": campaign.flagged,  # Adjust if necessary
            "sponsor_id": campaign.sponsor_id,  # Adjust if necessary
            "sponsor": campaign.sponsor.full_name,  # Adjust if necessary
            # "ad_requests": campaign.goals,  # Adjust if necessary
        }
        campaign_list.append(campaign_data)
    print("after creating campaign list")
    return jsonify({"success": True, "campaigns": campaign_list}), 201 # Return the campaign data as JSON


@auth.route('/api/add_campaign', methods=['POST'])
def add_campaign():
    data = request.get_json()

    # Validate required fields
    required_fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'visibility', 'sponsor_id']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'success': False, 'message': f'{field} is required'}), 400

    # Parse dates
    try:
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid date format'}), 400

    # Find the sponsor
    sponsor = Sponsor.query.get(data['sponsor_id'])
    if not sponsor:
        return jsonify({'success': False, 'message': 'Sponsor not found'}), 404
    # Create the new campaign
    new_campaign = Campaign(
        name=data['name'],
        description=data['description'],
        start_date=start_date,
        end_date=end_date,
        budget=data['budget'],
        visibility=data['visibility'],
        goals=data.get('goals'),
        sponsor_id=data['sponsor_id']
    )

    try:
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Campaign created successfully', 'campaign': new_campaign.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 501


@auth.route("/api/get_sponsor_campaign/<int:id>", methods = ["GET"])
def get_sponsor_campaigns(id):
    try:
        sps_campaigns = Campaign.query.filter_by(sponsor_id=id).all()
        if(sps_campaigns):
            return jsonify({
                "success": True,
                "sponsor_campaigns" : [campaign.to_dict() for campaign in sps_campaigns if campaign],
            })
        else:
            return  jsonify({
                "success": True,
                "message": "no campaigns found"
            })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 501


