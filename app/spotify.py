from httpx import Client
import os


class Spotify:
    def __init__(self, default_url):
        self.default_url = default_url
        self.downloader = Client()

    def download(self):
        return self._make_request()

    def _make_request(self):
        token = os.getenv("SPOTIFY_TOKEN")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }
        return self.downloader.get(self.default_url, headers=headers)
