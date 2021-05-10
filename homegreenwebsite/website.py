import os
import logging
import datetime
from num2words import num2words

from flask import Flask, request, Response, render_template
from database_helpers import connect, count


app = Flask(__name__)
from database_helpers import connect
logger = logging.getLogger()
# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')

def home():
    """ tries to count member numbers in database and calculate reduction and returns homepage or w/ dummy values"""
    try:
        query = f"SELECT * FROM Users;"
        con = connect(query)
        cou = int(count(con))
        ordinal = num2words(cou, to = 'ordinal')

        if cou <= 100:
            seq = ordinal
            sale = 100 - cou
            return render_template('index.html', page_title="HomeGreen", sequence=seq, reduction=sale)
        else:
            return "Sorry, our quota for alpha members is full"
    except:
         return render_template('index.html', page_title="HomeGreen", sequence="first", reduction=99)
        

    


@app.route('/api/checkuser', methods=['POST'])
def checkUser():
    """Checks the database for user w email as PK"""
    data = request.form["email"]

    query = f"SELECT * FROM Users WHERE email=\"{data}\";"
    
    exists = count(connect(query))

    try:
        if exists:
            
            return "User exists"
        
        else:
            try:
                return addNewUser(data)

            except:
                return "Error adding user"
    except:
        return "Error connecting database"


@app.route('/api/addnewuser', methods=["POST"])
def addNewUser(data):
    """adds user to database w email as PK"""
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


