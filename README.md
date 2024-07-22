# T2A2 - Climbing events API - Camilla De Pretto

API webserver created for Coder Academy T2A2 assignment. 

[Github repository](https://github.com/camilla-cs/APIproject2024)

[Trello Board](https://trello.com/b/0Xr1Krxi/t2a2-api-assignment)

## Chapters 

- [API Setup](#api-setup)
- [R1: Addressing the problem](#r1-addressing-the-problem)
- [R2: Tracking the tasks]
- [R3: Packages]
- [R4: Benefits and drawback of the database's system]
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



 