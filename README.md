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

Please follow the steps below taking into consideration that were run on a MacOS operating system and Insomnia was used to run the server. 

1. Clone the API from the GitHub repository to your local machine. 

2. Open the terminal of choice. 

3. Run `python3 -m venv .venv` to create a virtual environment. 

4. Run `source .venv/bin/activate` to active the virtual environment. 

5. To install all the required packages run `pip3 install -r requirements.txt` into your terminal. 

6. Create a  separate .env file in the */src* folder and set your database URL and secret key based on the `.env.sample` file. 

7. Make sure you have installed and run PostgreSQL in the terminal. In case you don't have postgreSQL installed, run this command in the terminal: 
`pip install flask`

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
    

    events= db.relationship("Event", back_populates="location")
```
 

The use of foreign key constraints ensure that the relationships between tables are maintained , for example an event must be linked to a valid location and the participants partecipanting at events must be registered users.

This also allows data consistency and integrity but also facilitates querying of the database. For instance the API can easily fetch all the posts a user has created or retrieve all the partecipants of a specific event using the join-table EventUser. The creation of a join-table helps normalize the database , reducing data redundancy and ensuring a clear structure of the data, which will make the database's maintainance easier. 

The relationships between models also ensure flexibility in managing the data, as new locations can be added without affecting the events, and users can join or delete the partecipation to an event without damaging the other data. So, this scalability is crucual as the number of users and events grows. 

In conclusion, the clear relationships between models make managing data more straightforward and easy to implement updates or changes. 


## R8: Application's Endpoints

#### Register New User
 This route allows to register a user's account in order to login. 

**POST** method /auth/register


Body request example: 
```JSON
{
	"username":"Han Solo",
	"email":"hansolo@email.com",
	"experience_level":10,
	"password":"1234"
}
```
Response example:
 ```JSON
 {
	"id": 3,
	"username": "Han Solo",
	"email": "hansolo@email.com",
	"experience_level": 10,
	"bio": null,
	"is_admin": false,
	"posts": []
}
 
 ```

#### Login 
This allows user and admin to login, it will also give a Token (valid temporary) necessary to user to create, delete or edit a post, and for admin to create, delete, modify events as well as seeing the events' participants. 

**Login** method /auth/login 

Body request example: 
```JSON
{
	"email": "jonsnow@email.com",
	"password":"snow"
}

```

Response example: 
```JSON
{
	"email": "jonsnow@email.com",
	"is_admin": false,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMTk5MjUxNywianRpIjoiMTQxNzY5OWQtNzJlNi00OTIyLWE3YTMtOTAxZWFlMzc3ZGNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE3MjE5OTI1MTcsImNzcmYiOiIyOWVkNzFhNy0zNTRmLTQ0NDUtOGU1ZC03NTllMmJmNzAzYjgiLCJleHAiOjE3MjIwNzg5MTd9.a_FdipgHR-6_fJKpP8YyOZyt6nuXIFGHTiwE6PyCzrw"
}
```

#### Retrieve all posts

This route allows us to retrieve information about the posts created.

**GET** method /posts
 
 Body request: 
 Not needed 

Response example: 
```JSON
[
	{
		"user": {
			"id": 1,
			"username": null,
			"email": "admin@email.com"
		},
		"content": "Next event will be revealed soon!",
		"date": "2024-07-14"
	},
	{
		"user": {
			"id": 2,
			"username": "Jon Snow",
			"email": "jonsnow@email.com"
		},
		"content": "Going at Sydney rock climbing gym in St.Peters with some friends this weekend, feel free to join us!!",
		"date": "2024-07-14"
	}
]

```

#### Create New Post

**POST** method /posts

For this request is necessary a Token, that will be inserted in the Auth parameter, where 'Bearer Token' is selected.

Body request example: 
```JSON
{
	"content":"Does anyone know a good climbing spot for beginners?"
}

```

Response example: 
```JSON
{
	"user": {
		"id": 3,
		"username": "Han Solo",
		"email": "hansolo@email.com"
	},
	"content": "Does anyone know a good climbing spot for beginners?",
	"date": "2024-07-13"
}
```

#### Delete Post

Token of the user required. 

**DEL** method /posts/{post_id}

Body request: 
Not necessary

Response example: 
```JSON
{
    "message": "Post '{id}' deleted successfully"

}

```
#### Edit Post

Token required. 

**PATCH** method /posts/1 

Body request example: 
```JSON
{
	"content":"The new event location will be at the Blue Mountains! Keep in touch to hear more info!"
}
```

Response example: 
```JSON
{
	"user": {
		"id": 1,
		"username": null,
		"email": "admin@email.com"
	},
	"content": "The new event location will be at the Blue Mountains! Keep in touch to hear more info!",
	"date": "2024-07-15"
}
```

#### Retrieve All Events 

**GET** method /events

Body request example: 
Not needed. 

Response example: 
```JSON
[
	{
		"event_id": 1,
		"title": "Winter is coming.",
		"date": "2024-07-14",
		"description": "A nice weekend in the cold Perisher Valley! For more info see the instagram page.",
		"difficulty_level": 17,
		"location": {
			"name": "BlocHaus Bouldering Sydney",
			"address": "49 Fitzroy St, Marrickville NSW 2204"
		}
	},
	{
		"event_id": 2,
		"title": "Beginner Climbing Session",
		"date": "2024-07-14",
		"description": "A session for beginners to get started with climbing.",
		"difficulty_level": 0,
		"location": {
			"name": "Perisher Valley",
			"address": "-36.396624,148.405136"
		}
	}
]

```

#### Retrieve One Event 

**GET** method /events/{event_id}

Body request: 
Not needed 

Response example: 
```JSON 
{
	"event_id": 2,
	"title": "Beginner Climbing Session",
	"date": "2024-07-14",
	"description": "A session for beginners to get started with climbing.",
	"difficulty_level": 0,
	"location": {
		"name": "Perisher Valley",
		"address": "-36.396624,148.405136"
	}
}
```


#### Create New Event
 **POST** method /events 

 Token required. 

 Body request example: 
 ```JSON
{
	"title":"Family's Day at Climbing Gym",
	"description":"Bring your kids for a day of fun and games! Suitable for all ages and skill levels.",
	"difficulty_level":0,
	"location_id": 2,
	"is_admin": true
	
}
 ```

 Response example: 
 ```JSON
{
	"event_id": 3,
	"title": "Family's Day at Climbing Gym",
	"date": "2024-07-14",
	"description": "Bring your kids for a day of fun and games! Suitable for all ages and skill levels.",
	"difficulty_level": 0,
	"location": {
		"name": "BlocHaus Bouldering Sydney",
		"address": "49 Fitzroy St, Marrickville NSW 2204"
	}
}
 ```

 #### Delete Event

 Token required. 

 **DEL** method /events/{event_id}

Body request: 
Not needed. 


 ```JSON
Response example: 

 {
	"message": "Event with id 2 deleted successfully."
}
 ```

#### Edit Event

Token required. 

**PATCH** method /events/{event_id}

Body request example: 
```JSON
{
	"description":"UPDATED: because of heavy snow in the area the event is postponed. "
}
```

Response example: 
```JSON
{
	"event_id": 1,
	"title": "Winter is coming.",
	"date": "2024-07-14",
	"description": "UPDATED: because of heavy snow in the area the event is postponed. ",
	"difficulty_level": 17,
	"location": {
		"name": "Perisher Valley",
		"address": "-36.396624,148.405136"
	}
}
```

#### Add Participant to Event

Token required. 

**POST** method /events/{event_id}/add_participant

Body request example: 
Not needed. 

Response example: 
```JSON
{
	"message": "User {username} added to event Winter is coming.."
}
```

#### Remove participant to Event 

Token required. 

**DELETE** method /events/{event_id}/{user_id}/remove_participant 

Body request: 
Not needed. 

Response example: 

```JSON
{
	"message": "User Han Solo removed from event Winter is coming.."
}
```

#### Get Participants To Event 

Admin Token required. 

**GET** method /events/{event_id}/participants

Body request: 
Not needed. 

Response example: 

```JSON
{
	"participants": [
		"Han Solo"
        "Jon Snow"

	]
}
```

