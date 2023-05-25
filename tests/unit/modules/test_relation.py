import requests
from unittest.mock import patch
from tests.utils import connect_for_ut

from travelmanager import Relation


class TestRelation:
    @patch.object(requests, "get")
    def test_get(self, get_mock):
        connect_for_ut()
        get_mock.return_value.json.return_value = {"value": "test"}

        result = Relation.get("test_station", "test_date")
        assert result == {"value": "test"}
        get_mock.assert_called_once_with(
            "https://test_url/q",
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "station": "test_station",
                "date": "test_date",
                "call": "relations",
            },
            timeout=5,
        )
