from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.post import Post

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped") 


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
    db.session.commit()

    print("Tables seeded")
