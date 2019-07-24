from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/brandon")
def salvador():
    return "Hello, Brandon"


if __name__ == "__main__":
    app.run(debug=True)