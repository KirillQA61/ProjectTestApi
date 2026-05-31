import allure
import requests
from services.bookings.payloads import Payload
from services.bookings.endpoints import Endpoints

class BookingsAPI:

    def __init__(self, public_headers: dict = None, authorized_headers: dict = None):
        self.payloads = Payload()
        self.public_headers = public_headers or {}
        self.authorized_headers = authorized_headers or {}
        self.endpoints = Endpoints()

    @allure.step("Get Booking IDs")
    def get_booking_ids(self, firstname: str = None, lastname: str = None,
                        checkin: str = None, checkout: str = None):
        params = {}
        if firstname:
            params["firstname"] = firstname
        if lastname:
            params["lastname"] = lastname
        if checkin:
            params["checkin"] = checkin
        if checkout:
            params["checkout"] = checkout

        allure.attach(
            body=f"URL: {self.endpoints.BASE_URL}{self.endpoints.bookings_url}\nParams: {params}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        response = requests.get(
            url=f"{self.endpoints.BASE_URL}{self.endpoints.bookings_url}",
            params=params,
            headers = self.public_headers
        )

        allure.attach(
            body=f"Status: {response.status_code}\nBody: {response.text}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

        return response

    @allure.step("Get Booking")
    def get_booking_by_id(self, booking_id: int):
        url = f"{self.endpoints.BASE_URL}{self.endpoints.booking_by_id_url}{booking_id}"

        allure.attach(
            body=f"URL: {url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        response = requests.get(
            url=url,
            headers=self.public_headers
        )

        allure.attach(
            body=f"Status: {response.status_code}\nBody: {response.text}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

        return response

    @allure.step("Сreate Booking")
    def create_booking(self):
        response = requests.post(
            ...
        )

    @allure.step("Update Booking")
    def update_booking(self):
        response = requests.put(
            ...
        )

    @allure.step("Partial Update Booking")
    def partial_update_booking(self):
        response = requests.patch(
            ...
        )

    @allure.step("Delete Booking")
    def delete_booking(self):
        response = requests.delete(
            ...
        )