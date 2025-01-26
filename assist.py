import asyncio
import pygame
import time

# Initialize pygame
pygame.init()

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
        pygame.time.Clock().tick(10)

# Test playing a sound
if __name__ == "__main__":
    sound_file = "path/to/your/soundfile.mp3"  # Update with your actual file path
    print("Playing sound...")
    play_sound(sound_file)
    print("Sound finished!")
