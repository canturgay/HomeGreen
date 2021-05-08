import os
import logging
import datetime

from flask import Flask, request, Response, render_template, jsonify, redirect
from database_helpers import connect


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
    data = request.form["email"]

    query = f"SELECT EXISTS(SELECT * FROM Users WHERE email=\"{data}\");"


    try:
        exist = connect(query)
        return addNewUser(data)
    except:
        return "User already exists"



@app.route('/api/addnewuser', methods=["POST"])
def addNewUser(data):
    insert = f"INSERT INTO Users (email) VALUESgit add * (\"{data}\");"

    newUser = connect(insert)

    return "NEW USER ADDED"


