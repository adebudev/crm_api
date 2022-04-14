import json

import pytest
from app.auth.schemas.token import Token
from app.common.config import settings
from jose import jwt


def test_log_in(test_app, test_user):
    res = test_app.post(
        "/login", json={"email": test_user["email"], "password": test_user["password"]}
    )

    login_res = Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert id == json.dumps(str(test_user["id"]))
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
def test_incorrect_login(test_app, test_user, email, password, status_code):
    res = test_app.post("/login", json={"email": email, "password": password})
    assert res.status_code == status_code
