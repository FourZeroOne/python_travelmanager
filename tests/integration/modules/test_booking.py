import requests
from tests.utils import connect_for_it

from travelmanager import Booking
from travelmanager.schemas import Ticket


class TestBooking:
    def test_create(self):
        connect_for_it()

        result = Booking.create(
            "[[25,26,1,5]]",
            "2023-09-22",
            [Ticket("8", "2"), Ticket("1", "2")],
            "Test1 Test2",
            "0171/12345678",
            "test@jep-dev.com",
            "#TEST12345678",
        )
        print(result)
        assert result["booking_reference"] != ""

        result = Booking.delete(result["booking_reference"] )
        assert result == {'success': True}

    def test_create_with_accessoirs(self):
        connect_for_it()

        result = Booking.create(
            "[[25,26,1,5]]",
            "2023-09-22",
            [Ticket("8", "2", 2), Ticket("1", "2")],
            "Test1 Test2",
            "0171/12345678",
            "test@jep-dev.com",
            "#TEST12345678",
        )

        print(result)
        assert result["booking_reference"] != ""

        result = Booking.delete(result["booking_reference"] )
        assert result == {'success': True}


