def test_root(test_app):
    res = test_app.get("/")
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_pong(test_app):
    res = test_app.get("/ping")
    assert res.json().get("ping") == "pong!"
    assert res.status_code == 200
