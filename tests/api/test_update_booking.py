from requests import api

from API.booking_client import BookingAPIClient
from API.builders import make_booking


def test_put_replaces_the_whole_booking(
    booking_client: BookingAPIClient, created_booking
):
    # Get the booking ID and original booking data from the fixture
    booking_id, payload = created_booking

    # Create completely new booking data
    new_payload = make_booking(
        firstname="Big",
        lastname="Boss",
        totalprice=222
    )

    # Send a PUT request to replace the entire existing booking
    r = booking_client.update_booking(booking_id, new_payload)

    # Verify the PUT request was successful
    assert r.status_code == 200

    # Verify the response contains the new booking data
    assert r.json() == new_payload

    # GET the booking again and verify the saved booking matches the new data
    assert booking_client.get_booking(booking_id).json() == new_payload


def test_update_without_token_403(api_session, created_booking):
    # Get the booking ID and original booking data
    booking_id, payload = created_booking

    # Create new booking data for the update
    new_payload = make_booking(
        firstname="Big",
        lastname="Boss",
        totalprice=222
    )

    # Create a client without an authentication token
    anon = BookingAPIClient(api_session)

    # Attempt to update the booking without authentication
    r = anon.update_booking(booking_id, new_payload)

    # Verify the server rejects the request with 403 Forbidden
    assert r.status_code == 403


def test_patch_only_last_name(
    booking_client: BookingAPIClient, created_booking
):
    # Get the booking ID and original booking data
    booking_id, payload = created_booking

    # PATCH only the lastname field
    r = booking_client.patch_booking(
        booking_id,
        {"lastname": "Gomez"}
    )

    # GET the booking after the PATCH to see what is actually stored
    actual = booking_client.get_booking(booking_id).json()

    # Copy the original booking so we don't modify the original payload
    expected = payload.copy()

    # Change ONLY the lastname in our expected result
    expected["lastname"] = "Gomez"

    # Verify lastname changed AND every other field stayed the same
    assert actual == expected

    # Verify the PATCH request was successful
    assert r.status_code == 200


def test_patch_without_token_is_403(api_session, created_booking):
    # Get the booking ID and original booking data
    booking_id, payload = created_booking

    # Create a client without an authentication token
    anonymous = BookingAPIClient(api_session)

    # Attempt to PATCH the booking without authentication
    r = anonymous.patch_booking(
        booking_id,
        make_booking()
    )

    # Verify the server rejects the request with 403 Forbidden
    assert r.status_code == 403