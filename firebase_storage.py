import firebase_admin
from firebase_admin import storage

def obtain_firebase_blob():
    # Key obtained in 'configuracion del proyecto -> cuentas de servicio'
    service_account_key = 'C:\property-improver\property-improver-2-firebase-adminsdk-mjk8o-a56fc1f7aa.json'
    cred = firebase_admin.credentials.Certificate(service_account_key)
    default_app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'property-improver-2.appspot.com'
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
            imgs.append('https://firebasestorage.googleapis.com/v0/b/property-improver-2.appspot.com/o/house'
                        + str(house_num) + '%2F' + str(img_name) + '.jpg?alt=media&token=ecb27b15-5543-4859-997c-63ebb2dea3be')

    return imgs