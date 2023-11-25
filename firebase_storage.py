import firebase_admin
from firebase_admin import storage

def obtain_images_path(f_blob, house_num, imgs=[]):
    house_name_img = "house" + str(house_num) + "/img"
    num = 1

    for blob in f_blob:
        if (house_name_img in blob.name):
            img_name = blob.name.split('/')[num].split('.')[0]
            imgs.append(
                'https://firebasestorage.googleapis.com/v0/b/property-improver.appspot.com/o/house' + str(house_num) +
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