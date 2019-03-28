from db import datahome_collection
def add_data(name, summary, introduction, unique_features, special_note, rating, featured_photo,Mon_to_thurs,Fri_to_sun,Phi_tang_them,So_dem_toi_thieu,So_dem_toi_da,checkin_time,checkout_time,address_line,city,state,country,full_address,photos_1,thumbnail_1,photos_2,thumbnail_2,photos_3,thumbnail_3,photos_4,thumbnail_4,photos_5,thumbnail_5,photos_6,thumbnail_6,photos_7,thumbnail_7,photos_8,thumbnail_8,photos_9,thumbnail_9,photos_10,thumbnail_10,photos_11,thumbnail_11,photos_12,thumbnail_12,photos_13,thumbnail_13,photos_14,thumbnail_14,photos_15,thumbnail_15):
    data = {
        "name": name,
        "summary": summary,
        "introduction": introduction,
        "unique_features":unique_features,
        "special_note": special_note,
        "rating": rating,
        "featured_photo": featured_photo,
 
        "Mon_to_thurs": Mon_to_thurs,
        "Fri_to_sun": Fri_to_sun,
        "Phi_tang_them": Phi_tang_them,
        "So_dem_toi_thieu": So_dem_toi_thieu,
        "So_dem_toi_da": So_dem_toi_da,
        "checkin_time": checkin_time,
        "checkout_time": checkout_time, 

        "address_line": address_line,
        "city": city,
        "state": state,
        "country": country,
        "full_address": full_address,

        "photos_1": photos_1,
        "thumbnail_1": thumbnail_1,

        "photos_2": photos_2,
        "thumbnail_2": thumbnail_2,
  
        "photos_3": photos_3,
        "thumbnail_3": thumbnail_3,
  
        "photos_4": photos_4,
        "thumbnail_4": thumbnail_4,
 
        "photos_5": photos_5,
        "thumbnail_5": thumbnail_5,
 
        "photos_6": photos_6,
        "thumbnail_6": thumbnail_6,
 
        "photos_7": photos_7,
        "thumbnail_7": thumbnail_7,
   
        "photos_8": photos_8,
        "thumbnail_8": thumbnail_8,
 
        "photos_9": photos_9,
        "thumbnail_9": thumbnail_9,
 
        "photos_10": photos_10,
        "thumbnail_10": thumbnail_10,

        "photos_11": photos_11,
        "thumbnail_11": thumbnail_11,

        "photos_12": photos_12,
        "thumbnail_12": thumbnail_12,

        "photos_13": photos_13,
        "thumbnail_13": thumbnail_13,

        "photos_14": photos_14,
        "thumbnail_14": thumbnail_14,

        "photos_15": photos_15,
        "thumbnail_15": thumbnail_15,


    }
    datahome_collection.insert_one(data)


    