# Basic Flask/Python Web Application College Project.
#### Data Representation and Querying Project 2016

This repository contains code and information for my third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
My lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project Overview
I have created a Single-Page Web Application (SPA) Called Meme Base.
This application allows the user to either create a new meme or view existing memes
that the user may have stored in the meme base database.
A Meme is commonly known as an image which has a text overlay.
Meme base allows the user to upload an image and overlay text on it.
The user then has the option ot donwload the meme or upload it to the meme base data base.
If the user decides to upload the meme.
They can then view it by typing in their meme base name and their memes will be retrieved by the database,
and displayed on the web page.
Initially, we considered three different applications:

1. A [ToDoListMe](http://todolistme.net/) alternative.
2. A [Pastebin](http://pastebin.com/) alternative.
3. A [Yelp](https://www.yelp.ie/) alternative.

In our early discussions, we excluded option 3 as it would be too difficult to construct in the short time we had to complete the project.
That left option 1 and 2.
We chose 2 after some consideration, as we were more interested in the idea.

The project was guided by the following excerpt from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.


### Team Members
We elected to complete this project as a team.
The team members are:
- Seasca the dog
- Marco the dog
- Mog the cat
All team members contributed to all aspects of the project.
However, Seasca was given the lead in documentation, Marco the lead in Python coding, and Mog was given the lead in front-end development (HTML, CSS and JS) and user experience.

### Meetings
Team meetings were held every Tuesday at 11am in the canteen at GMIT's Dublin Road campus for the duration of the project.
At these meetings, the management of the project was discussed, among other topics.
The project was divided into separate tasks, and each task was assigned to team members - usually on an individual basis.
At each meeting, Mog took notes using their laptop and assigned the tasks using GitHub Issues.


### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python webapp.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:4000/ .

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
We chose SQLite as it is easy to use and does not require much setup to get the web application up and running.


**Lecturer's note:** this is a very short README example. Much more information would be required here for a high grade.
