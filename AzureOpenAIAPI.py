import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-02-01"
)
# 1. Text generation
response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short story about a time-traveling cat."},
    ]
)
print(response.choices[0].message.content)


# Print the generated story
print("Generated Text:", response.choices[0].text.strip())


# 2.
# Long text input for summarization
text = """
Artificial intelligence is transforming industries, from healthcare to finance. With machine learning and 
natural language processing, AI systems are capable of automating tasks, improving efficiency, and providing 
new insights. This has led to advancements in personalized medicine, fraud detection, and more. However, there 
are also concerns about job displacement and ethical considerations.
"""

response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
    ]
)
print(response.choices[0].message.content)

# Print the summary
print("Summary:", response.choices[0].text.strip())


# 3.# Q&A request
# Context and question for Q&A
context = """
The Azure OpenAI Service offers powerful language models like GPT-3, which can generate human-like text. 
It can be used in applications ranging from customer support to content generation. Azure OpenAI enables 
developers to leverage these models securely within their own cloud infrastructure.
"""
question = "What can Azure OpenAI Service be used for?"


response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Based on the following context, answer the question:\n\nContext: {context}\n\nQuestion: {question}"},
    ]
)
print(response.choices[0].message.content)

# Print the answer
print("Answer:", response.choices[0].text.strip())


# 4.
# Text to translate
text_to_translate = "Hello, how are you?"

# Translation request
response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text_to_translate},
    ]
)

# Print the translation
print("Translation:", response.choices[0].text.strip())


# 5.
# User message
user_message = "What are the benefits of using Azure AI services?"

# Chatbot response
response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"You are a helpful assistant. Respond to the user message:\n\nUser: {user_message}\nAssistant:"},
    ]
)


# Print chatbot's reply
print("Chatbot Reply:", response.choices[0].text.strip())
