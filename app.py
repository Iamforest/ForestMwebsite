from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("menuTemplate.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug = True)