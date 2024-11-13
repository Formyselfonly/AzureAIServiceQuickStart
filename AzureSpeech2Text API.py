import os
import azure.cognitiveservices.speech as speechsdk

# Set up Speech SDK credentials
speech_key = os.getenv("AZURE_SPEECH_KEY") or "<YOUR_API_KEY>"
service_region = "<YOUR_REGION>"  # e.g., "westus"

# Initialize the speech recognizer
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_filename = "<PATH_TO_YOUR_AUDIO_FILE>"  # e.g., "path/to/audio.wav"
audio_input = speechsdk.AudioConfig(filename=audio_filename)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

# Recognize and print the speech
print("Recognizing speech from audio...")
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Text:", result.text)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized")
else:
    print("Error:", result.error_details)
