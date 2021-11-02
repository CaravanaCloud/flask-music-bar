from flask import render_template
from app.spotify import Spotify
from dotenv import load_dotenv

load_dotenv()


class HomeController:
    def index(self):
        default_url = "https://api.spotify.com/v1/browse/new-releases?country=BR&limit=20&offset=0"
        spotify = Spotify(default_url=default_url)
        releases = spotify.download()
        return render_template("index.html", releases=releases.json())
