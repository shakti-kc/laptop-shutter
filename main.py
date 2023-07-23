import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./index.html")

@app.route("/shutdown", methods=["POST"])
def shutdown():
    os.system("shutdown /s")
    return "Magic processing..."


app.run(debug=True)
