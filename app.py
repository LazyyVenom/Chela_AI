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
import speech_recognition as sr

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

# Speaking Thread
engine.say("Hello Sir, how can I help you?")
engine.runAndWait()

# Loading Image Analysis Model Here
model = md.vl(model=r"C:\users\anubhav choubey\Downloads\moondream-2b-int8.mf")

if __name__ == "__main__":
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = np.frombuffer(pcm, dtype=np.int16)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print('--------------------------------------------------')
            query = recognize_speech(microphone, recognizer)
            if query.lower() in ["quit", "exit", "bye bye", "bye"]:
                engine.say("Bye Bye Sir!")
                engine.runAndWait()
                break

            category = query_category(query)['Category']
            if category == "PLAY_CHESS":
                engine.say("Starting chess, Ready To Lose? ")
                engine.runAndWait()
                print("Playing chess...")
                subprocess.run(["python", "main.py"], cwd=r"C:\Users\Anubhav Choubey\Documents\Own_Projects\Chess")
            
            elif category == "ANALYZE_CURRENT_SCREEN":
                answer = further_evaluate(screen_analysis(model),query)
                engine.say("Starting chess, Ready To Lose? ")
                engine.runAndWait()
                print(answer)
            
            elif category == "TAKE_PICTURE_AND_ANALYSE":
                print(further_evaluate(camera_analysis(model),query))
            
            elif category == "USE_CLIPBOARD":
                print(use_clipboard_to_process(query))
            
            else:
                print(normal_talk(query))
        
print("Goodbye!")