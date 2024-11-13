import os
import requests

# Set up API key and endpoint
subscription_key = os.getenv("AZURE_TEXT_ANALYTICS_KEY") or "<YOUR_API_KEY>"
endpoint = "<YOUR_ENDPOINT_URL>/text/analytics/v3.1/sentiment"

# Define the input text
documents = {"documents": [{"id": "1", "language": "en", "text": "I love using Azure AI services!"}]}

# Set up headers and make the request
headers = {"Ocp-Apim-Subscription-Key": subscription_key, "Content-Type": "application/json"}
response = requests.post(endpoint, headers=headers, json=documents)

# Print the sentiment analysis result
if response.status_code == 200:
    sentiment = response.json()
    print("Sentiment Analysis:", sentiment)
else:
    print("Error:", response.status_code, response.text)
