import json
import random

# Load the response patterns from the JSON file
def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

# Find the appropriate response based on recognized text
def find_response(recognized_text, patterns):
    recognized_text = recognized_text.lower()
    print('Rec Text: ', recognized_text)
    
    for intent in patterns.get("intents", []):
        for pattern in intent.get("patterns", []):
            # Check if the recognized text contains any of the patterns
            # if pattern.lower() in recognized_text:
            if pattern.lower() == recognized_text:
                # Return a random response from the available responses to add variety
                return random.choice(intent.get("responses", ["Sorry, I don't have the answer to that yet."]))
    
    return "Sorry, I did not understand that."
