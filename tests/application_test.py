from unittest import mock


@mock.patch("httpx.Client.get")
def test_visitors_view_musics_in_home_page(request_mock, spotify_mock, client):
    request_mock.return_value = mock.Mock(status_code=200)
    request_mock.return_value.json.return_value = spotify_mock

    response = client.get("/")

    assert response.status_code == 200
    assert "Simone & Simaria" in response.get_data(as_text=True)
    assert "Felipe Araújo" in response.get_data(as_text=True)
    assert "Os Barões Da Pisadinha" in response.get_data(as_text=True)
