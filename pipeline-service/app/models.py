from sqlalchemy import Column, String, Float, DateTime # type: ignore
from .core.database import Base
import datetime
from sqlalchemy import Date # type: ignore

class CustomerModel(Base):
    __tablename__ = 'customers'

    customer_id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    address = Column(String)
    date_of_birth = Column(Date) # Bisa gunakan Date type jika formatnya sesuai
    account_balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)