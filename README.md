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
- [R5: ORM]
- [R6: ERD]
- [R7: Model and database relationship]
- [R8: Application's Endpoints]


## API Setup

Please follow the steps below taking into consideration that were run on a MacOS operating system. 

1. Clone the API from the GitHub repository to your local machine. 
2. Open the terminal 
3. Run `python3 -m venv .venv`
4. Run `source .venv/bin/activate`
5. To install the required libraries run `pip3 install -r requirements.txt` into your terminal. 
6. Create a .env file and set your database URI and secret key. 
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

--> screenshots 

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

