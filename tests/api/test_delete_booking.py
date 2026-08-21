

from API.booking_client import BookingAPIClient
from API.builders import make_booking
from tests.API.conftest import api_session


def test_deleted_booking_is_gone(booking_client: BookingAPIClient, created_booking):
    booking_id, payload  = created_booking

    r = booking_client.delete_booking(booking_id)

    assert r.status_code == 201

    assert booking_client.get_booking(booking_id).status_code == 404

def test_delete_without_token(booking_client: BookingAPIClient, api_session, created_booking):
    booking_id, payload = created_booking

    # Create a client without an authentication token
    anon = BookingAPIClient(api_session)

    # Attempt to delete the booking without authentication
    r = anon.delete_booking(booking_id)

    # Verify the server rejects the request with 403 Forbidden
    assert r.status_code == 403
    

def test_full_booking_cycle(booking_client: BookingAPIClient):
    #Create

    payload = make_booking()
    booking_id = booking_client.create_booking(payload).json()["bookingid"]

    #Read

    assert booking_client.get_booking(booking_id).json() == payload

    #Update

    new_payload = make_booking(totalprice = 999)
    r = booking_client.update_booking(booking_id, new_payload)

    assert booking_client.get_booking(booking_id).json() == new_payload

    #Delete

    r = booking_client.delete_booking(booking_id)
    assert booking_client.get_booking(booking_id).status_code == 404






