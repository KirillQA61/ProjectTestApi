import allure
import pytest
from services.bookings.api import BookingsAPI

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@allure.story("Получение списка бронирований")
class TestGetBookingIDs:

    @allure.title("Получить список всех бронирований")
    @allure.description("Проверка GET /booking без параметров фильтрации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_booking_ids_success(self, public_headers):
        api_client = BookingsAPI(public_headers=public_headers)

        response = api_client.get_booking_ids()
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"


        data = response.json()
        assert isinstance(data, list), f"Ожидался список, получен {type(data).__name__}"

        if len(data) > 0:
            first_item = data[0]
            assert "bookingid" in first_item, "Ответ должен содержать ключ 'bookingid'"
            assert isinstance(first_item["bookingid"], int), "bookingid должен быть целым числом"