
class chatbot:
    def __init__(self, name="Chatbot"):
        self.name = name
        self.intents = {
            "hello": ["hi", "hello", "hey", "good morning", "good evening"],
            "bye": ["bye", "goodbye", "see you", "later"],
            "thanks": ["thanks", "thank you", "thx"],
            "how are you": ["how are you", "how's it going", "what's up"],
            "help": ["help", "support", "assist"]
        }
        self.responses = {
            "hello": "Hello! How can I help you today?",
            "bye": "Goodbye! Have a great day!",
            "thanks": "You're welcome! 😊",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "help": "I can assist you with general queries. Try saying 'hello', 'bye', or 'thanks'."
        }

    def get_intent(self, user_input):
        user_input = user_input.lower()
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in user_input:
                    return intent
    
    def get_response(self, user_input):
        intent = self.get_intent(user_input)
        if intent:
            return self.responses[intent]
        else:
            return "I'm not sure how to respond to that. Try asking for 'help'."
        
    def chat(self):
        print(f"{self.name}: Hello! Type 'bye' to exit.")
        while True:
            user_input = input("Boss: ")
            if user_input.lower() in self.intents["bye"]:
                print(f"{self.name}: {self.responses['bye']}")
                break
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

bot = chatbot("Jarvis")

bot.chat()