from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Event (db.Model): 
    __tablename__="events"

    event_id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date= db.Column(db.Date)
    description= db.Column(db.String,nullable=False)
    difficulty_level= db.Column(db.Integer, nullable=False)
    is_admin= db.Column (db.Boolean,default=False)
    location_id= db.Column(db.Integer, db.ForeignKey("locations.location_id"),nullable=False)

    location = db.relationship("Location", back_populates="events")


class EventSchema(ma.Schema):
    location = fields.Nested("LocationSchema", only=["name","address"])

    class Meta: 
        fields=("event_id","title","date","description","difficulty_level","location")
    

event_schema=EventSchema()
events_schema=EventSchema(many=True)


