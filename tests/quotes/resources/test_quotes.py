import datetime
import uuid

from app.quotes.schemas.quote_dto import QuoteResponse, QuoteResponses


def test_get_quotes(authorized_client, quote_base):
    res = authorized_client.get("/quotes/")

    def validate_quote(quote):
        return QuoteResponses(**quote)

    quote_map = map(validate_quote, res.json())
    quotes = list(quote_map)
    assert len(res.json()) == len(quotes)
    assert res.status_code == 200


def test_post_quotes(authorized_client, test_user, test_client):
    quote_data = {
        "quote": {
            "quoteNumber": 100,
            "expirationDate": str(datetime.datetime.now()),
            "quoteStatus": True,
            "userId": test_user["id"],
            "clientId": test_client["id"],
        },
        "detail": {
            "validTime": 120,
            "deliverTime": str(datetime.datetime.now()),
            "currencyType": "COP",
            "paymentTerms": "Monthly",
            "subTotal": 13.5,
            "total": 20.5,
        },
        "item": [
            {
                "name": "item test 1",
                "description": "item test description",
                "quantity": 10,
                "unitValue": 16,
            },
            {
                "name": "item test 2",
                "description": "item test description 2",
                "quantity": 11,
                "unitValue": 15.5,
            },
        ],
        "taxes": [{"taxName": "iva", "taxValue": 20.3}],
        "comment": {"comment": "comment test 1"},
    }
    res = authorized_client.post("/quotes/", json=quote_data)

    created_quote = QuoteResponse(**res.json())
    assert res.status_code == 201
    assert str(created_quote.client_id) == test_client["id"]
    assert str(created_quote.user_id) == test_user["id"]


def test_put_quotes(authorized_client, test_user, test_client, quote_base):
    data = {
        "id": str(quote_base[1].id),
        "quoteNumber": 5,
        "userId": test_user["id"],
        "clientId": test_client["id"],
        "expirationDate": str(datetime.datetime.now()),
        "quoteStatus": True,
    }
    res = authorized_client.put(f"/quotes/{quote_base[1].id}", json=data)
    updated_quote = QuoteResponse(**res.json())
    assert res.status_code == 200
    assert updated_quote.quote_num == 5
    assert updated_quote.quote_status == True


def test_delete_quotes(authorized_client, quote_base):
    res = authorized_client.delete(f"/quotes/{quote_base[1].id}")
    assert res.status_code == 200


def test_delete_quotes_with_no_id(authorized_client, quote_base):
    res = authorized_client.delete(f"/quotes/{uuid.uuid4()}")
    assert res.status_code == 404
