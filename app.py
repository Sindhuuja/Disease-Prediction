import re
import random
from flask import Flask, request, jsonify,render_template


app = Flask(__name__)

@app.route('/')
def nlp():
    return render_template("nlp.html")

# Responses for different types of crises
crisis_responses = {
    'emergency': [
        "Please stay calm. Can you tell me your location?",
        "Call emergency services immediately. Do you need help with anything else?"
    ],
    'depression': [
        "I'm really sorry to hear that you're feeling this way. It's important to talk about it. Would you like me to find resources for you?",
        "It's okay not to be okay. Do you want to talk about what's bothering you?"
    ],
    'anxiety': [
        "Take a deep breath. You're not alone. Would you like me to suggest relaxation techniques?",
        "Try to focus on your breathing. Can I assist you further?"
    ],
    'suicidal': [
        "It's crucial to seek help immediately. Please call a helpline or emergency services. You matter!",
        "Your safety is the top priority. Please reach out to a trusted person or helpline right away."
    ],
    'default': [
        "I'm not sure I understand. Can you please rephrase or provide more details?",
        "I'm here to help. Could you please elaborate?"
    ],
    'greetings': [
        "Nice to meet you.How can I help you?"
    ]
}

# Define patterns for detecting different types of crises
crisis_patterns = {
    'emergency': [r'emergency', r'urgent', r'sos'],
    'depression': [r'depressed', r'sad', r'unhappy'],
    'anxiety': [r'anxious', r'nervous', r'stressed'],
    'suicidal': [r'suicidal', r'suicide', r'kill myself'],
    'greetings':[r'hi',r'hello',r'good morning',r'good afternoon',r'good evening']
}
def main():
    print("Welcome to the Crisis Response and Support Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for using the chatbot. Take care!")
            break
        crisis_type = detect_crisis(user_input)
        responses = crisis_responses.get(crisis_type, crisis_responses['default'])
        response = random.choice(responses)
        print("Bot:", response)

# Function to determine the type of crisis based on user input using regular expressions
def detect_crisis(text):
    for crisis_type, patterns in crisis_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return crisis_type
    return 'default'

# Route for handling user requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    crisis_type = detect_crisis(user_input)
    responses = crisis_responses.get(crisis_type, crisis_responses['default'])
    response = random.choice(responses)
    return jsonify({"bot_response": response})

if __name__ == "__main__":
    app.run(debug=True)
