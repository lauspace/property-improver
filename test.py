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

images = ['https://storage.googleapis.com/property-improver-4.appspot.com/house1/img_1.jpg?Expires=3600&GoogleAccessId=firebase-adminsdk-mtvx2%40property-improver-4.iam.gserviceaccount.com&Signature=XOODJouPWuRjwpJHlslkfmhTsk%2BjlUTi6YxysLu3p6exmdFQk2kh%2BZPLkc9t66qDk3AACtvlbqDYv40L5sHn1j%2FwZl4M7R1iW6fkylNKTIIfRAgfwWZv3boYUMa1gBzUwqlzkkrl5nGphVNSAoXvE06KcfPP42QduDbBVESmX104nKxDHqATB%2BwkjePrYAX7nSdivhvAHb3u6YwUiN6Pqqz5l8INIiAmbpkQiO6U4Bt8lFz7RfDwWtIlFktib6N8h2wHXJ6mBtCFk3VCuKgYYqcPwOH%2FztV6YKYWobLemQA%2BT4bAV0h5vC3jT%2BtpxbMQJB99SKPMxtu0159YNToNcw%3D%3D',
                  'https://firebasestorage.googleapis.com/v0/b/property-improver-4.appspot.com/o/house1%2Fimg_17.jpg?alt=media&token=4ac5e97b-2a8b-45c4-93a6-dcbd6175b73e']

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