import json
from datetime import date
from ..travelmanager_api import TravelManagerAPI


class Ticket:
    id = ""
    quantity = ""
    caption = ""
    price = 0.0
    currency = ""
    vatrate = 0

    def __init__(self, id, quantity, caption, price, currency, vatrate) -> None:
        self.id = id
        self.quantity = quantity
        self.caption = caption
        self.price = price
        self.currency = currency
        self.vatrate = vatrate


class Booking:
    @staticmethod
    def create(
        product: str,
        date: date,
        ticket: Ticket,
        customer_name: str,
        phone: str,
        email: str,
        reference: str,
        remarks: str = "",
    ) -> dict:
        data = {
            "product": product,
            "date": date,
            "ticket": [json.dumps(ticket)],
            "customer": customer_name,
            "phone": phone,
            "email": email,
            "booking_reference": reference,
            "remarks": remarks,
        }
        return TravelManagerAPI.post("booking", data)

    @staticmethod
    def delete(booking_id: str) -> dict:
        param = {
            "booking_reference": booking_id,
        }
        return TravelManagerAPI.delete("cancel", param)


"""
{
    booking_reference: "28711",
    qrcode: "XQPfykGViICSVg56cJRibjdmbZ/O5rTFz2AWSx42Dmnq0C3YBSG8lKr0z1Pb6vDymrWAaXbEbUJLH581W6me3Q==",
    onlineticket: "https://buchung.reederei-peters.de/?unique_id=a646e68dab310d20881"
}


{
    errorCode: "NO_AVAILABILITY",
    errorMessage: "Zu dem angegebenen Datum finden keine Fahrten statt"
}


{
    success: true
}

"""
