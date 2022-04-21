from app.common.schemas.client import ClientResponse

def test_client_endpoint(test_app, test_user):
    client_data = {
        "name": "client_1",
        "address": "calle 10",
        "city": "Barranquilla",
        "country": "Colombia",
        "goverment_id": "1234567",
        "user_id": test_user["id"]
    }
    res = test_app.post("/client/", json=client_data)

    new_client = ClientResponse(**res.json())
    assert new_client.name == "client_1"
    assert new_client.city == "Barranquilla"
    assert res.status_code == 201
