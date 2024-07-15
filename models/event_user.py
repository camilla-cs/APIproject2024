from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp


#join table between users and events 
class EventUser(db.Model):
    __tablename__="event_user"
    event_user=db.Table("event_user",
                            db.Column("event_id",db.Integer,db.ForeignKey("events.event_id"), primary_key=True),
                            db.Column("user_id",db.Integer,db.ForeignKey("users.id"), primary_key=True)
)

