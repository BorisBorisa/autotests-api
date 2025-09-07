import httpx

login_payload = {
    "email": "users@example.com",
    "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response_data["token"])
print(login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
me_response_data = me_response.json()

print(me_response_data)
print(me_response.status_code)
