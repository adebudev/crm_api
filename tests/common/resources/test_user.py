from app.common.schemas.user import UserResponse


def test_create_user(test_app):
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
    res = test_app.post(
        "/users/", json=user_data
    )

    new_user = UserResponse(**res.json())
    assert new_user.email == "jhondoe@gmail.com"
    assert res.status_code == 201
