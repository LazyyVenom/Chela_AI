from assistant_functions.llm_response_gen import (
    query_category,
    normal_talk,
    use_clipboard_to_process,
    further_evaluate
)
import moondream as md
from assistant_functions.text_image_model import screen_analysis, camera_analysis
import subprocess

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

model = md.vl(model=r"C:\users\anubhav choubey\Downloads\moondream-2b-int8.mf")

wanna_quit = False
print("Enter 'quit' to exit.")
while not wanna_quit:
    print('--------------------------------------------------')
    query = input("Enter your query: ")
    if query == "quit":
        wanna_quit = True
    else:
        category = query_category(query)['Category']
        # print("CATEGORY CHOSEN: ", category)
        if category == "PLAY_CHESS":
            print("Playing chess...")
            subprocess.run(["python", "main.py"], cwd=r"C:\Users\Anubhav Choubey\Documents\Own_Projects\Chess")
        elif category == "ANALYZE_CURRENT_SCREEN":
            print(further_evaluate(screen_analysis(model),query))
        elif category == "TAKE_PICTURE_AND_ANALYSE":
            print(further_evaluate(camera_analysis(model),query))
        elif category == "USE_CLIPBOARD":
            print(use_clipboard_to_process(query))
        else:
            print(normal_talk(query))

print("Goodbye!")