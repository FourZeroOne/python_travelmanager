import requests
from unittest.mock import patch
from tests.utils import connect_for_ut
from travelmanager.travelmanager_api import TravelManagerAPI


class TestTravelManagerAPI:
    def test_connect(self):
        connect_for_ut()
        assert TravelManagerAPI.api_url == "https://test_url/q"
        assert TravelManagerAPI.portal_id == "test_portal_id"
        assert TravelManagerAPI.token == "test_token"
        assert TravelManagerAPI.basic_params == {
            "portal": "test_portal_id",
            "token": "test_token",
        }

    @patch.object(requests, "get")
    def test_get(self, get_mock):
        connect_for_ut()

        get_mock.return_value.json.return_value = {"value": "test"}
        # act
        actual = TravelManagerAPI.get("test")
        # assert
        assert actual == {"value": "test"}

    """
    @patch.object(requests, "get")
    def test_get_error(self, get_mock):
        TravelManagerAPI.connect("test", "test_portal_id", "test_token")
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("Mocked 500 error")
        )
        get_mock.return_value = mock_response

        with pytest.raises(requests.exceptions.HTTPError):
            response = TravelManagerAPI.get("test")
            response.raise_for_status()
    """
    """
    def test_get(self):
        # arrange
        expected = "test"
        with patch.object(requests, "get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = expected
            # act
            actual = TravelManagerAPI.get("test")
            # assert
            assert actual == expected

    def test_get_with_params(self):
        # arrange
        expected = "test"
        with patch.object(requests, "get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = expected
            # act
            actual = TravelManagerAPI.get("test", {"test": "test"})
            # assert
            assert actual == expected

    """
