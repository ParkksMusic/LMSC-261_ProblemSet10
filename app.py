from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/venues")
def venues():
    #Open csv file in Unicode
    file = open("entertainment-licenses.csv", "r", encoding="utf-8")
    reader = csv.reader(file)
    next(reader) # Skip the first line
    venues = list(reader) # Create a list
    file.close()
    return render_template("venues.html", venues=venues)

@app.route("/search", methods=["POST"])
def search():
    if request.method == 'POST':
        request.form['response']
        return "Search successful!"
    # Implement YOUR CODE HERE
    return "hello, world"