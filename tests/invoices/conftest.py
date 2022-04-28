import pytest
from app.invoices.models.invoices import Invoice


@pytest.fixture
def invoice_base(test_app, test_user, test_client, session):
    invoice_date = [
        {
            "invoice_num": 1,
            "user_id": test_user["id"],
            "client_id": test_client["id"],
            "detail": "test detail 1",
            "total": 10.5,
        },
        {
            "invoice_num": 10,
            "user_id": test_user["id"],
            "client_id": test_client["id"],
            "detail": "test detail 2",
            "total": 13.4,
        }
    ]

    def create_invoice_model(invoice):
        return Invoice(**invoice)

    invoice_map = map(create_invoice_model, invoice_date)
    invoices = list(invoice_map)
    session.add_all(invoices)
    session.commit()
    invoices = session.query(Invoice).all()
    return invoices
