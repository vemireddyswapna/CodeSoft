import time
import sys

def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! Nice to meet you 😊"

    elif "name" in user_input:
        return "I'm CodSoft AI Chatbot 🤖"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 💙"

    elif "internship" in user_input:
        return "CodSoft internship helps students learn real-world skills!"

    elif "skills" in user_input:
        return "I can chat with you, answer questions, and assist you!"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day 👋"

    elif "help" in user_input:
        return """You can ask me:
• hello
• internship
• skills
• your name
• exit"""

    else:
        return "Sorry, I didn't understand that. Type 'help' to see options."

def main():

    print("\n" + "="*50)
    print("        🤖 CODSOFT AI CHATBOT 🤖")
    print("="*50)

    typing("Welcome! I'm your AI Assistant.")
    typing("Type 'help' to see options.")
    typing("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        response = chatbot_response(user_input)

        typing("Bot: " + response)

        if user_input.lower() in ["exit", "bye"]:
            break

main()