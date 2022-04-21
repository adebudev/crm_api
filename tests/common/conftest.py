import pytest

# TODO: add to general conftest
@pytest.fixture
def test_user(test_app):
    user_data = {"email": "jhondoe@gmail.com", "password": "test"}
    res = test_app.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def test_client(test_app, test_user):
    client_data = {
        "name": "client_1",
        "address": "calle 10",
        "city": "Barranquilla",
        "country": "Colombia",
        "goverment_id": "1234567",
        "user_id": test_user["id"]
    }
    res = test_app.post("/clients/", json=client_data)
    assert res.status_code == 201
    new_client = res.json()
    return new_client
