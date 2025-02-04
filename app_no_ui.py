from assistant_functions.llm_response_gen import query_category, normal_talk
# import pyttsx3

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

wanna_quit = False
print("Enter 'quit' to exit.")
while not wanna_quit:
    print('--------------------------------------------------')
    query = input("Enter your query: ")
    if query == "quit":
        wanna_quit = True
    else:
        category = query_category(query)['Category']
        print("CATEGORY CHOOSEN: ", category)
        if category == "FETCH_COLLEGE_RESULT":
            print("Anubhav The Great is adding Fetch Result Soon")
        elif category == "PLAY_CHESS":
            print("Anubhav The Great is adding Chess Soon")
        elif category == "ANALYZE_CURRENT_SCREEN":
            print("Anubhav The Great is adding Analyze Current screen Soon")
        elif category == "TAKE_PICTURE_AND_ANALYSE":
            print("Anubhav The Great is adding photo analysis Soon")
        elif category == "USE_CLIPBOARD":
            print("Anubhav The Great is adding Fetch Result Soon")
        else:
            print(normal_talk(query))

print("Goodbye!")