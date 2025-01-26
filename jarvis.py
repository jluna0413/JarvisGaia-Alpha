import speech_recognition as sr
import time
import assist
import spot

def record_audio():
    """
    Listens for audio input from the microphone.
    Returns the recognized speech or None if no speech is detected.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        r.energy_threshold = 4000  # Adjust the energy threshold to avoid false positives
        print("Listening for the hotword 'Jarvis'...")
        try:
            # Set timeout and phrase_time_limit to avoid long waits
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio, language="en-US")
            print(f"You said: {text}")
            return text.lower()  # Convert to lowercase for easier matching
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def listen_for_hotword():
    """
    Continuously listens for the hotword "Jarvis" and triggers actions when it's detected.
    """
    while True:
        user_input = record_audio()
        if user_input:
            print(f"Hotword detected: {user_input}")
            if "jarvis" in user_input:
                print("Hotword 'Jarvis' detected. Activating Jarvis!")
                # Once the hotword is detected, break the loop and activate Jarvis
                break
            else:
                print("Listening for the hotword 'Jarvis'...")
        time.sleep(1)

def main():
    """
    Main function to run the Jarvis AI assistant.
    """
    print("Welcome to Jarvis!")

    # Start listening for the hotword 'Jarvis'
    listen_for_hotword()

    # Once the hotword is detected, you can add further functionality here
    # Example: Greet the user and start additional tasks

    print("How can I assist you, Sir?")
    while True:
        user_input = record_audio()
        if user_input:
            if "weather" in user_input:
                print("Fetching weather information...")
                weather_info = asyncio.run(assist.get_weather("Chicago"))
                assist.TTS(weather_info)
            elif "play music" in user_input:
                print("Playing music...")
                spot.start_music()
            elif "pause music" in user_input:
                print("Pausing music...")
                spot.stop_music()
            elif "skip track" in user_input:
                print("Skipping track...")
                spot.skip_to_next()
            elif "exit" in user_input:
                print("Goodbye, Sir!")
                break
            else:
                print(f"Sorry, I didn't understand: {user_input}")
                assist.TTS("Sorry, I didn't catch that. Could you repeat?")
        time.sleep(1)

if __name__ == "__main__":
    main()
