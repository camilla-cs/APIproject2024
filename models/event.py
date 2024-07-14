from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Event (db.Model): 
    __table__="events"

    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date= db.Column(db.Date)
    description= db.Column(db.String,nullable=False)
    difficulty_level= db.Column(db.Integer, nullable=False)
   
    location_id= db.Column(db.Integer, db.ForeignKey("locations.id"),nullable=False)

    location = db.relationship("Location", back_populates="locations")


class EventSchema(ma.Schema):
    location = fields.Nested("LocationSchema", only=["name","address"])

    class Meta: 
        fields=("id","title","date","description","difficulty_level","locations")
    

event_schema=EventSchema()
events_schema=EventSchema(many=True)


