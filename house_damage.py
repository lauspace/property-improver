import requests


def evaluate_damage(model, cli_key, images):
    damage_detected = {}
    damage_result = []
    for image in images:
        json = evaluate_images_using_API_2(model, cli_key, image)
        dets = json['response']['solutions']['re_inspection_damage']['detections']
        labels = []
        if len(dets) != 0:
            for det in dets:
                labels.append(det.label)
            damage_detected[image] = labels
        else: damage_detected[image] = 0

        if all(value == 0 for value in damage_detected.values()): return 0
        else: return list(damage_result.values())

def evaluate_images_using_API_2(model, cli_key, image):
    payload = {
        # Add your client key
        'client_key': cli_key,
        'model_id': 're_inspection_damage',
        # Add the image URL you want to process
        'image_url': image
    }

    # Make the API request
    response = requests.get(model, params=payload)

    # The response is formatted in JSON
    json_response = response.json()

    return json_response


