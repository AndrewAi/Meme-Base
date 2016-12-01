# Basic Flask / Python Web Application College Project.
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


The project was guided by the following excerpt from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.


## User Guide part 1:
### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

I used couchdb as my database.you must also install couchdb before you can run my project.
You can download couchdb here (http://couchdb.apache.org/,

Once these prerequisites are installed, the application can be run locally:
```bash
$ python app.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/.


## User Guide part 2:
### How to use this application
When you run the python app.py from the terminal or command prompt you will be prompted with a url
to enter into the address bar in a browser so that you can access the application.
Once you enter the url http://127.0.0.1:5000/ . the app will load the index page.
From here you have two options either create a new meme
or access a previously created meme that you created by entering your meme base data base name.

NOTE : you must create a meme base by creating and uploading a meme to the meme base before you can access your meme base.

### Create A meme:
To create a meme click on the create a new meme button in the Welcome to Meme base home page
 On the Create page you can upload and image,
 Overlay text on it and either download it onto your device or upload it to the meme base database.
 To upload it to the meme base data base you must enter in a valid name for your meme and a name for your meme base.
 
### View A meme:
 Enter in a valid meme base name on the Welcome to Meme base.
 Which will then retrieve your memes from the meme base if your meme base exists.
 


### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses Couchdb as a database.
Technologies that were used are list below:
Languages : Python, HTML, JavaScript(& Ajax), CSS
Libraries : jQuery, Bootstrap
Frameworks : Flask
Databases : Couchdb

Python 3 and Flask were requirements for the project, but Couchdb was selected by me
as it is easy to use and does not require much setup to get the web application up and running.

