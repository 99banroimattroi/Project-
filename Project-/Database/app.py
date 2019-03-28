from flask import Flask, render_template,request
import utils

app = Flask(__name__)

@app.route("/add_data", methods =["GET","POST"])
def add_data():
  if request.method == "GET": 
    return render_template("home.html", methods=["GET","POST"])
  elif request.method == "POST":
    form = request.form
    name = form["name"]
    summary =  form["summary"]
    introduction = form["introduction"]
    unique_features = form["unique_features"]
    special_note = form["special_note"]
    rating = form["rating"]
    featured_photo = form["featured_photo"]
    Mon_to_thurs = form["Mon_to_thurs"]
    Fri_to_sun = form["Fri_to_sun"]
    Phi_tang_them = form["Phi_tang_them"]
    So_dem_toi_thieu = form["So_dem_toi_thieu"]
    So_dem_toi_da = form["So_dem_toi_da"]
    checkin_time = form["checkin_time"]
    checkout_time = form["checkout_time"]
    address_line = form["address_line"]
    city = form["city"]
    state = form["state"]
    country = form["country"]
    full_address = form["full_address"]
    photos_1 = form["photos_1"]
    thumbnail_1 = form["thumbnail_1"]
    photos_2 = form["photos_2"]
    thumbnail_2 = form["thumbnail_2"]
    photos_3 = form["photos_3"]
    thumbnail_3 = form["thumbnail_3"]
    photos_4 = form["photos_4"]
    thumbnail_4 = form["thumbnail_4"]
    photos_5 = form["photos_5"]
    thumbnail_5 = form["thumbnail_5"]
    photos_6 = form["photos_6"]
    thumbnail_6 = form["thumbnail_6"]
    photos_7 = form["photos_7"]
    thumbnail_7 = form["thumbnail_7"]
    photos_8 = form["photos_8"]
    thumbnail_8 = form["thumbnail_8"]
    photos_9 = form["photos_9"]
    thumbnail_9 = form["thumbnail_9"]
    photos_10 = form["photos_10"]
    thumbnail_10 = form["thumbnail_10"]
    photos_11 = form["photos_11"]
    thumbnail_11 = form["thumbnail_11"]
    photos_12 = form["photos_12"]
    thumbnail_12 = form["thumbnail_12"]
    photos_13 = form["photos_13"]
    thumbnail_13 = form["thumbnail_13"]
    photos_14 = form["photos_14"]
    thumbnail_14 = form["thumbnail_14"]
    photos_15 = form["photos_15"]
    thumbnail_15 = form["thumbnail_15"]

    utils.add_data(name,summary,introduction,unique_features,special_note,rating,featured_photo,Mon_to_thurs,Fri_to_sun,Phi_tang_them,So_dem_toi_thieu,So_dem_toi_da,checkin_time,checkout_time,address_line,city,state,country,full_address,photos_1,photos_2,photos_3,photos_4,photos_5,photos_6,photos_7,photos_8,photos_9,photos_10,photos_11,photos_12, photos_13, photos_14, photos_15,thumbnail_1,thumbnail_2,thumbnail_3,thumbnail_4,thumbnail_5,thumbnail_6,thumbnail_7,thumbnail_8,thumbnail_9,thumbnail_10,thumbnail_11,thumbnail_12,thumbnail_13,thumbnail_14,thumbnail_15) 

    return "OK !"

if __name__ == '__main__':
  app.run(debug=True)