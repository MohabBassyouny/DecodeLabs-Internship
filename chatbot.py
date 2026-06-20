responses = {
    "hello": "Hi, How are you.",
    "how are you": "I'm fin, and you ? ",
    "what is your name": "I am Chatbot built by Mohab.",
    "help": " What do you need?",
    "status": "All systems are operational."
}

print("--- AI Chatbot ---")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    clean_input = user_input.lower().strip()
    
    if clean_input == 'exit':
        print("Bot: Shutting down... Goodbye!")
        break
        
    bot_reply = responses.get(clean_input, "I do not understand.")
    
    print("Bot:", bot_reply)
    print("-" * 30)