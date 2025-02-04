from assistant_functions.llm_response_gen import query_category, normal_talk, use_clipboard_to_process
import moondream as md
from assistant_functions.text_image_model import screen_analysis, camera_analysis

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
        print("CATEGORY CHOSEN: ", category)
        if category == "FETCH_COLLEGE_RESULT":
            print("Anubhav The Great is adding Fetch Result Soon")
        elif category == "PLAY_CHESS":
            print("Anubhav The Great is adding Chess Soon")
        elif category == "ANALYZE_CURRENT_SCREEN":
            
        elif category == "TAKE_PICTURE_AND_ANALYSE":
            print("Anubhav The Great is adding photo analysis Soon")
        elif category == "USE_CLIPBOARD":
            print(use_clipboard_to_process(query))
        else:
            print(normal_talk(query))

print("Goodbye!")