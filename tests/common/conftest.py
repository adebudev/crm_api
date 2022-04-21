import pytest


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
