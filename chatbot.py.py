import random

# Predefined responses. Each key phrase maps to one or more possible replies,
# so the bot can pick a random one and feel a little less repetitive.
RESPONSES = {
    "hello": ["Hi there!", "Hello!", "Hey! Nice to see you."],
    "hi": ["Hi there!", "Hello!", "Hey! Nice to see you."],
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple chatbot built for the CodeAlpha internship!"],
    "whats your name": ["I'm a simple chatbot built for the CodeAlpha internship!"],
    "your name": ["I'm a simple chatbot built for the CodeAlpha internship!"],
    "help": ["I can chat about simple greetings. Try saying 'hello', 'how are you', or 'bye'."],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."],
}

DEFAULT_RESPONSE = "Sorry, I didn't understand that. Try saying 'help' to see what I can do."


def get_response(user_input: str) -> str:
    """Look at the user's input (case-insensitive), check it against known
    key phrases, and return an appropriate reply."""
    text = user_input.lower().strip()

    # Check each known phrase to see if it appears in the user's message
    for phrase, replies in RESPONSES.items():
        if phrase in text:
            return random.choice(replies)

    return DEFAULT_RESPONSE


def chat() -> None:
    """Run the chatbot loop until the user says 'bye' or types 'quit'/'exit'."""
    print("Simple Rule-Based Chatbot")
    print("Type 'bye', 'quit', or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ("quit", "exit"):
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    chat()