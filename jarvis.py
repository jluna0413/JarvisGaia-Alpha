import pyttsx3
import speech_recognition as sr
import urllib.request
import json

class Jarvis:
    def __init__(self):
        self.name = "Jarvis"

    def speak(self, text):
        print(f"Jarvis: {text}")

    def listen(self):
        # Simulate listening (replace this with actual microphone input handling)
        return input("You: ")

    def handle_request(self, user_input):
        if "hello" in user_input:
            self.speak("Hello, Sir. How can I assist you?")
        elif "goodbye" in user_input:
            self.speak("Goodbye, Sir. Have a great day!")
        else:
            self.speak("I am not sure how to assist with that, Sir.")

    def run(self):
        while True:
            user_input = self.listen()
            if user_input:
                self.handle_request(user_input)
            if "goodbye" in user_input or "exit" in user_input:
                self.speak("Goodbye, Sir. Have a great day!")
                break


def listen(self):
    with self.microphone as source:
        self.recognizer.adjust_for_ambient_noise(source)
        self.speak("Listening...")
        try:
            audio = self.recognizer.listen(source, timeout=5)
            self.speak("Recognizing...")
            recognized_text = self.recognizer.recognize_google(audio)
            print(f"DEBUG: Recognized text: {recognized_text}")
            return recognized_text
        except sr.UnknownValueError:
            self.speak("I couldn't understand that, Sir.")
        except sr.RequestError:
            self.speak("I seem to be having trouble connecting, Sir.")
        except sr.WaitTimeoutError:
            self.speak("I didn't catch anything, Sir.")
    return ""

    def handle_request(self, request):
        request = request.lower()
        self.history.append(request)

        if "turn on the 3d printer" in request:
            self.devices["3D printer"] = True
            self.speak("The 3D printer has been turned on. #3d_printer-1")
        elif "turn off the 3d printer" in request:
            self.devices["3D printer"] = False
            self.speak("The 3D printer has been turned off. #3d_printer-0")
        elif "turn on the lights" in request:
            self.devices["lights"] = True
            self.speak("The lights have been turned on. #lights-1")
        elif "turn off the lights" in request:
            self.devices["lights"] = False
            self.speak("The lights have been turned off. #lights-0")
        elif "tell me about plants" in request:
            self.speak("Plants are vital for oxygen production and provide food, shelter, and medicine for various species, Sir.")
        elif "tell me a story" in request:
            self.speak("Once upon a time, an AI named Jarvis helped his commander achieve greatness. The end, Sir.")
        elif "can you help" in request:
            self.speak("Of course, Sir. Please tell me what you need assistance with.")
        elif "what time is it" in request:
            from datetime import datetime
            now = datetime.now().strftime("%I:%M %p")
            self.speak(f"The time is {now}, Sir.")
        else:
            self.speak("I am not sure how to assist with that, Sir.")

    def run(self):
        while True:
            user_input = self.listen()
            if user_input:
                self.handle_request(user_input)
            if "goodbye" in user_input or "exit" in user_input:
                self.speak("Goodbye, Sir. Have a great day!")
                break


if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
