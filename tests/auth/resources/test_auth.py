import pytest
from app.auth.schemas.user import LoginResponse
from app.common.config import settings
from jose import jwt


def test_log_in(test_app, test_user_auth):
    res = test_app.post(
        "/login",
        json={"email": test_user_auth["email"], "password": test_user_auth["password"]},
    )

    login_res = LoginResponse(**res.json())
    cookie = res.cookies.get("access_token")
    payload = jwt.decode(cookie, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == str(test_user_auth["id"])
    assert login_res.token_type == "Bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "test", 401),
        ("johndoe@gmail.com", "wrongpassword", 401),
        ("wrongemail@gmail.com", "wrongpassword", 401),
        (None, "test", 422),
        ("johndoe@gmail.com", None, 422),
    ],
)
def test_incorrect_login(test_app, test_user_auth, email, password, status_code):
    res = test_app.post("/login", json={"email": email, "password": password})
    assert res.status_code == status_code
