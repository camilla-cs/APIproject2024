from datetime import date

from flask import Blueprint
from sqlalchemy import text

from init import db, bcrypt
from models.user import User
from models.post import Post
from models.event import Event
from models.location import Location 



db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    try:
        db.session.execute(text('DROP TABLE IF EXISTS event_user CASCADE'))
        db.session.execute(text('DROP TABLE IF EXISTS events CASCADE'))
        db.session.execute(text('DROP TABLE IF EXISTS users CASCADE'))
        db.session.commit()
        print("Tables dropped successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error dropping tables: {e}")


@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash("apple").decode("utf-8"),
            experience_level="12",
            is_admin=True
        ),

        User(
            username="Jon Snow",
            email= "jonsnow@email.com",
            experience_level="8",
            bio="I like snow. ",
            password=bcrypt.generate_password_hash("snow").decode("utf-8")
        )
    ]


    db.session.add_all(users)
 

    posts = [
        Post(
            content="Next event will be revealed soon!",
            date=date.today(),
            user=users[0]
        ),

        Post(
            content="Going at Sydney rock climbing gym in St.Peters with some friends this weekend, feel free to join us!!",
            date=date.today(),
            user=users[1]
        ),

       
    ]
    
    db.session.add_all(posts)

    events = [
        Event(
            title="Winter is coming.",
            date=date.today(),
            description="A nice weekend in the cold Perisher Valley! For more info see the instagram page.",
            difficulty_level= 17,
            location_id="1",
            is_admin=True
        ),

        Event(
            title="Beginner Climbing Session",
            date=date.today(),
            description="A session for beginners to get started with climbing.",
            difficulty_level=0,
            location_id="2",
            is_admin=True
        )
    ]
    
    db.session.add_all(events)
   

    locations = [
        Location (
            name = "Perisher Valley",
            address="-36.396624,148.405136",
            difficulty_level=5
        ),

        Location (
            name="BlocHaus Bouldering Sydney",
            address="49 Fitzroy St, Marrickville NSW 2204",
            difficulty_level=0
        )
    ]

    db.session.add_all(locations)


    db.session.commit()

    print("Tables seeded")
