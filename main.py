from os import path

import requests
import json

import firebase_admin
from firebase_admin import credentials, initialize_app, storage

def evaluate_house(model, cli_key, images):
    url = model
    payload = {
        # Add your client key
        'client_key': cli_key
    }
    request_body = {
        "image_urls": images,
        "solutions": {"roomtype": 1.0, "roomtype_reso": 1.0, "style": 1.0, "r1r6": None, "c1c6": None, "q1q6": None,
                      "features": 5.0, "features_reso": 2.0, "compliance": 3.0, "caption": None}
    }

    # Make the classify request
    response = requests.post(url, params=payload, json=request_body)

    # The response is formatted in JSON
    json_data = response.json()

    # Save JSON file
    with open("data.json", "w") as file:
        json.dump(json_data, file)

    return json_data

def obtain_scores(data):
    # Accessing the property score parameter
    c1c6_score = data["response"]["solutions"]["c1c6"]["property"]["score"]

    return c1c6_score

def obtain_images_path(f_blob, house_num, imgs=[]):
    house_name_img = "house" + str(house_num) + "/img"
    num = 1

    for blob in f_blob:
        if (house_name_img in blob.name):
            img_name = blob.name.split('/')[num].split('.')[0]
            imgs.append('https://firebasestorage.googleapis.com/v0/b/property-improver.appspot.com/o/house' + str(house_num) +
                '%2F' + str(img_name) + '.jpg?alt=media&token=c34bc59e-8043-4e99-9a5b-6b45e100d8b9')

        
    return imgs

def obtain_firebase_blob():
    service_account_key = 'C:\property-improver\property-improver-firebase-adminsdk-3ggpz-bc0a5db718.json'
    cred = firebase_admin.credentials.Certificate(service_account_key)
    default_app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'property-improver.appspot.com'
    })
    bucket = storage.bucket()
    blob = list(bucket.list_blobs())

    return blob

if __name__ == '__main__':
    client_key = '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
    model_url = 'https://property.restb.ai/v1/multianalyze'
    house_number = 1

    firebase_blob = obtain_firebase_blob()
    input_images = obtain_images_path(firebase_blob, house_number)
    house_data = evaluate_house(model_url, client_key, input_images)
    scores = obtain_scores(house_data)

    print("C1C6 Score (condition):", scores)
