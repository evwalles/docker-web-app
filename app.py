from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from os import path, environ
from pymongo import MongoClient
import sys
import optparse

app = Flask(__name__)
client = MongoClient('db', 27017)
db = client.peopledb

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        person = {
            'name': request.form['name']
        }
        try:
            db.peopledb.insert_one(person)
            return redirect('/')
        except:
            return 'There was an issue adding you'
    else:
        _people = db.peopledb.find()
        people = [person for person in _people]
        return render_template('index.html', people=people)

@app.route('/delete/<string:name>')
def delete(name):

    try:
        db.peopledb.remove({"name" : name})
        return redirect('/')
    except:
        return 'There was a problem deleting that person'

@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):

    if request.method == 'POST':

        try:
            db.peopledb.update_one({"name" : name},{'$set' : {"name" : request.form['name']}})
            return redirect('/')
        except:
            return 'There was a problem updating that person'

    else:
        return render_template('update.html', name=name)

if __name__=="__main__":
    parser = optparse.OptionParser(usage="python app.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print ("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)