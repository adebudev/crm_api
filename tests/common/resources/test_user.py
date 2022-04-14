from app.common.schemas.user import UserResponse


def test_create_user(test_app):
    res = test_app.post(
        "/users/", json={"email": "johndoe@gmail.com", "password": "test"}
    )

    new_user = UserResponse(**res.json())
    assert new_user.email == "johndoe@gmail.com"
    assert res.status_code == 201
