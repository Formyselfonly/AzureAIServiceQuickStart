import os
import requests

# Set up API key and endpoint
subscription_key = os.getenv("AZURE_COMPUTER_VISION_KEY") or "<YOUR_API_KEY>"
endpoint = "<YOUR_ENDPOINT_URL>/vision/v3.1/analyze"
image_url = "<IMAGE_URL>"

# Define the analysis parameters and headers
params = {"visualFeatures": "Description,Objects,Tags"}
headers = {"Ocp-Apim-Subscription-Key": subscription_key, "Content-Type": "application/json"}
data = {"url": image_url}

# Make the API request
response = requests.post(endpoint, headers=headers, params=params, json=data)

# Print the response
if response.status_code == 200:
    analysis = response.json()
    print("Image Analysis:", analysis)
else:
    print("Error:", response.status_code, response.text)
