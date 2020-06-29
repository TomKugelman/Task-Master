# Task Master using Flask
> Author: Thomas Kugelman

> Date Created: June, 2020

> Languages: Python with Flask, CSS/HTML, deployed with Heroku. .

> Webapp: <a style="color: Green;" href="https://taskmastercrudappwithflask.herokuapp.com/"><strong>Link to WebApp</strong></a>

## Description
This web app allows the user to maintain a task list; providing functionality to create, update, and delete tasks. Tasks are stored within an SQLite local database.

This program uses Flask as a web framework and is deployed using Heroku.

## Notes
My goal with this project was to create an app that can potentially increase my productivity. I love the idea of Kanban and Trello Boards and I figured it would be fun to start small and try to build my own version of those organization tools.

### What I learned
While building this project I learned a myriad of things along the way. My exposure to HTML and CSS has been pretty limited thus far. Completing the basic framework for this project has allowed me to gain some experience using web development tools like HTML, CSS, and Flask. 

### Roadmap
As this project is something I want to use regularly to increase my own productivity, I want to add features to make the experience better and more robust.

#### Step 1 (Completed): 
Implement basic CRUD functionality and a usable interface. 

#### Step 2:
Add password protection, preventing others from using this app without permission (as this is being hosted on my GitHub and the app itself is usable by anyone). This project is a portfolio piece and I would prefer anyone looking at this app to only see information approved by me. Until this feature is completed I will be periodically checking in to make sure there is no inappropriate content (although the likelihood of that is low).

#### Step 3: 
Create stages of completion; much like how a Kanban or Trello board allows users to move tasks into different stages of development. "Planned", "Started", and "Implemented" are a few examples of catagories tasks could be marked under.

#### Potential Later Additions
These are outside the scope of this current project goals and may not be implemented. However, depending on how the project develops the viability of these features will likely change.

- Ability to create and maintain multiple projects like "Housework", "Project_A", "Hobby_Goals"
- Beautify the app. A basic CRUD app isn't particularly interesting to look at. I want to add interesting visual elements to make it easier on the eyes. This also includes audio ques when updating a task. Auditory stimulus can send dopamine to the brain and increase the desire to be productive.
- Allow other users to create and manage their own task boards. Currently the database is shared between every user. This is not ideal, although a collaborative feature would be interesting.
