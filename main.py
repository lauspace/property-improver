import firebase_storage
import house_evaluation

if __name__ == '__main__':
    client_key = '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
    model_url = 'https://property.restb.ai/v1/multianalyze'
    house_number = 1

    firebase_blob = firebase_storage.obtain_firebase_blob()
    input_images = firebase_storage.obtain_images_path(firebase_blob, house_number)
    house_data = house_evaluation.evaluate_house(model_url, client_key, input_images)
    room_to_improve = house_evaluation.obtain_min_room_score(house_data)


