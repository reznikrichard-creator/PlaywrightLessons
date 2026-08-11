from socket import timeout
import requests
# {
#     "username": "asdsds"
# }
BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_token():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        timeout=10,
    )
    # print("Status Code:", response.status_code)

    assert response.status_code == 200
    assert response.json()["token"]
    
def test_ping():
    response = requests.get(
        f"{BASE_URL}/ping",
        timeout=10,
    )

    assert response.status_code == 201
    #201 is a bug.200 is excpected
    