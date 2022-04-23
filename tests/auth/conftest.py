import pytest


@pytest.fixture
def test_user_auth(test_app):
    user_data = {"email": "jhondoe@gmail.com", "password": "test"}
    res = test_app.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user
