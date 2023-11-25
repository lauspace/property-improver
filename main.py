import requests
import json

url = 'https://property.restb.ai/v1/multianalyze'
payload = {
  # Add your client key
  'client_key': '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
}
request_body = {
  "image_urls": ["C:/property-improver/data/bathroom_1.jpg"],
  "solutions": {"roomtype": 1.0, "roomtype_reso": 1.0, "style": 1.0, "r1r6": None, "c1c6": None, "q1q6": None, "features": 5.0, "features_reso": 2.0, "compliance": 3.0, "caption": None}
}

# Make the classify request
response = requests.post(url, params=payload, json=request_body)

# The response is formatted in JSON
json_response = response.json()

# Save JSON file
with open("data.json", "w") as file:
  json.dump(json_response, file)