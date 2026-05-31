import pytest
import allure
import os
from dotenv import load_dotenv
from clients.auth_clients import AuthClients
load_dotenv()

@pytest.fixture(scope="session")
def auth_token():
    with allure.step("Авторизация: проверка токена"):
        token = os.getenv("TOKEN")

        if not token:
            allure.attach(
                body="Токен отсутствует в .env. Получаем новый...",
                name="Статус токена",
                attachment_type=allure.attachment_type.TEXT
            )

            with allure.step("Запрос токена через API /auth"):
                client = AuthClients()
                token = client.create_token()

            with allure.step("Сохранение токена в .env"):
                with open(".env", "w", encoding="utf-8") as f:
                    f.write(f"TOKEN={token}\n")

                os.environ["TOKEN"] = token

            allure.attach(
                body=f"Новый токен получен и сохранён:\n{token}",
                name="Токен авторизации",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                body=f"Используем существующий токен:\n{token}",
                name="Токен авторизации",
                attachment_type=allure.attachment_type.TEXT
            )

        return token

@pytest.fixture(scope="session")
def authorized_headers(auth_token):
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": f"token='{auth_token}'",
        "Authorization": "Basic"
    }

@pytest.fixture(scope="session")
def public_headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"