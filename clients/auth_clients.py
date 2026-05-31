import requests
from services.bookings.endpoints import Endpoints

class AuthClients:
    def __init__(self):
        self.base_url = Endpoints.BASE_URL

    def create_token(self, username: str = "admin", password: str = "password123") -> str:
        url = f"{self.base_url}{Endpoints.auth_url}"
        payload = {
            "username": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        token = response.json().get("token")
        return token