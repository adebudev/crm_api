import datetime
import uuid

import pytest
from app.quotes.schemas.quote_dto import QuoteResponse, QuoteResponses

# TODO: protect routes


def test_get_quotes(quote_base, test_app):
    res = test_app.get("/quotes/")

    def validate_quote(quote):
        return QuoteResponses(**quote)

    quote_map = map(validate_quote, res.json())
    quotes = list(quote_map)
    assert len(res.json()) == len(quotes)
    assert res.status_code == 200


def test_post_quotes(test_app, test_user, test_client):
    quote_data = {
        "quote": {
            "quote_num": 100,
            "exp_date": str(datetime.datetime.now()),
            "quote_status": True,
            "user_id": test_user["id"],
            "client_id": test_client["id"],
        },
        "detail": {
            "valid_time": 120,
            "deliver_time": str(datetime.datetime.now()),
            "currency_type": "COP",
            "payment_terms": "Monthly",
            "sub_total": 13.5,
            "total": 20.5,
        },
        "item": [
            {
                "name": "item test 1",
                "description": "item test description",
                "quantity": 10,
                "unit_value": 16,
            },
            {
                "name": "item test 2",
                "description": "item test description 2",
                "quantity": 11,
                "unit_value": 15.5,
            },
        ],
        "taxes": [{"tax_name": "iva", "tax_value": 20.3}],
        "comment": {"comment": "comment test 1"},
    }
    res = test_app.post("/quotes/", json=quote_data)

    created_quote = QuoteResponse(**res.json())
    assert res.status_code == 201
    assert str(created_quote.client_id) == test_client["id"]
    assert str(created_quote.user_id) == test_user["id"]


def test_put_quotes(test_app, test_user, test_client, quote_base):
    data = {
        "id": str(quote_base[1].id),
        "quote_num": 5,
        "user_id": test_user["id"],
        "client_id": test_client["id"],
        "exp_date": str(datetime.datetime.now()),
        "quote_status": True,
    }
    res = test_app.put(f"/quotes/{quote_base[1].id}", json=data)
    updated_quote = QuoteResponse(**res.json())
    assert res.status_code == 200
    assert updated_quote.quote_num == 5
    assert updated_quote.quote_status == True


def test_delete_quotes(test_app, quote_base):
    res = test_app.delete(f"/quotes/{quote_base[1].id}")
    assert res.status_code == 200


def test_delete_quotes_with_no_id(test_app, quote_base):
    res = test_app.delete(f"/quotes/{uuid.uuid4()}")
    assert res.status_code == 404
