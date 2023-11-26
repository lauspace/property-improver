import firebase_admin
from firebase_admin import credentials, storage
import requests

# Initialize Firebase with your credentials
cred = credentials.Certificate("property-improver-4-firebase-adminsdk-mtvx2-8f800a232a.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'property-improver-4.appspot.com'})

# Reference to the image in storage
image_ref = storage.bucket().get_blob('house1/img_1.jpg')

# Get the download URL
url = image_ref.generate_signed_url(expiration=3600)  # URL expires in 1 hour

response = requests.get(url)
image_data = response.content

print(image_data)