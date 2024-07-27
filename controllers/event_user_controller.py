from datetime import date

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.event import Event, events_schema, event_schema
from models.location import Location, location_schema, locations_schema
from models.user import User, user_schema, users_schema
from models.event_user import EventUser

eventuser_bp = Blueprint ("event_user",__name__,url_prefix="/events")

#to add user to a event
@eventuser_bp.route("/<int:event_id>/add_participant", methods=["POST"])
@jwt_required()
def add_participant(event_id):
    user_id = get_jwt_identity()
    event = Event.query.get(event_id)
    user = User.query.get(user_id) 

    if not event:
        return {"error": f"Event with id {event_id} not found."}, 404
    
    if not user:
        return {"error": f"User with id {user_id} not found."}, 404
    
    if user in event.participants:
        return {"error": "User already participating in the event."}, 400
    
    event.participants.append(user)
    db.session.commit()

    return {"message": f"User {user.username} added to event {event.title}."}, 200

#to remove a user from a event
@eventuser_bp.route("/<int:event_id>/<int:id>/remove_participant", methods=["DELETE"])
@jwt_required()
def remove_participant(event_id, id):
    user_id = get_jwt_identity()
    event = Event.query.get(event_id)
    user = User.query.get(id)
    
    if not event:
        return {"error": f"Event with id {event_id} not found."}, 404
    
    if not user:
        return {"error": f"User with id {id} not found."}, 404
    
    if user not in event.participants:
        return {"error": "User is not participating in the event."}, 400
    
    event.participants.remove(user)
    db.session.commit()
    
    return {"message": f"User {user.username} removed from event {event.title}."}, 200

#to get all participants to an event (only admin can perform this action)
@eventuser_bp.route("/<int:event_id>/participants", methods=["GET"])
@jwt_required()
def get_participants(event_id):
    admin_id = get_jwt_identity()
    admin_user=User.query.get(admin_id)
    if not admin_id or not admin_user.is_admin:
        return jsonify({"error": "Only admin can perform this action."}), 403

    
    event = Event.query.get(event_id)
    if not event:
        return {"error": f"Event with id {event_id} not found."}, 404
    
    participants = [user.username for user in event.participants]
    return {"participants": participants}, 200

