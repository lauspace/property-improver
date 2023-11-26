import requests

def evaluate_images_using_API_2(images):
    model = 'https://api-us.restb.ai/vision/v2/multipredict'
    payload = {
        # Add your client key
        'client_key': '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3',
        'model_id': 're_inspection_damage',
        # Add the image URL you want to process
        'image_url': images
    }

    # Make the API request
    response = requests.get(model, params=payload)

    # The response is formatted in JSON
    json = response.json()
    return json

images = ['https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_33.jpg?alt=media&token=2c4c8968-76fe-4cee-aec1-2822bb7cb491',
                  'https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_11.jpg?alt=media&token=d5dc1a73-b70e-4065-8db8-0c09b52ef8a0',
          'https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e']

damage_detected = {}
for image in images:
    json_response = evaluate_images_using_API_2(image)
    dets = json_response['response']['solutions']['re_inspection_damage']['detections']
    labels = []
    if len(dets) != 0:
        for det in dets:
            labels.append(det['label'])
        damage_detected[image] = labels
    else: damage_detected[image] = 0