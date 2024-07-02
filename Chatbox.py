import re
rules = {
    r'hello': 'Hi there! How can I help you today?',
    r'hi': 'Hello! How are you doing?',
    r'how are you': 'I am just a chatbot, but I am here to help you!',
    r'what is your name': 'I am a chatbot created to assist you.',
    r'how can you help me': 'I can provide information, answer questions, and help with tasks.',
    r'bye': 'Goodbye! Have a great day!',
    r'thank you': 'You are welcome!',
    r'.help.': 'Sure, I am here to help you! What do you need assistance with?',
}

def chatbot_response(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()