import firebase_admin
from firebase_admin import storage

def obtain_firebase_blob():
    # Key obtained in 'configuracion del proyecto -> cuentas de servicio'
    service_account_key = 'property-improver-3-firebase-adminsdk-wussi-546eccd8af.json'
    cred = firebase_admin.credentials.Certificate(service_account_key)
    default_app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'property-improver-3.appspot.com'
    })
    bucket = storage.bucket()
    blob = list(bucket.list_blobs())

    return blob

def obtain_images_path(f_blob, house_num, imgs=[]):
    house_name_img = "house" + str(house_num) + "/img"

    # Obtain image paths from blob
    for blob in f_blob:
        if (house_name_img in blob.name):
            img_name = blob.name.split('/')[1].split('.')[0]
            imgs.append('https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house'
                        + str(house_num) + '%2F' + str(img_name) + '.jpg?alt=media&token=8316b6b3-d51c-4361-9f49-5ea9e5afb048')

    return imgs