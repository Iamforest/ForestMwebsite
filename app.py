from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def redirectToHome():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug = True)