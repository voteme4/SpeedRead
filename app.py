from flask import Flask, render_template, url_for
from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient('localhost', 27017)

@app.route("/")

def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)