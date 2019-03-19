from db import datahome_collection
def add(name,info,price,intro,highlights,image1,image2,image3,image4,evaluate,address,utilities,note,gadgets,bedroom,bathroom,family):
    new_datahome = {
        "name": name,
        "info":info,
        "price": price,
        "intro": intro,
        "highlights": highlights,
        "image1": image1,
        "image2": image2,
        "image3": image3,
        "image4": image4,
        "evaluate":evaluate,
        "address": address,
        "utilities": utilities,
        "note": note,
        "gadgets": gadgets,
        "bedroom": bedroom,
        "bathroom": bathroom,
        "family": family,
    }

    datahome_collection.insert_one(new_datahome)