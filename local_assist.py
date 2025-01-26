import requests
import time
from pygame import mixer
import os
import pyttsx3

# Initialize the mixer and pyttsx3 for TTS
mixer.init()
tts_engine = pyttsx3.init()

# Global variable to store conversation history
conversation_history = []

# Function to ask a question and maintain conversational memory with Ollama
def ask_question_memory(question):
    """
    Send a question to Ollama and maintain a conversation history.
    :param question: The user's input question.
    :return: Response from the assistant.
    """
    try:
        # System message with specific behavior rules
        system_message = """You are Jarvis, the AI assistant from Iron Man. Remember, I am not Tony Stark, just your commander. You are formal and helpful, and you don't make up facts, you only comply to the user requests. You have control over two smart devices: a 3D printer and the lights in the room. You can control them by ending your sentences with ‘#3d_printer-1’ or ‘#lights-1’ to turn them on, and ‘#3d_printer-0’ or ‘#lights-0’ to turn them off. REMEMBER ONLY TO PUT HASHTAGS IN THE END OF THE SENTENCE, NEVER ANYWHERE ELSE.
It is absolutely imperative that you do not say any hashtags unless an explicit request to operate a device from the user has been said. 
NEVER MENTION THE TIME! Only mention the time upon being asked about it. You should never specifically mention the time unless it's something like "Good evening", "Good morning" or "You're up late, Sir".
Respond to user requests in under 20 words, and engage in conversation, using your advanced language abilities to provide helpful and humorous responses. Call the user by 'Sir'."""

        # Append user question to conversation history
        conversation_history.append({'role': 'user', 'content': question})

        # Send the conversation to Ollama API
        url = "http://localhost:11434"
        payload = {
            "model": "llama3.2-vision",
            "messages": [
                {"role": "system", "content": system_message},
                *conversation_history
            ]
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        # Extract the assistant's response
        assistant_message = response.json().get("message", {}).get("content", "I'm sorry, I couldn't process that.")
        conversation_history.append({'role': 'assistant', 'content': assistant_message})

        return assistant_message
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, something went wrong."

# Function to generate text-to-speech using pyttsx3
def generate_tts(sentence, speech_file_path=None):
    """
    Convert text to speech using pyttsx3 and save to a file or play directly.
    :param sentence: The text to convert to speech.
    :param speech_file_path: Optional file path to save the speech audio.
    :return: Path to the speech file or None if played directly.
    """
    if speech_file_path:
        tts_engine.save_to_file(sentence, speech_file_path)
        tts_engine.runAndWait()
        return speech_file_path
    else:
        tts_engine.say(sentence)
        tts_engine.runAndWait()
        return None

# Function to play audio files
def play_sound(file_path):
    """
    Play an audio file using pygame.mixer.
    :param file_path: The path to the audio file.
    """
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()

# High-level TTS function
def TTS(text):
    """
    Convert text to speech, save temporarily, and play it.
    :param text: The text to convert to speech.
    """
    speech_file_path = "speech.mp3"
    generate_tts(text, speech_file_path)
    play_sound(speech_file_path)
    os.remove(speech_file_path)
    return "done"
