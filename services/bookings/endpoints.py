
class Endpoints:
    BASE_URL="https://restful-booker.herokuapp.com"

    bookings_url = "/booking"       # GET /booking, POST /booking
    booking_by_id_url = "/booking/" # GET /booking/{id}, PUT, PATCH, DELETE
    auth_url = "/auth"              # POST /auth