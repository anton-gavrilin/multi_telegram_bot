
keyboard_buttons = ["Random number", "Throw dice", "Random person", "Random image"]

password_init_text = """Write in format:
        *site* = *password* (Add password)
        get *site* (Get password)
        get (Get all passwords)
        delete *site* (Delete password)
        delete (Delete all passwords)
        q (Quit)"""

translate_init_text = """Write in format:
        *source* to *destination*"""

currency_init_text = """Write in format:
        *currency* to *currency* : *amount*
        *currency* to *currency* in *year* : *amount*"""

notify_init_text = """Write in format:
        *week day* **:** - time when notify
        *amount* minute - every amount minute notify
        *amount* second - every amount second notify
        *amount* hour - every amount hour notify
        quit - Quit from notifier
        stop - stop all alerts"""

start_init_text = "Let's do something, choose a command, ma friend 😶‍🌫️🤯🤩😎👺👾🤖💪🤙👀👮‍♂️🐲🌚🌝🦍🐊🐅"

# ChatGPT texts

chatgpt_init_text = """Write anything what you want to AI:

for instruction click buttons below keyboard
for exit write 'q'"""

chatgpt_features_keyboard_buttons = ["Text completion", "Code completion", "Image generation"]

chatgpt_text_keyboard_buttons = [
    "Classification",
    "Generation",
    "Conversation",
    "Translation",
    "Conversion",
    "Summarization"
]

chatgpt_code_keyboard_buttons = [
    "Create",
    "Explain",
    "Edit"
]

chatgpt_image_keyboard_buttons = [
    "Generate",
    "Edits",
    "Variation"
]

chatgpt_text_classification = """To create a text classifier with the API, we provide a description of the task and a few examples
            
Classify the sentiment in these tweets:
1. "I can't stand homework"
2. "This sucks. I'm bored 😠"
3. "I can't wait for Halloween!!!"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate"

Tweet sentiment ratings:"""

chatgpt_text_generation = """You can ask for anything from story ideas, to business plans, to character descriptions and marketing slogans 
            
Brainstorm some ideas combining VR and fitness:"""

chatgpt_text_conversation = """The API is extremely adept at carrying on conversations with humans and even with itself.
            
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
Human:"""

chatgpt_text_translation = """Translate this into French, Spanish and Japanese:

What rooms do you have available?"""

chatgpt_text_conversion = """Convert movie titles into emoji.

Back to the Future: 👨👴🚗🕒 
Batman: 🤵🦇 
Transformers: 🚗🤖 
Star Wars:"""

chatgpt_text_summarization = """The API is able to grasp the context of text and rephrase it in different ways
            
                    Summarize this for a second-grade student:
                    Jupiter is the fifth planet from the Sun and the largest in the Solar System. 
                    It is a gas giant with a mass one-thousandth that of the Sun, 
                    but two-and-a-half times that of all the other planets in the Solar System combined."""

chatgpt_code_edit = """AI can refactor, rename, documentate, create code parts
// Some function or part of code
// Instruction of what to do"

// Write a function in python that calculates fibonacci"""

chatgpt_code_create = """Write small description of what method or class you would have, examples:
# Create a function called 'nameImporter' to add a first and last name to the database
# Java language
# Calculate the mean distance between an array of points"""

chatgpt_code_explain = """// Function 1: Part of code
// What does Function 1 do?"""

chatgpt_image_generate = """You can create an original image given a text prompt(image: write image text), examples:

image: a white siamese cat, image: a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears"""

chatgpt_image_edits = """You can edit and extend an image by uploading a mask(upload image and write image: about image, examples:

image: A sunlit indoor lounge area with a pool containing a flamingo"""

chatgpt_image_variation = """You can generate a variation of a given image, upload you image, and AI will send variation"""