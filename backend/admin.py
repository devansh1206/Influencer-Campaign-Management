from flask import Flask, jsonify, request, redirect, session
from datetime import datetime
from models import db, User, Role, Campaign, CampaignInfluencers, Sponsor, UserRoles, Influencer, AdRequest
from flask import Blueprint, render_template, current_app as app
from flask_security import verify_password, hash_password, auth_required, current_user
from functools import wraps


admin_bp = Blueprint('admin', __name__)

# Route to fetch unapproved users
@admin_bp.route('/api/users', methods=['GET'])
# @auth_required('token')  # Assuming you are using JWT for authentication
def get_users():
    try:
        users = User.query.all()
        users_data = [user.to_dict() for user in users]  # Assuming you have a to_dict() method in User model
        return jsonify({"success": True, "users": users_data}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@admin_bp.route('/api/approve_user/<int:user_id>', methods=['POST'])
# @auth_required('token')
def approve_user(user_id):
    try:
        user = User.query.filter_by(id = user_id).first()
        
        if(not user):
           return jsonify({"success": True, "message": "user not registered yet"})
        if user.active:
            return jsonify({"success": True, "message": "User is already approved"}), 400
        user.active = True

        db.session.commit()
        return jsonify({"success": True, "message": "User approved successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@admin_bp.route('/api/flag_user/<int:user_id>', methods=['POST'])
# @auth_required('token')
def flag_user(user_id):
    try:
        user = User.query.filter_by(id = user_id).first()
        
        if(not user):
           return jsonify({"success": True, "message": "user not registered yet"})
        if user.flagged:
            return jsonify({"success": True, "message": "User is already flagged"}), 400
        user.flagged = True

        db.session.commit()
        return jsonify({"success": True, "message": "User flagged successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@admin_bp.route('/api/unapprove_user/<int:user_id>', methods=['POST'])
# @auth_required('token')
def unapprove_user(user_id):
    try:
        user = User.query.filter_by(id = user_id).first()

        if(not user):
           return jsonify({"success": True, "message": "user not registered yet"})
        if not user.active:
            return jsonify({"success": True, "message": "User is already unapproved"}), 400
        user.active = False
        
        db.session.commit()
        return jsonify({"success": True, "message": "User unapproved successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@admin_bp.route('/api/unflag_user/<int:user_id>', methods=['POST'])
# @auth_required('token')
def unflag_user(user_id):
    try:
        user = User.query.filter_by(id = user_id).first()

        if(not user):
           return jsonify({"success": True, "message": "user not registered yet"})
        if not user.flagged:
            return jsonify({"success": True, "message": "User is already unflagged"}), 400
        user.flagged = False
        
        db.session.commit()
        return jsonify({"success": True, "message": "User unflagged successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@admin_bp.route('/api/approve_campaign/<int:campaign_id>', methods=['POST'])
# @auth_required('token')
def approve_campaign(campaign_id):
    try:
        campaign = Campaign.query.filter_by(id = campaign_id).first()
        
        if(not campaign):
           return jsonify({"success": True, "message": "campaign not registered yet"})
        if campaign.active:
            return jsonify({"success": True, "message": "campaign is already approved"}), 400
        campaign.active = True

        db.session.commit()
        return jsonify({"success": True, "message": "campaign approved successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@admin_bp.route('/api/flag_campaign/<int:campaign_id>', methods=['POST'])
# @auth_required('token')
def flag_campaign(campaign_id):
    try:
        campaign = Campaign.query.filter_by(id = campaign_id).first()
        
        if(not campaign):
           return jsonify({"success": True, "message": "campaign not registered yet"})
        if campaign.flagged:
            return jsonify({"success": True, "message": "campaign is already flagged"}), 400
        campaign.flagged = True

        db.session.commit()
        return jsonify({"success": True, "message": "campaign flagged successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@admin_bp.route('/api/unapprove_campaign/<int:campaign_id>', methods=['POST'])
# @auth_required('token')
def unapprove_campaign(campaign_id):
    try:
        campaign = Campaign.query.filter_by(id = campaign_id).first()

        if(not campaign):
           return jsonify({"success": True, "message": "campaign not registered yet"})
        if not campaign.active:
            return jsonify({"success": True, "message": "campaign is already unapproved"}), 400
        campaign.active = False
        
        db.session.commit()
        return jsonify({"success": True, "message": "campaign unapproved successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@admin_bp.route('/api/unflag_campaign/<int:campaign_id>', methods=['POST'])
# @auth_required('token')
def unflag_campaign(campaign_id):
    try:
        campaign = Campaign.query.filter_by(id = campaign_id).first()

        if(not campaign):
           return jsonify({"success": True, "message": "campaign not registered yet"})
        if not campaign.flagged:
            return jsonify({"success": True, "message": "campaign is already unflagged"}), 400
        campaign.flagged = False
        
        db.session.commit()
        return jsonify({"success": True, "message": "campaign unflagged successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

