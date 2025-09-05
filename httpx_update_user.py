import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response.status_code)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)

update_user_payload = {
    "email": fake.email(),
    "lastName": "Olegov",
    "firstName": "Oleg",
    "middleName": "Oleg"
}
user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=user_headers,
    json=update_user_payload
)

print(update_response.json())
print(update_response.status_code)
