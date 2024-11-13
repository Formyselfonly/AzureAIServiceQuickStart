import os
import requests

# Set up API key and endpoint
subscription_key = os.getenv("AZURE_TRANSLATOR_KEY") or "<YOUR_API_KEY>"
endpoint = "<YOUR_ENDPOINT_URL>/translate"
params = {
    "api-version": "3.0",
    "from": "en",
    "to": ["es", "fr"]  # Translate to Spanish and French
}

# Define the text to translate
headers = {"Ocp-Apim-Subscription-Key": subscription_key, "Content-Type": "application/json"}
body = [{"text": "Hello, how are you?"}]

# Make the API request
response = requests.post(endpoint, headers=headers, params=params, json=body)

# Print the translated text
if response.status_code == 200:
    translations = response.json()
    for translation in translations[0]['translations']:
        print(f"Translated to {translation['to']}: {translation['text']}")
else:
    print("Error:", response.status_code, response.text)
