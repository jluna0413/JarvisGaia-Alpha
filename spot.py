import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyController:
    def __init__(self, client_id, client_secret, redirect_uri, username):
        """
        Initialize the SpotifyController with user credentials.
        """
        self.username = username
        self.scope = "user-read-currently-playing user-modify-playback-state"
        self.spotify = self.authenticate(client_id, client_secret, redirect_uri)
    
    def authenticate(self, client_id, client_secret, redirect_uri):
        """
        Authenticate with Spotify using Spotipy.
        """
        try:
            auth_manager = SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope=self.scope,
                username=self.username
            )
            return spotipy.Spotify(auth_manager=auth_manager)
        except Exception as e:
            print(f"Error during Spotify authentication: {e}")
            return None

    def get_current_playing_info(self):
        """
        Get information about the currently playing track.
        """
        try:
            current_track = self.spotify.current_user_playing_track()
            if current_track is None or 'item' not in current_track:
                return "No track is currently playing."
            
            artist_name = current_track['item']['artists'][0]['name']
            album_name = current_track['item']['album']['name']
            track_title = current_track['item']['name']

            return {
                "artist": artist_name,
                "album": album_name,
                "title": track_title
            }
        except Exception as e:
            return f"Error retrieving current track: {e}"

    def start_music(self):
        """
        Start/resume music playback.
        """
        try:
            self.spotify.start_playback()
            return "Playback started."
        except spotipy.SpotifyException as e:
            return f"Error starting playback: {str(e)}"

    def stop_music(self):
        """
        Pause music playback.
        """
        try:
            self.spotify.pause_playback()
            return "Playback paused."
        except spotipy.SpotifyException as e:
            return f"Error pausing playback: {str(e)}"

    def skip_to_next(self):
        """
        Skip to the next track.
        """
        try:
            self.spotify.next_track()
            return "Skipped to the next track."
        except spotipy.SpotifyException as e:
            return f"Error skipping to the next track: {str(e)}"

    def skip_to_previous(self):
        """
        Skip to the previous track.
        """
        try:
            self.spotify.previous_track()
            return "Skipped to the previous track."
        except spotipy.SpotifyException as e:
            return f"Error skipping to the previous track: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Replace these values with your Spotify credentials
    username = "your_spotify_username"
    client_id = "your_spotify_client_id"
    client_secret = "your_spotify_client_secret"
    redirect_uri = "http://localhost:8888/callback"

    spotify_controller = SpotifyController(client_id, client_secret, redirect_uri, username)

    # Example operations
    print(spotify_controller.get_current_playing_info())
    print(spotify_controller.start_music())
    print(spotify_controller.stop_music())
    print(spotify_controller.skip_to_next())
    print(spotify_controller.skip_to_previous())
