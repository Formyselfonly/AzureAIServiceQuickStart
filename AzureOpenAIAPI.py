import os
import openai

# Set up OpenAI API credentials and endpoint
openai.api_type = "azure"
openai.api_base = "<YOUR_ENDPOINT_URL>"  # Replace with your endpoint URL
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY") or "<YOUR_API_KEY>"

# Define your deployment name (the name you assigned to the model in Azure)
deployment_name = "<YOUR_MODEL_NAME>"  # Replace with your model name


# 1.
# Text generation example
response = openai.Completion.create(
    engine=deployment_name,
    prompt="Write a short story about a time-traveling cat.",
    max_tokens=100,
    temperature=0.7
)

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

# Summarization request
response = openai.Completion.create(
    engine=deployment_name,
    prompt=f"Summarize the following text:\n\n{text}",
    max_tokens=50,
    temperature=0.3
)

# Print the summary
print("Summary:", response.choices[0].text.strip())


# 3.
# Context and question for Q&A
context = """
The Azure OpenAI Service offers powerful language models like GPT-3, which can generate human-like text. 
It can be used in applications ranging from customer support to content generation. Azure OpenAI enables 
developers to leverage these models securely within their own cloud infrastructure.
"""
question = "What can Azure OpenAI Service be used for?"

# Q&A request
response = openai.Completion.create(
    engine=deployment_name,
    prompt=f"Based on the following context, answer the question:\n\nContext: {context}\n\nQuestion: {question}",
    max_tokens=50,
    temperature=0.3
)

# Print the answer
print("Answer:", response.choices[0].text.strip())


# 4.
# Text to translate
text_to_translate = "Hello, how are you?"

# Translation request
response = openai.Completion.create(
    engine=deployment_name,
    prompt=f"Translate the following English text to French: '{text_to_translate}'",
    max_tokens=30,
    temperature=0.3
)

# Print the translation
print("Translation:", response.choices[0].text.strip())


# 5.
# User message
user_message = "What are the benefits of using Azure AI services?"

# Chatbot response
response = openai.Completion.create(
    engine=deployment_name,
    prompt=f"You are a helpful assistant. Respond to the user message:\n\nUser: {user_message}\nAssistant:",
    max_tokens=60,
    temperature=0.5
)

# Print chatbot's reply
print("Chatbot Reply:", response.choices[0].text.strip())
