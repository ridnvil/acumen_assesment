from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional

class CustomerSchema(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    date_of_birth: Optional[date] = None
    account_balance: float
    created_at: datetime

    # Tambahkan ini agar Pydantic bisa membaca data dari objek SQLAlchemy
    class Config:
        from_attributes = True

class CustomerResponse(BaseModel):
    data: List[CustomerSchema]
    total: int
    page: int
    limit: int

    class Config:
        from_attributes = True

class IngestResponse(BaseModel):
    status: str
    inserted: int

