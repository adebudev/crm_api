import pytest
import datetime
from app.quotes.models.quote import Quote


@pytest.fixture
def quote_base(test_app, test_user, test_client, session):
    quote_data = [
        {
            "quote_num": 1,
            "user_id": test_user["id"],
            "client_id": test_client["id"],
            "exp_date": datetime.datetime.now(),
            "quote_status": True,
        },
        {
            "quote_num": 10,
            "user_id": test_user["id"],
            "client_id": test_client["id"],
            "exp_date": datetime.datetime.now(),
            "quote_status": False,
        }
    ]

    def create_quote_model(quote):
        return Quote(**quote)

    quote_map = map(create_quote_model, quote_data)
    quotes = list(quote_map)
    session.add_all(quotes)
    session.commit()
    quotes = session.query(Quote).all()
    return quotes
