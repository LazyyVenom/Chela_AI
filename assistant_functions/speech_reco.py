import speech_recognition as sr
import pvporcupine
import pyaudio
import numpy as np

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False
        self.recognizing = False
        self.porcupine = pvporcupine.create(keywords=["blueberry"], sensitivities=[1])
        self.audio_stream = pyaudio.PyAudio().open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def recognize_speech_from_mic(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.listening = True
            print("Listening...")
            audio = self.recognizer.listen(source)
            self.listening = False
            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    def listen_for_wake_word(self):
        print("Listening for wake word...")
        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = np.frombuffer(pcm, dtype=np.int16)
            keyword_index = self.porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                self.recognize_speech_from_mic()
                break

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.listen_for_wake_word()