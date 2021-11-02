from app import create_app
from pytest import fixture
import json


@fixture
def spotify_mock():
    with open("tests/fixtures/spotify.json") as f:
        return json.loads(f.read())


@fixture
def client():
    app = create_app()
    app.testing = True

    return app.test_client()
