import eel
import os
from backend_features.sound import playAssistantSound
from assistant_functions.speech_reco import SpeechRecognizer
import multiprocessing as mp

def listen_for_wake_word():
    recognizer = SpeechRecognizer()
    recognizer.listen_for_wake_word()

if __name__ == "__main__":
    eel.init("www")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    playAssistantSound()
    p = mp.Process(target=listen_for_wake_word)
    p.start()
    print("STARTING EEL APP")
    eel.start("index.html",mode=None)