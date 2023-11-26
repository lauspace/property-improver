import requests
import json
from itertools import islice


def evaluate_worst_imgs(model, cli_key, images):
    images_eval = {}
    for image in images:
        image_json = evaluate_images_using_API(model, cli_key, [image])
        images_eval[image] = image_json['response']['solutions']["r1r6"]["property"]["score"]
    filtered_images_eval = {key: value for key, value in images_eval.items() if value is not None}
    sort_aux = sorted(filtered_images_eval.items(), key=lambda x: x[1])
    sorted_filtered_images_eval = dict(sort_aux)

    num_elements_to_store = min(3, len(sorted_filtered_images_eval))
    worst_images = list(islice(sorted_filtered_images_eval, num_elements_to_store))
    return worst_images

def evaluate_images_using_API(model, cli_key, images, save=False):
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
    response = requests.post(model, params=payload, json=request_body)

    # The response is formatted in JSON
    json_data = response.json()

    # Save JSON file
    if save:
        with open("data.json", "w") as file:
            json.dump(json_data, file)

    return json_data


def obtain_min_room_score(data):
    room_type_score = {}
    # Accessing scores from each room type
    scores_path = data["response"]["solutions"]["r1r6"]["summary"]["score"]
    room_type_score["bathroom"] = scores_path["bathroom"]
    room_type_score["exterior"] = scores_path["exterior"]
    room_type_score["interior"] = scores_path["interior"]
    room_type_score["kitchen"] = scores_path["kitchen"]

    filtered_dict = {key: value for key, value in room_type_score.items() if value is not None}
    return room_type_score, min(filtered_dict, key=filtered_dict.get)


def obtain_worst_type_imgs(type, json, images_list):
    images = []
    image_selected = 0
    room_classification = {
        'AerialView': 'exterior',
        'Attic': 'interior',
        'BackOfStructure': 'exterior',
        'Balcony': 'exterior',
        'Bar': 'interior',
        'Basement': 'interior',
        'BasketballCourt': 'exterior',
        'Bathroom': 'bathroom',
        'Bedroom': 'interior',
        'BonusRoom': 'interior',
        'Closet': 'interior',
        'Community': 'exterior',
        'Deck': 'interior',
        'DiningArea': 'interior',
        'Dock': 'exterior',
        'EntranceFoyer': 'interior',
        'Entry': 'interior',
        'ExerciseRoom': 'interior',
        'Fence': 'exterior',
        'FloorPlan': 'interior',
        'FrontOfStructure': 'exterior',
        'GameRoom': 'interior',
        'Garage': 'interior',
        'Gym': 'interior',
        'Hallway': 'interior',
        'Kitchen': 'kitchen',
        'Laundry': 'interior',
        'LivingRoom': 'interior',
        'Lobby': 'interior',
        'Map': 'interior',
        'MediaRoom': 'interior',
        'MudRoom': 'interior',
        'Office': 'interior',
        'Other': 'interior',
        'OutBuildings': 'exterior',
        'Pantry': 'interior',
        'Parking': 'interior',
        'Patio': 'exterior',
        'Playground': 'exterior',
        'Pool': 'exterior',
        'Reception': 'interior',
        'Sauna': 'interior',
        'SideOfStructure': 'exterior',
        'SittingRoom': 'interior',
        'Stable': 'exterior',
        'Stairs': 'interior',
        'Storage': 'interior',
        'SunRoom': 'interior',
        'TennisCourt': 'exterior',
        'UtilityRoom': 'interior',
        'View': 'exterior',
        'WalkInClosets': 'interior',
        'WineCellar': 'interior',
        'Yard': 'exterior',
    }

    type_selected_class = {key: value for key, value in room_classification.items() if value is type}

    # Access the JSON structure
    for result in json['response']['solutions'].get("roomtype_reso", {}).get("results", []):
        # Get the value of 'top_prediction'
        top_prediction = result.get("values", {}).get("top_prediction", {})

        # Check if 'label' is in the 'type_selected_class' set
        if top_prediction.get("label") in type_selected_class:
            # Add the image to the list
            images.append(images_list[image_selected])

        image_selected += 1

    return images