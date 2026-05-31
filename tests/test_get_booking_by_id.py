import allure
import pytest
from services.bookings.api import BookingsAPI

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@allure.story("Получение конкретного бронирования по ID")
class TestGetBookingById:

    @allure.title("Получить бронирование по ID")
    @allure.description("Проверка GET /booking/{id} - получение полной информации о бронировании")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_booking_by_id_success(self, public_headers):
        api_client = BookingsAPI(public_headers=public_headers)

        all_bookings = api_client.get_booking_ids()
        booking_id = all_bookings.json()[0]["bookingid"]

        response = api_client.get_booking_by_id(booking_id=booking_id)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict), \
            f"Ожидался dict, получен {type(data).__name__}"

        expected_fields = [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
            "additionalneeds"
        ]
        for field in expected_fields:
            assert field in data, f"Отсутствует {field} в ответе"

        assert isinstance(data["bookingdates"], dict), \
            "bookingdates должен быть объектом"
        assert "checkin" in data["bookingdates"], "Отсутствует checkin"
        assert "checkout" in data["bookingdates"], "Отсутствует checkout"

        allure.attach(
            body=f"Бронирование ID {booking_id} получено успешно",
            name="Test Summary",
            attachment_type=allure.attachment_type.TEXT
        )