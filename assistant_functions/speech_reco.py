import speech_recognition as sr
import pvporcupine
import pyaudio
import numpy as np
# import eel
import pyautogui

# class SpeechRecognizer:
#     def __init__(self):
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()
#         self.porcupine = pvporcupine.create(keywords=["blueberry"], sensitivities=[1])
#         self.audio_stream = pyaudio.PyAudio().open(
#             rate=self.porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=self.porcupine.frame_length
#         )

#     @eel.expose
#     def recognize_speech_from_mic(self):
#         with self.microphone as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")
#             eel.setAssistantText("Listening...")
#             audio = self.recognizer.listen(source)
#             try:
#                 eel.setAssistantText("Recognizing...")
#                 print("Recognizing...")
#                 text = self.recognizer.recognize_google(audio)
#                 return text
#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#             return None

#     def listen_for_wake_word(self):
#         print("Listening for wake word...")
#         while True:
#             pcm = self.audio_stream.read(self.porcupine.frame_length)
#             pcm = np.frombuffer(pcm, dtype=np.int16)
#             keyword_index = self.porcupine.process(pcm)
#             if keyword_index >= 0:
#                 self.handle_wake_word_detected()
#                 break

#     def handle_wake_word_detected(self):
#         self.recognize_speech_from_mic()

def recognize_speech(microphone, recognizer):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    
# def listen_for_wake_word(audio_stream, porcupine):
#     while True:
#         pcm = audio_stream.read(porcupine.frame_length)
#         pcm = np.frombuffer(pcm, dtype=np.int16)
#         keyword_index = porcupine.process(pcm)
#         if keyword_index >= 0:
#             return True