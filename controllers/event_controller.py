from datetime import date

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.event import Event, events_schema, event_schema
from models.location import Location, location_schema, locations_schema
from models.user import User, user_schema, users_schema

events_bp = Blueprint("events", __name__, url_prefix="/events")

#to get all the events 
@events_bp.route("/", methods=["GET"])
def get_all_events():
    try:
        events = Event.query.order_by(Event.date.desc()).all()
        return events_schema.dump(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#to get one event
@events_bp.route("/<int:event_id>", methods=["GET"])
def get_one_event(event_id):
    try:
        event = Event.query.get(event_id)
        if event:
            return event_schema.dump(event), 200
        else:
            return jsonify({"error": f"Event with id {event_id} not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

#to create a new event
@events_bp.route("/", methods=["POST"])
@jwt_required()
def create_event(): 
    body_data= request.get_json()
    
    location_id = body_data.get("location_id")
    location = Location.query.get(location_id)
    if not location:
        return jsonify({"error": f"Location with id {location_id} not found."}), 404

    admin_id = get_jwt_identity()
    if not admin_id:
        return {"error": "Only admin can create events."}, 403
    
    event = Event (
        title=body_data.get("title"),
        date=date.today(),
        description=body_data.get("description"),
        difficulty_level= body_data.get("difficulty_level"),
        location_id=body_data.get("location_id"), 
        is_admin=True
        
    ) 

    db.session.add(event)
    db.session.commit()

    return event_schema.dump(event)

#to delete an event
@events_bp.route("/<int:event_id>", methods=["DELETE"])
@jwt_required()
def delete_event(event_id): 
    admin_id = get_jwt_identity()
    if not admin_id:
        return jsonify({"error": "Only admin can delete events."}), 403
    
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": f"Event with id {event_id} deleted successfully."}), 200
    else:
        return jsonify({"error": f"Event with id {event_id} not found."}), 404
    
#to edit an event 
@events_bp.route("/<int:event_id>", methods=["PUT","PATCH"])
@jwt_required()
def edit_event(event_id): 
    body_data=request.get_json()
    admin_id = get_jwt_identity()
    if not admin_id:
        return {"error": "Only admin can edit events."}, 403
    
    event = Event.query.get(event_id)

    if event: 
        event.description = body_data.get("description",event.description) 
        event.title= body_data.get("title", event.title)

        db.session.commit()
        return event_schema.dump(event)
    
    else: 
        return {"error":f"Event with id {event_id} not found."}, 404 
    