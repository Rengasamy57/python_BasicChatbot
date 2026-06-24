def get_response(user_input):
    """Return an appropriate response based on the user's input."""
    
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hey"]:
        return "Hello! How can I help you today?"
    elif user_input == "hi":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm just a program, but I'm doing great! Thanks for asking."
    elif user_input == "what is your name":
        return "I'm a simple chatbot created for the CodeAlpha internship task."
    elif user_input == "thank you":
        return "You're welcome!"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."


def start_chat():
    """Start the chatbot loop and interact with the user."""
    print("Chatbot: Hello! Type 'bye' to exit the chat.")

    while True:
       
        user_input = input("You: ")

        
        response = get_response(user_input)

        
        print("Chatbot:", response)

        
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    start_chat()