from app.common.schemas.client import ClientResponse

# TODO: protect routes


def test_client_endpoint(test_app, test_user):
    client_data = {
        "name": "client_1",
        "address": "calle 10",
        "city": "Barranquilla",
        "country": "Colombia",
        "govermentId": "1234567",
        "userId": test_user["id"],
    }
    res = test_app.post("/client/", json=client_data)

    new_client = ClientResponse(**res.json())
    assert new_client.name == "client_1"
    assert new_client.city == "Barranquilla"
    assert res.status_code == 201
