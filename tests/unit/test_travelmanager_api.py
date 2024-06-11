import requests
from unittest.mock import patch
from tests.utils import connect_for_ut
from travelmanager.travelmanager_api import TravelManagerAPI


class TestTravelManagerAPI:
    def test_connect(self):
        connect_for_ut()
        assert TravelManagerAPI.api_url == "https://test_url/q"
        assert TravelManagerAPI.portal_id == "test_portal_id"
        assert TravelManagerAPI.token == "test_token"  # nosec B105
        assert TravelManagerAPI.basic_params == {
            "portal": "test_portal_id",
            "token": "test_token",
        }

    @patch.object(requests.Session, "get")
    def test_get(self, get_mock):
        connect_for_ut()

        get_mock.return_value.json.return_value = {"value": "test"}
        # act
        actual = TravelManagerAPI.get("test")
        # assert
        assert actual == {"value": "test"}
