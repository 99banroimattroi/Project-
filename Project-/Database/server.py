from db import datahome_collection
from flask import Flask, render_template, request, redirect
app = Flask(__name__)





@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/")



if __name__ == '__main__':
  app.run(debug=True)