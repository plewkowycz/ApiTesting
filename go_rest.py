import requests
import json

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = "5c56f8de35eb391f48199278529c82be7cdaa14f89fb66ad58abfa9eeb656ef0"

# POST Create User


def create_user():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "John",
        "email": "john3@test.pl",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(
        f"{BASE_URL}/users", headers=headers, data=json.dumps(payload))
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    user_id = response.json()["data"]["id"]
    return user_id

# GET Single User


def get_single_user(user_id):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
    }
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_data = response.json()["data"]
    return user_data

# Update user email


def update_user_email(user_id, new_email):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "email": new_email
    }
    response = requests.put(
        f"{BASE_URL}/users/{user_id}", headers=headers, data=json.dumps(payload))
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_data = response.json()["data"]
    return user_data

# GET All Users and verify if specific exist with updated email


def get_all_users_and_verify_email(user_id, expected_email):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
    }
    response = requests.get(f"{BASE_URL}/users", headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    users = response.json()["data"]

    found_user = None
    for user in users:
        if user["id"] == user_id:
            found_user = user
            break

    assert found_user is not None, f"User with id {user_id} not found"
    assert found_user["email"] == expected_email, f"Expected email {expected_email}, but got {found_user['email']}"

# Remove single user


def remove_single_user(user_id):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
    }
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

# Verify single user does not exist


def verify_user_does_not_exist(user_id):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
    }
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"


if __name__ == "__main__":
    created
