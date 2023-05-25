from dotenv import dotenv_values
from travelmanager.travelmanager_api import TravelManagerAPI


def connect_for_ut():
    TravelManagerAPI.connect("test_url", "test_portal_id", "test_token")


def connect_for_it():
    config = dotenv_values(".env")
    TravelManagerAPI.connect(
        config["URL"],
        config["PORTAL_ID"],
        config["TOKEN"],
    )
