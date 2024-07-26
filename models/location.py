from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Location(db.Model): 
    __tablename__= "locations"

    location_id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    difficulty_level= db.Column(db.Integer, nullable=False)

    events= db.relationship("Event", back_populates="location")


class LocationSchema (ma.Schema): 
    events= fields.List(fields.Nested("EventSchema",only=["title","date"]))

    class Meta: 
        fields=("location_id","name","address","difficulty_level","events")

location_schema = LocationSchema()
locations_schema=LocationSchema(many=True)

 