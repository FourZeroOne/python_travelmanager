import requests
from unittest.mock import patch
from tests.utils import connect_for_ut

from travelmanager import Station


class TestStation:
    @patch.object(requests.Session, "get")
    def test_get(self, get_mock):
        connect_for_ut()
        get_mock.return_value.json.return_value = {"value": "test"}

        result = Station.get()
        assert result == {"value": "test"}
        get_mock.assert_called_once_with(
            "https://test_url/q",
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "call": "fetchstations",
            },
            timeout=5,
        )
