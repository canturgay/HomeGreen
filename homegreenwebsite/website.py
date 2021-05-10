import os
import logging
import datetime

from flask import Flask, request, Response, render_template
from database_helpers import connect, count


app = Flask(__name__)
from database_helpers import connect
logger = logging.getLogger()
# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')

def home():
    """returns homepage"""
    return render_template('index.html', page_title="HomeGreen", sequence="First", reduction="100")


@app.route('/api/checkuser', methods=['POST'])

def checkUser():
    global engine
    data = request.form["email"]

    query = f"SELECT * FROM Users WHERE email=\"{data}\";"
    
    exists = count(connect(query))

    if exists:
        
       return "User exists"
    
    else:
        try:
            return addNewUser(data)

        except:
            return "Error adding user"


@app.route('/api/addnewuser', methods=["POST"])
def addNewUser(data):
    if request.form.get('consentdata'):
        consentdata = 1
    else:
        consentdata = 0

    if request.form.get('news'):
        news = 1
    else:
        news = 0

    insert = f"INSERT INTO Users (email, date, notify, news) VALUES (\"{data}\", NOW(), {consentdata}, {news});"

    newUser = connect(insert)

    return "NEW USER ADDED"


