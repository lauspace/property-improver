import requests
import json

import firebase_storage

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



if __name__ == '__main__':
    client_key = '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
    model_url = 'https://property.restb.ai/v1/multianalyze'
    house_number = 1

    firebase_blob = firebase_storage.obtain_firebase_blob()
    input_images = firebase_storage.obtain_images_path(firebase_blob, house_number)
    house_data = evaluate_house(model_url, client_key, input_images)
    scores = obtain_scores(house_data)

