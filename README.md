# T2A2 - Climbing events API - Camilla De Pretto

API webserver created for Coder Academy T2A2 assignment. 

[Github repository](https://github.com/camilla-cs/APIproject2024)

[Trello Board](https://trello.com/b/0Xr1Krxi/t2a2-api-assignment)

## Chapters 

- [API Setup](#api-setup)
- [R1: Addressing the problem](#r1-addressing-the-problem)
- [R2: Tracking the tasks](#r2-tracking-the-tasks)
- [R3: Packages](#r3-packages)
- [R4: Benefits and drawback of the database's system](#r4-benefits-and-drawback-of-the-databases-system)
- [R5: ORM](#r5-orm)
- [R6: ERD](#r6-erd)
- [R7: Models and database relationship](#r7-models-and-database-relationship)
- [R8: Application's Endpoints](#r8-application's-endpoints)


## API Setup

Please follow the steps below taking into consideration that were run on a MacOS operating system. 

1. Clone the API from the GitHub repository to your local machine. 
2. Open the terminal 
3. Run `python3 -m venv .venv`
4. Run `source .venv/bin/activate`
5. To install the required libraries run `pip3 install -r requirements.txt` into your terminal. 
6. Create a .env file and set your database URL and secret key based on this example: 

-- mettere di creare user e database
7. Run `flask db create` to create the tables. 
8. Run `flask db seed `.
9. Run `flask run` to start the server on http://localhost:8080 

## R1: Addressing the Problem 
The intent behind this API project is to create a system for climbers to store rock climbing and bouldering routes, having the possibility to check the presence of any events and the possibility to create a community of climbing enthusiasts.

As a climber myself there are little events dedicated to climbers since most of them are being shared in closed forums or only in the gyms themselves. Moreover these informations are scattered in differe sites, making it difficult and more time consuming. 
There is no single platform where climbers can find detailed information about different climbing locations, their difficulty levels, and upcoming events and often lack a solid community space to engage with fellow climbers, share experiences and participate in events. 

This API allows to retain information about the location, difficulty level of a location and users are allowed to create posts. 
Admins can create events at different climbing locations, detailing the date and time of the event, and the different levels of experience required. Users can join or leave events and can decide whether to join an event by looking at the grade of difficulty.  


## R2: Tracking the tasks 

[Trello Board](https://trello.com/b/0Xr1Krxi/t2a2-api-assignment)

The tasks are tracked by using a kanban method in trello.com and organized them in : to do, doing and done. 
The tasks were mainly organized before designing and coding the API, and some were added along the way. 

First thing I focused on was the ERD diagram, essential for starting the coding part of the project. Then I divided the workload in three: I started coding the User and Post table, completing the models and controllers. I checked that the endpoints in Insomnia worked so I could do the same thing for Event, ClimbingLocation and the join table called UserEvent. 

Then the last thing that remained was the documentation part and making sure I would meet all the requirements. 

!!! --> screenshots !!! 

 ## R3: Packages

The packages used in this API are the following: 

### Flask
Flask is a WSGI web application framework easy to understand and is used to run web applications. 

### Marshmallow
Marshammlow is a ORM/ODM library used to convert complex datatypes such as objects to and from Python datatypes. In this project is mainly used to validate input data, serialize and deserialize data into objects that can then be rendered in JSON format. 

### PostgreSQL 
PostgreSQL is an open source object-relational database system that uses SQL languange and expands it, it is vastly used as it's robust and ACID compliant. In this project it is used to store and manage data, foreign keys relations and joins. 

### SQLAlchemy
SQLAlchemy is a Python's library that manages the database interactions. The ORM is used to define the database schema through Python classes, where each class represents a table in the database and the attributes represent the table's columns. It is also used to perform CRUD operations which are essential to manage the different relationships within the database. 
 
### Psycopg2
It's a Python adapter which allows a more direct interaction between Python and the PostgreSQL database, so that we are able to use Python commands to interact with the database. 

### Bcrypt 
Bcrypt is used to hash a user's password which is gonna be transformed into a fixed-lenght of characters, it help securing the password from external and malivolent attacks. 

### JWT-Extended 
In this API, JWT-Extended is a Flask's extension that creates tokens for users or admins which allow them authentication services thorugh the usage of JSON Web Tokens(JWT). 

### dotenv 
It's a library used to protect data and store them in a separate file. 

## R4: Benefits and drawback of the database's system 
The database system used for this project is PostgreSQL. 

### Benefits: 
#### it’s ACID compliant. 
That means it follows the principles of : 
- 1) Atomicity : the database ensures that either all the commands succeed or none at all. 
- 2) Consistency : 
- 3) Isolation: Transactions are executed in isolated environments to prevent interference. 
- 4) Durability: Makes sure that once a transaction is committed, its changes persist even in case of failure. 
#### supports advanced data type
can handle JSON and also XML, it also allows to create custom functions, languages and more. This is why it’s also
#### extensible. 
#### supports audio, images and video. 
#### strong security system with data encryption and advanced user authentication. 
#### it’s able to perform efficiently even with complex queries. 
#### it's able to handle multiple transactions at the same time. 
#### it is open source with a large community that contributes to improve and to support. 


### Drawbacks: 
#### protection issues: 
the open-source feature can also be problematic because it doesn’t come with a warranty or protection. Moreover, because it’s managed by many communities, it may lack user-friendly features. 
#### compability issues: 
Compatibility issues with some users tools or applications, requiring additional configuration. 
#### slower
Slower performance compared to SQL Server and MySQL
#### complex 
can be complex for beginners. 
#### memory usage 
can have a substantial impact on memory and CPU usage, as a consequence, it requires powerful hardware. 

## R5 : ORM 
The ORM language used for this project is SQLAlchemy.

Object-relational mapping allows developers to convert data between the database and the programming language used, and is based on abstraction, through wich developers don't need to know SQL to generate SQL queries. 

In this project it is used to facilitate the interaction between Python and the database. 

The key features are: 
- **Mapping** : by using Python classes to define database schema we are able to map the class attributes to the database table columns. This allows me to define the database schema in Python language. 
- **CRUD operations** are performed *more easily* thanks to a high-level query interface that allows for complex queries using Python functions. 
- It supports the definition of *relationships between tables*, allowing complex data relationship using Python code so that data manipulation and retrieval is easier. 
- it can *create automatically database schema* without needing to write SQL for generating tables. 

The ORM makes the code more readable and clear across different platforms, easier to maitain since we don't need to write SQL queries inside the code. Many ORM tools have the advantage of  reducing time and improving the overall performance by implementing automatic common tasks such as creating, uptading and deleting, validating and managing data. 



## R6: ERD

![ERD Diagram](/docs/api_2024.drawio.png)

Based on this ERD diagram we can have an idea of the tables and relationships of the API. 

Starting from the top left we have  'User' table which is linked to 'Post' table by a one-to-many relationship. This means that one and only one user will be able to create posts , or none at all. 

Between 'User' and 'Event' table there is a many-to-many relationship so a join table named 'EventUser' is created. One User can partecipate at many events, at the same time one event can have many users. This allows the admin to see which users will be attending which event. 

Finally, one-to-many relationship takes place between 'Event' and 'Location' tables, where in one location can take place many events, but one event can have one and only one climbing location happening. --> RIGUARDA !!  

## R7: Models and database relationships 

Each model has a separate file in the models folder and they are the following: 

#### - User Model
```python
class User(db.Model): 
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True) 
    experience_level= db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String, nullable=True)
    password = db.Column (db.String,nullable=False)
    is_admin= db.Column (db.Boolean,default=False) 

    #to connect to post model 
    posts = db.relationship('Post', back_populates="user")
    #to connect to event model 
    events=db.relationship("Event",secondary="event_user",backref="users",cascade="all,delete")

```
The **User model** represents the users table in the database and it relates to the **Post model** through a *one-to-many* relationship, but also to the **event model** with a *many-to-many* relationship that is taken care by a join table called **EventUser** . 

#### - Post Model 
```python
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String,nullable=False)
    date = db.Column(db.Date)
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    #to get info about the user
    user = db.relationship('User', back_populates='posts')

```
The **Post model** contains the user_id as foreign key to link every post that has been created to its own owner, but you'll also be able to get information about the user's personal details such as *id*,*email* and *username*. 

#### - Event Model
```python
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

    participants= db.relationship("User", secondary="event_user",backref=db.backref('events_partecipating', lazy='dynamic'))
```
As we can see in the model above, only an admin can create an event, and there's also a foreign key called location_id that links this model to the **Location model** through a one-to-many relationship. 
The admin can also retrieve information about the location details as well as the partecipants that are gonna join the event through the EventUser table as seen below. 

#### - EventUser Model 

```python
#join-table between users and events 
class EventUser(db.Model):
    __tablename__="event_user"
    event_user=db.Table("event_user",
                            db.Column("event_id",db.Integer,db.ForeignKey("events.event_id"), primary_key=True),
                            db.Column("user_id",db.Integer,db.ForeignKey("users.id"), primary_key=True)
)

```
This join-table allow the admin to see to which event users will join and all the details not only about the event and the user, but also the location's ones. 

#### - Location Model 
```python
class Location(db.Model): 
    __tablename__= "locations"

    location_id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    difficulty_level= db.Column(db.Integer, nullable=False)
    event_id= db.Column(db.Integer, db.ForeignKey("events.event_id"),nullable=False)

    events= db.relationship("Event", back_populates="location")
```
The presence of event_id reminds us of the one-to-many relationship with Event model. 

The use of foreign key constraints ensure that the relationships between tables are maintained , for example an event must be linked to a valid location and the participants partecipanting at events must be registered users.

This also allows data consistency and integrity but also facilitates querying of the database. For instance the API can easily fetch all the posts a user has created or retrieve all the partecipants of a specific event using the join-table EventUser. The creation of a join-table helps normalize the database , reducing data redundancy and ensuring a clear structure of the data, which will make the database's maintainance easier. 

The relationships between models also ensure flexibility in managing the data, as new locations can be added without affecting the events, and users can join or delete the partecipation to an event without damaging the other data. So, this scalability is crucual as the number of users and events grows. 

In conclusion, the clear relationships between models make managing data more straightforward and easy to implement updates or changes. 


## R8: Application's Endpoints
