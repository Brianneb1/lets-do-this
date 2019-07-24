from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/brandon")
def brandon():
    return "Hello, Brandon"

@app.route("/fancy")
def fancy():
    return render_template("fancy.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")


if __name__ == "__main__":
    app.run(debug=True)