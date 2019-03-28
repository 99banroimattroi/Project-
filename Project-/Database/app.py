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
    su =  form["summary"]
    intro = form["introduction"]
    uni = form["unique_features"]
    spec = form["special_note"]
    rat = form["rating"]
    fea = form["featured_photo"]

    t25 = form["T2-T5"]
    t6cn = form["T6-CN"]
    ttt = form["Phi Tang Them"]
    sdtt = form["So_dem_toi_thieu"]
    sdtd = form["So_dem_toi_da"]
    checki = form["checkin_time"]
    checko = form["checkout_time"]

    addl = form["address_line"]
    ci = form["city"]
    sta = form["state"]
    cou = form["country"],
    fad = form["full_address"]

    p1 = form["photos_1"]
    t1 = form["thumbnail_1"]
    p2 = form["photos_2"]
    t2 = form["thumbnail_2"]
    p3 = form["photos_3"]
    t3 = form["thumbnail_3"]
    p4 = form["photos_4"]
    t4 = form["thumbnail_4"]
    p5 = form["photos_5"]
    t5 = form["thumbnail_5"]
    p6 = form["photos_6"]
    t6 = form["thumbnail_6"]
    p7 = form["photos_7"]
    t7 = form["thumbnail_7"]
    p8 = form["photos_8"]
    t8 = form["thumbnail_8"]
    p9 = form["photos_9"]
    t9 = form["thumbnail_9"]
    p10 = form["photos_10"]
    t10 = form["thumbnail_10"]
    p11 = form["photos_11"]
    t11 = form["thumbnail_11"]
    p12 = form["photos_12"]
    t12 = form["thumbnail_12"]
    p13 = form["photos_13"]
    t13 = form["thumbnail_13"]
    p14 = form["photos_14"]
    t14 = form["thumbnail_14"]
    p15 = form["photos_15"]
    t15 = form["thumbnail_15"]
    p16 = form["photos_16"]
    t16 = form["thumbnail_16"]
    p17 = form["photos_17"]
    t17 = form["thumbnail_17"]
    p18 = form["photos_18"]
    t18 = form["thumbnail_18"]
    p19 = form["photos_19"]
    t19 = form["thumbnail_19"]



    utils.add(n,su,intro,uni,spec,rat,fea,t25,t6cn,ttt,sdtt,sdtd,checki,checko,addl,ci,sta,cou,fad,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19 ) 
    return "OK !"

if __name__ == '__main__':
  app.run(debug=True)