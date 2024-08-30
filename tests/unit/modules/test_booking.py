import requests
from unittest.mock import patch
from tests.utils import connect_for_ut

from travelmanager import Booking
from travelmanager.schemas import Ticket


class TestBooking:
    @patch.object(requests.Session, "post")
    def test_create(self, post_mock):
        connect_for_ut()
        post_mock.return_value.json.return_value = {"value": "test"}

        result = Booking.create(
            "product",
            "booking_date",
            [Ticket("8", "3"), Ticket("1", "2")],
            "customer_name",
            "phone",
            "email",
            "reference",
        )
        assert result == {"value": "test"}
        post_mock.assert_called_once_with(
            "https://test_url/q",
            json={
                "product": "product",
                "date": "booking_date",
                "ticket": [
                    {"id": "8", "quantity": "3", "type": 1},
                    {"id": "1", "quantity": "2", "type": 1},
                ],
                "customer": "customer_name",
                "phone": "phone",
                "email": "email",
                "booking_reference": "reference",
                "remarks": "",
            },
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "call": "booking",
            },
            timeout=5,
        )

    @patch.object(requests.Session, "post")
    def test_create_with_accessoirs(self, post_mock):
        connect_for_ut()
        post_mock.return_value.json.return_value = {"value": "test"}

        result = Booking.create(
            "product",
            "booking_date",
            [Ticket("8", "3", 2), Ticket("1", "2")],
            "customer_name",
            "phone",
            "email",
            "reference",
        )
        assert result == {"value": "test"}
        post_mock.assert_called_once_with(
            "https://test_url/q",
            json={
                "product": "product",
                "date": "booking_date",
                "ticket": [
                    {"id": "8", "quantity": "3", "type": 2},
                    {"id": "1", "quantity": "2", "type": 1},
                ],
                "customer": "customer_name",
                "phone": "phone",
                "email": "email",
                "booking_reference": "reference",
                "remarks": "",
            },
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "call": "booking",
            },
            timeout=5,
        )

    @patch.object(requests.Session, "get")
    def test_delete(self, get_mock):
        connect_for_ut()
        get_mock.return_value.json.return_value = {"value": "test"}

        result = Booking.delete("test_booking_id")
        assert result == {"value": "test"}
        get_mock.assert_called_once_with(
            "https://test_url/q",
            params={
                "portal": "test_portal_id",
                "token": "test_token",
                "call": "cancel",
                "booking_reference": "test_booking_id",
            },
            timeout=5,
        )
