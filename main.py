from flask import Flask, render_template, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://jdbzrwypiusgxn:c18624cf57fc6e64fc19d9c245664691541fc01abeeef0f836be048a74e3243c@ec2-174-129-226-232.compute-1.amazonaws.com:5432/dbnb45i2duvp6o'
heroku = Heroku(app)
db = SQLAlchemy(app)


class Task(db.Model):
    task = db.Column(db.String(120), primary_key=True)
    checked = db.Column(db.Boolean)

    def __init__(self, task):
        self.task = task
        self.checked = False

    def __repr__(self):
        return '<Task {}>'.format(self.task)

@app.route("/")
def tasks():
    app.logger.info("called /tasks")
    tasks = db.session.query(Task).all()
    app.logger.info("queried")
    return render_template("todo.html", tasks=tasks)


@app.route("/add_task", methods=['POST'])
def add_task():
    intask = Task(request.form['newTask'])
    app.logger.info(intask)
    if intask.task != "":
        task_list = db.session.query(Task).all()
        duplicate = False
        for task_item in task_list:
            if task_item.task == intask.task:
                duplicate = True
        if not duplicate:
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


@app.route("/update_task", methods=["POST"])
def update_task():
    t = request.form['task']
    app.logger.info(t)
    check_task = db.session.query(Task).filter(Task.task == t).first()
    app.logger.info(check_task)
    if check_task.checked == False:
        check_task.checked = True
    else:
        check_task.checked = False;
    db.session.commit()
    return tasks()


@app.route("/rename_task", methods=["POST"])
def rename_task():
    t = request.form['task']
    newTask = request.form['newTaskName']
    app.logger.info(t)
    rename_task = db.session.query(Task).filter(Task.task == t).first()
    app.logger.info(rename_task)
    rename_task.task = newTask
    db.session.commit()
    return tasks()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)
