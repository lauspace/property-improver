import requests
import json

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

def obtain_min_room_score(data):
    room_type_score = {}
    # Accessing scores from each room type
    scores_path = data["response"]["solutions"]["c1c6"]["summary"]["score"]
    room_type_score["bathroom"] = scores_path["bathroom"]
    room_type_score["exterior"] = scores_path["exterior"]
    room_type_score["interior"] = scores_path["interior"]
    room_type_score["kitchen"] = scores_path["kitchen"]

    filtered_dict = {key: value for key, value in room_type_score.items() if value is not None}
    return min(filtered_dict, key=filtered_dict.get)