import python_weather
import asyncio
import os
from icrawler.builtin import GoogleImageCrawler
from spot import SpotifyController
import local_assist  # Now referring to the refactored local assistant
import time

# Initialize the Spotify controller (use your actual credentials here)
spotify_controller = SpotifyController(client_id="your_spotify_client_id", 
                                        client_secret="your_spotify_client_secret", 
                                        redirect_uri="http://localhost:8888/callback", 
                                        username="your_spotify_username")

# Fetch weather information using python_weather
async def get_weather(city_name):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city_name)
        return weather

# Search for images using GoogleImageCrawler
def search(query):
    google_Crawler = GoogleImageCrawler(storage={"root_dir": r'./images'})
    google_Crawler.crawl(keyword=query, max_num=1)

# Parse various commands and trigger appropriate actions
def parse_command(command):
    if "weather" in command:
        try:
            # Retrieve weather info for a given city
            weather_description = asyncio.run(get_weather("Chicago"))
            weather_info = f"Current weather in Chicago: {weather_description.current.temperature}°F, {weather_description.current.sky_text}"
            print(weather_info)
            # Use the local assistant to respond
            response = assist_local.ask_question_memory(weather_info)
            assist_local.TTS(response)
        except Exception as e:
            print(f"Error retrieving weather: {e}")

    elif "search" in command:
        # Image search functionality
        try:
            files = os.listdir("./images")
            [os.remove(os.path.join("./images", f)) for f in files]
            query = command.split("-")[1]  # Assume query comes after "search-"
            search(query)
        except Exception as e:
            print(f"Error during image search: {e}")

    elif "play" in command:
        # Play music
        try:
            response = spotify_controller.start_music()
            print(response)
        except Exception as e:
            print(f"Error playing music: {e}")

    elif "pause" in command:
        # Pause music
        try:
            response = spotify_controller.stop_music()
            print(response)
        except Exception as e:
            print(f"Error pausing music: {e}")

    elif "skip" in command:
        # Skip to next track
        try:
            response = spotify_controller.skip_to_next()
            print(response)
        except Exception as e:
            print(f"Error skipping to next track: {e}")

    elif "previous" in command:
        # Skip to previous track
        try:
            response = spotify_controller.skip_to_previous()
            print(response)
        except Exception as e:
            print(f"Error skipping to previous track: {e}")

    elif "spotify" in command:
        # Get current playing track info
        try:
            spotify_info = spotify_controller.get_current_playing_info()
            print(spotify_info)
            response = assist_local.ask_question_memory(spotify_info)
            assist_local.TTS(response)
        except Exception as e:
            print(f"Error fetching Spotify info: {e}")
