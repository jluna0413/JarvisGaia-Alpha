import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    try:
        # Convert the input text to speech using pyttsx3
        engine.say(text)
        engine.runAndWait()
        return "done"
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"The request failed: {e}"

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            return text.lower()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Main function
def main():
    print("Welcome to Jarvis!")

    while True:
        user_input = record_audio()

        if user_input is not None and "play" in user_input or "spotify" in user_input:
            # Play music here
            speak("Playing music...")
        elif user_input is not None and "?" in user_input:
            # Ask a question
            response, command = parse_command(user_input)
            if len(response) > 0:
                speak(response)
            if len(command) > 0:
                execute_command(command)

if __name__ == "__main__":
    main()
