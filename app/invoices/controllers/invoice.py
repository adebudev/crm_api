from typing import List

from app.common.database import get_db
from app.invoices.models.invoices import Invoice
from app.invoices.schemas.invoices import InvoiceBase, InvoiceResponse
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/invoices", tags=["Invoices"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    invoice = db.query(Invoice).all()
    return invoice


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceBase, db: Session = Depends(get_db)):
    new_invoice = Invoice(**invoice.dict())
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice
