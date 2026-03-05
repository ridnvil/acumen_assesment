from typing import List
from sqlalchemy.orm import Session # type: ignore
from fastapi import APIRouter, Depends, HTTPException
from ..core.database import get_db
from ..schemas import CustomerResponse, CustomerSchema, IngestResponse
from ..models import CustomerModel
from ..services.ingest_service import process_ingest

router = APIRouter()

@router.get("/health", response_model=dict)
def health_check():
    return {
        "message": "Server is healthy"
    }

@router.post("/ingest", response_model=IngestResponse)
def ingest_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    try:
        count = process_ingest(page, limit, db)
        return {"status": "success", "inserted": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/customers", response_model=CustomerResponse)
def read_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    customers = db.query(CustomerModel).offset(skip).limit(limit).all()
    response = CustomerResponse(
        data=customers, # type: ignore
        total=len(customers),
        page=page,
        limit=limit
    )
    return response

@router.get("/customers/{customer_id}", response_model=CustomerSchema)
def read_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


