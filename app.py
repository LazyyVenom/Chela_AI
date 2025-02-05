from assistant_functions.llm_response_gen import (
    query_category,
    normal_talk,
    use_clipboard_to_process,
    further_evaluate
)
import moondream as md
from assistant_functions.text_image_model import screen_analysis, camera_analysis
import subprocess
import pyttsx3
from assistant_functions.speech_reco import recognize_speech
import pvporcupine
import pyaudio
import numpy as np
import threading
import speech_recognition as sr
import keyboard

# For Recognizing Wake Word
porcupine = pvporcupine.create(keywords=["blueberry"], sensitivities=[1])
audio_stream = pyaudio.PyAudio().open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

# Engine For Speaking
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Loading Image Analysis Model Here
model = md.vl(model=r"C:\users\anubhav choubey\Downloads\moondream-2b-int8.mf")

engine_lock = threading.Lock()

def speak_while_processing(text):
    with engine_lock:
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    engine.say("Hello Sir, how can I help you?")
    engine.runAndWait()
    print("At your service!")

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = np.frombuffer(pcm, dtype=np.int16)
        keyword_index = porcupine.process(pcm)

        # keyboard.read_event()
        if keyword_index >= 0 or keyboard.is_pressed('ctrl+shift+a'):
            print('--------------------------------------------------')
            engine.say("Yes")
            engine.runAndWait()
            query = recognize_speech(microphone, recognizer)
            print(query)
            
        elif keyboard.is_pressed('ctrl+shift+b'):
            engine.say("You Can Type You Query Sir")
            engine.runAndWait()
            query = input("Enter your query: ")

        else:
            continue

        if query.lower() in ["quit", "exit", "bye bye", "bye"]:
            engine.say("Bye Bye Sir!")
            engine.runAndWait()
            break

        if query == "":
            engine.say("I didn't get that")
            engine.runAndWait()
            continue

        category = query_category(query)['Category']
        print(category)

        if category == "PLAY_CHESS":
            engine.say("Starting Chess Ready to lose")
            engine.runAndWait()
            answer = "Playing chess..."
            subprocess.run(["python", "main.py"], cwd=r"C:\Users\Anubhav Choubey\Documents\Own_Projects\Chess")
        
        elif category == "ANALYZE_CURRENT_SCREEN":
            engine.say("Analyzing Screen will take little time")
            engine.runAndWait()
            answer = further_evaluate(screen_analysis(model),query)
            engine.say(answer)
            engine.runAndWait()
        
        elif category == "TAKE_PICTURE_AND_ANALYSE":
            engine.say("Analyzing Picture will take little time")
            answer = further_evaluate(camera_analysis(model),query)
            engine.say(answer)
            engine.runAndWait()
        
        elif category == "USE_CLIPBOARD":
            answer = use_clipboard_to_process(query)
            engine.say(answer)
            engine.runAndWait()
        
        else:
            answer = normal_talk(query)
            engine.say(answer)
            engine.runAndWait()
            
        print(answer)
        print('--------------------------------------------------')
        
print("Goodbye!")