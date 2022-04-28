from app.invoices.schemas.invoices import InvoiceResponse


def test_get_quotes(authorized_client, invoice_base):
    res = authorized_client.get("/invoices/")

    def validate_invoice(invoice):
        return InvoiceResponse(**invoice)

    invoice_map = map(validate_invoice, res.json())
    invoices = list(invoice_map)
    assert len(res.json()) == len(invoices)
    assert res.status_code == 200


def test_post_invoices(authorized_client, test_user, test_client):
    invoice_data = {
        "invoiceNumber": 1,
        "userId": test_user["id"],
        "clientId": test_client["id"],
        "detail": "detail 1",
        "total": 1345
    }
    res = authorized_client.post("/invoices/", json=invoice_data)
    new_invoice = InvoiceResponse(**res.json())
    assert res.status_code == 201
    assert str(new_invoice.client_id) == test_client["id"]
    assert str(new_invoice.user_id) == test_user["id"]
