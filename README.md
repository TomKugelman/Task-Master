# Task Master using Flask
> Author: Thomas Kugelman

> Date Created: June, 2020

> Languages: Python with Flask, CSS/HTML, deployed with Heroku.

> Webapp: <a style="color: Green;" href="https://taskmastercrudappwithflask.herokuapp.com/"><strong>Link to WebApp</strong></a> // Middle Mouse click to open in new tab

## Description
This web app allows the user to maintain a task list; providing functionality to create, update, and delete tasks. Tasks are stored within an SQLite local database.

This program uses Flask as a web framework and is deployed using Heroku.

PLEASE NOTE: As of July 20th, 2020 the app is running, but some problems with the Flask-Login module cause frequent internal errors due to the module not recognizing a user login and defaulting to an anonymous user. The problem here is that the program periodically checks if the user is logged in and accesses user info that is not present for an anonymous user. Usually a combination of refreshing, going back a page, or closing the page and reopening can solve the issue, but it is clearly less-than-optimal in its current state. This is top priority for me.

## Notes
My goal with this project was to create an app that can potentially increase my productivity. I love the idea of Kanban and Trello Boards and I figured it would be fun to start small and try to build my own version of those organization tools.

### What I learned
While building this project I learned a myriad of things along the way. My exposure to HTML and CSS has been pretty limited thus far. Completing the basic framework for this project has allowed me to gain some experience using web development tools like HTML, CSS, and Flask. 

The first iteration of this app used Flask-SQLAlchemy (a python module that provides functionality to create models that mimic database tables allowing for easy database manipulation). The next step was to add Google OAuth to the project. While that was totally new to me at the time, after reading documentation and following some guides I found it fairly intuitive. Several errors involving JSON files caused me trouble, but creating a custom JSONEncoder solved the issue (a painless fix). However, when I decided to separate out the database and primary functionality from just the "app.py" file, Flask-SQLAlchemy began to show some cracks. I decided to move to a more robust module to take care of database integration and landed on SQLAlchemy ORM. While requiring much more initial reading of the fantastic documentation, once it is implemented it works consistantly in much the same way Flask-SQLAlchemy does, but with less work-around needed for segmenting sections fo code.

### Roadmap
As this project is something I want to use regularly to increase my own productivity, I want to add features to make the experience better and more robust.

#### Step 1 (Completed): 
Implement basic CRUD functionality and a usable interface. 

#### Step 2 (Completed):
Add password protection, preventing others from using this app without permission (as this is being hosted on my GitHub and the app itself is usable by anyone). This project is a portfolio piece and I would prefer anyone looking at this app to only see information approved by me. Until this feature is completed I will be periodically checking in to make sure there is no inappropriate content (although the likelihood of that is low).

#### Step 3: 
Create stages of completion; much like how a Kanban or Trello board allows users to move tasks into different stages of development. "Planned", "Started", and "Implemented" are a few examples of catagories tasks could be marked under.

#### Potential Later Additions
These are outside the scope of this current project goals and may not be implemented. However, depending on how the project develops the viability of these features will likely change.

- Ability to create and maintain multiple projects like "Housework", "Project_A", "Hobby_Goals"
- Beautify the app. A basic CRUD app isn't particularly interesting to look at. I want to add interesting visual elements to make it easier on the eyes. This also includes audio ques when updating a task. Auditory stimulus can send dopamine to the brain and increase the desire to be productive.
