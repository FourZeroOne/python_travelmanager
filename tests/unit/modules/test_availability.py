import requests
from unittest.mock import patch
from tests.utils import connect_for_ut

from travelmanager import Availability


class TestAvailabilty:
    @patch.object(requests, "get")
    def test_get(self, get_mock):
        connect_for_ut()
        get_mock.return_value.json.return_value = {"value": "test"}

        result = Availability.get(
            "test_product", "test_start_date", "test_stop_date"
        )
        assert result == {"value": "test"}
        get_mock.assert_called_once_with(
            "https://test_url/q",
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "product": "test_product",
                "start": "test_start_date",
                "stop": "test_stop_date",
                "call": "availability",
            },
        )
