


from requests import api
from API.booking_client import BookingAPIClient
from API.builders import make_booking


def test_put_replaces_the_whole_booking(booking_client: BookingAPIClient, created_booking):
    booking_id, payload = created_booking
    new_payload = make_booking(firstname="Big", lastname="Boss", totalprice=222)

    r = booking_client.update_booking(booking_id, new_payload)

    assert r.status_code == 200
    assert r.json() == new_payload
    assert booking_client.get_booking(booking_id).json()==new_payload

def test_update_without_token_403(api_session, created_booking):
    from API.booking_client import BookingAPIClient
    booking_id, payload = created_booking
    new_payload = make_booking(firstname="Big", lastname="Boss", totalprice=222)

    anon = BookingAPIClient(api_session)

    r = anon.update_booking(booking_id, new_payload)
    assert r.status_code == 403

def test_patch_only_last_name(booking_client: BookingAPIClient, created_booking):
    booking_id, payload = created_booking

    r = booking_client.patch_booking(booking_id, {"lastname":"Gomez"})

    actual = booking_client.get_booking(booking_id).json()

    expected = payload.copy()
    expected["lastname"] = "Gomez"

    assert actual == expected
    assert r.status_code == 200

def test_patch_without_token_is_403(api_session, created_booking):
    booking_id, payload = created_booking
    anonymous = BookingAPIClient(api_session) 

    r = anonymous.patch_booking(booking_id, make_booking())

    assert r.status_code == 403  