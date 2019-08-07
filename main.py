from copy import copy

from flask import Flask, render_template, send_from_directory, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os
import sys
import json


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class Task(db.Model):
    task = db.Column(db.String(120), primary_key=True)
    checked = db.Column(db.Boolean)

    def __init__(self, task):
        self.task = task
        self.checked = False

    def __repr__(self):
        return '<Task {}>'.format(self.task)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fancy")
def fancy():
    return render_template("fancy.html")

@app.route("/tasks")
def tasks():
    app.logger.info("called /tasks")
    tasks = db.session.query(Task).all()
    app.logger.info("queried")
    return render_template("todo.html", tasks=tasks)


@app.route("/add_task", methods=['POST'])
def add_task():
    intask = Task(request.form['newTask'])
    app.logger.info(intask)
    db.session.add(intask)
    db.session.commit()
    app.logger.info("committed")
    return tasks()


@app.route("/delete_task", methods=['DELETE'])
def delete_task():
    t = request.form['task']
    app.logger.info(t)
    db.session.query(Task).filter(Task.task == t).delete()
    db.session.commit()
    return tasks()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)