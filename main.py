import firebase_storage
import house_evaluation
import house_damage
from PIL import Image

if __name__ == '__main__':
    client_key = '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
    model_url = 'https://property.restb.ai/v1/multianalyze'
    house_number = 1

    firebase_blob = firebase_storage.obtain_firebase_blob()
    # given house selected obtain images urls
    input_images = firebase_storage.obtain_images_path(firebase_blob, house_number)

    # Given images urls obtain json data (API use)
    house_data_json = house_evaluation.evaluate_images_using_API(model_url, client_key, input_images, save=True)
    # type = exterior, interior, bathroom, kitchen
    # Given json extract worst type
    score_dict, worst_type = house_evaluation.obtain_min_room_score(house_data_json)

    print("\nOur software has scored your property's four room types as follows: ")
    for item in score_dict:
        print("    - " + item + ": " + str(score_dict[item]))
    print("The worst room type is: " + worst_type)
    print("\nWe are analyzing the images of this type of images...")

    # Given worst type extract images with this type
    worst_images = house_evaluation.obtain_worst_type_imgs(worst_type, house_data_json, input_images)
    # Evaluate each worst type image and obtain the three worst
    top_worst_images = house_evaluation.evaluate_worst_imgs(model_url, client_key, worst_images)

    print("\nWe have analyzed all the images of the " + worst_type + " type and we are going to make a more in-depth "
                                                                     "analysis of those that have obtained the lowest scores.")


    model_url = 'https://api-us.restb.ai/vision/v2/multipredict'
    # Obtain damage state from worst images
    damage_state = house_damage.evaluate_damage(model_url, client_key, top_worst_images)

    if damage_state == 0: print("\nWe haven't found relevant damages in the lowest scores images.")
    else:
        print("We have found this relevant damages in the lowest scores images: ")
        for value in damage_state:
            print("    - " + value)






