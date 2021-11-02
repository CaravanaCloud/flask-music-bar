from unittest import mock
from app.spotify import Spotify


@mock.patch("httpx.Client.get")
def test_should_return_json(request_mock, spotify_mock):
    default_url = "https://faker.spotify.net"

    request_mock.return_value = mock.Mock(status_code=200)
    request_mock.return_value.json.return_value = spotify_mock

    spotify = Spotify(default_url)
    response = spotify.download()

    data = response.json()

    assert response.status_code == 200
    assert (
        data["albums"]["href"]
        == "https://api.spotify.com/v1/browse/new-releases?country=BR&offset=0&limit=20"
    )
