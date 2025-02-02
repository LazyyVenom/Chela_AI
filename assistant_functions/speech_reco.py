import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False
        self.recognizing = False

    def recognize_speech_from_mic(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.listening = True
            print("Listening...")
            audio = self.recognizer.listen(source)
            self.listening = False
        try:
            print("Recognizing...")
            self.recognizing = True
            text = self.recognizer.recognize_google(audio)
            self.recognizing = False
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    final_text = recognizer.recognize_speech_from_mic()
    print(f"Final text: {final_text}")