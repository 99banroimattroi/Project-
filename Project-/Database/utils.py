from db import datahome_collection
def add_data(name, summary, introduction, unique_features, special_note, rating, featured_photo,T2T5,T6CN,ptt,sdtt,sdtd,checkin_time,checkout_time,address_line,city,state,country,full_address,photos_1,thumbnail_1,photos_2,thumbnail_2,photos_3,thumbnail_3,photos_4,thumbnail_4,photos_5,thumbnail_5,photos_6,thumbnail_6,photos_7,thumbnail_7,photos_8,thumbnail_8,photos_9,thumbnail_9,photos_10,thumbnail_10,photos_11,thumbnail_11,photos_12,thumbnail_12,photos_13,thumbnail_13,photos_14,thumbnail_14,photos_15,thumbnail_15,photos_16,thumbnail_16,photos_17,thumbnail_17,photos_18,thumbnail_18,photos_19,thumbnail_19):
    data = {
       "name": name,
       "summary": summary,
       "introduction": introduction,
       "unique_features":unique_features,
       "special_note": special_note,
       "rating": rating,
       "featured_photo": featured_photo,
    }, 
    price =  {
        "T2-T5": T2T5,
        "T6-CN": T6CN,
        "Phi Tang Them": ptt,
        "So_dem_toi_thieu": sdtt,
        "So_dem_toi_da": sdtd,
        "checkin_time": checkin_time,
        "checkout_time": checkout_time, 
    },
    address = {
        "address_line": address_line,
        "city": city,
        "state": state,
        "country": country,
        "full_address": full_address,
    },
    photos= {
        {
        "photos_1": photos_1,
        "thumbnail_1": thumbnail_1,
        },
        {
        "photos_2": photos_2,
        "thumbnail_2": thumbnail_2,
        },
        {
        "photos_3": photos_3,
        "thumbnail_3": thumbnail_3,
        },
        {
        "photos_4": photos_4,
        "thumbnail_4": thumbnail_4,
        },
        {
        "photos_5": photos_5,
        "thumbnail_5": thumbnail_5
        },
        {
        "photos_6": photos_6,
        "thumbnail_6": thumbnail_6,
        },
        {
        "photos_7": photos_7,
        "thumbnail_7": thumbnail_7,
        },
        {
        "photos_8": photos_8,
        "thumbnail_8": thumbnail_8,
        },
        {
        "photos_9": photos_9,
        "thumbnail_9": thumbnail_9,
        },
        {
        "photos_10": photos_10,
        "thumbnail_10": thumbnail_10,
        },
        {
        "photos_11": photos_11,
        "thumbnail_11": thumbnail_11
        },
        {
        "photos_12": photos_12,
        "thumbnail_12": thumbnail_12,
        },
        {
        "photos_13": photos_13,
        "thumbnail_13": thumbnail_13,
        },
        {
        "photos_14": photos_14,
        "thumbnail_14": thumbnail_14,
        },
        {
        "photos_15": photos_15,
        "thumbnail_15": thumbnail_15,
        },
    },
        
    datahome_collection.insert_one(new_datahome)