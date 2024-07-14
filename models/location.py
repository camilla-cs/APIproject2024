from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Location(db.Model): 
    __table__= "locations"

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    difficulty_level= db.Column(db.Integer, nullable=False)

    event_id= db.Column(db.Integer, db.ForeignKey("events.id"),nullable=False)

    event= db.relationship("Event", back_populates="events")


class LocationSchema (ma.Schema): 
    event= fields.List(fields.Nested("EventSchema",only=["title","date"]))

    class Meta: 
        fields=("id","name","address","difficulty_level","events")

location_schema = LocationSchema()
locations_schema=LocationSchema(many=True)

 