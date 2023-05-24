import pytest
import requests
from unittest.mock import patch
from travelmanager.travelmanager_api import TravelManagerAPI


class TestTravelManagerAPI:
    def test_connect(self):
        TravelManagerAPI.connect("test_url", "test_portal_id", "test_token")
        assert TravelManagerAPI.api_url == "https://test_url/q"
        assert TravelManagerAPI.portal_id == "test_portal_id"
        assert TravelManagerAPI.token == "test_token"
        assert TravelManagerAPI.basic_params == {
            "portal": "test_portal_id",
            "token": "test_token",
        }

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
