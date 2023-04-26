import requests
import json

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = "Your token"

# POST Create User


def create_user():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "John",
        "email": "joe33@test.pl",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(
        f"{BASE_URL}/users", headers=headers, data=json.dumps(payload))
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    user_id = response.json()["id"]
    return user_id

# GET Single User


def get_single_user(user_id):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
    }
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_data = response.json()
    return user_data


if __name__ == "__main__":
    created_user_id = create_user()
    print(get_single_user(created_user_id))
