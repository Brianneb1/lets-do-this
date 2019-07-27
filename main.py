from flask import Flask, render_template, send_from_directory, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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


@app.route("/add_task", methods=['GET','POST'])
def add_task():
    tasks = []
    if request.form:
        task = request.form['task']
        t = Task(task=task)
        db.session.add(t)
        db.session.commit()
        tasks = db.session.query(Task).all()
    return render_template("todo.html", tasks=tasks)

@app.route("/delete_task", methods=['DELETE'])
def delete_task():
    t = request.form['task']
    db.query.filter_by(task=t).delete(t)
    db.session.commit()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)