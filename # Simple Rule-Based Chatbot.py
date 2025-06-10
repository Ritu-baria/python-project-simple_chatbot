# Simple Rule-Based Chatbot

def chatbot():
    print("🤖 Hello! I am ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  # Convert to lowercase for easy matching

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("Bot: I am a simple chatbot created by Python.")
        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great!")
        elif "what can you do" in user_input:
            print("Bot: I can chat with you and answer basic questions.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
