from flask import Flask, render_template,request
import utils

app = Flask(__name__)

@app.route("/add_data", methods =["GET","POST"])
def add_data():
  if request.method == "GET": 
    return render_template("home.html", methods=["GET","POST"])
  elif request.method == "POST":
    form = request.form
    n = form["name"]
    p = form["price"] 
    it= form["intro"]
    hl= form["highlights"]
    im1= form["image1"]
    im2= form["image2"]
    im3= form["image3"]
    im4= form["image4"]
    ev=form["evaluate"]
    adr=form["address"]
    uti=form["utilities"]
    note= form["note"]
    gad = form["gadgets"]
    bed = form["bedroom"]
    bat = form["bathroom"]
    fa = form["family"]

    utils.add(n,p,it,hl,im1,im2,im3,im4,ev,adr,uti,note,gad,bed,bat,fa) 
    return "OK !"

if __name__ == '__main__':
  app.run(debug=True)