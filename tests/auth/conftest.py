import pytest


@pytest.fixture
def test_user_auth(test_app):
    user_data = {
        "firstName": "jhon",
        "lastName": "Doe",
        "email": "jhondoe@gmail.com",
        "password": "test",
        "phone": "3008002843",
        "address": "1800 avenue",
        "country": "COL",
        "city": "bar"
    }
    res = test_app.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user
