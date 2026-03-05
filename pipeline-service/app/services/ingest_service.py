import requests # type: ignore
from sqlalchemy.orm import Session # type: ignore
from ..models import CustomerModel

def process_ingest(page: int, limit: int, db: Session):
    FLASK_API = "http://localhost:5000/api/customers?page={}&limit={}".format(page, limit)    

    response = requests.get(FLASK_API)
    response.raise_for_status()
    customer_list = response.json().get("data", [])

    count = 0
    for customer in customer_list:
        existing = db.query(CustomerModel).filter(CustomerModel.customer_id == customer["customer_id"]).first()
        if not existing:
            new_customer = CustomerModel(**customer)
            db.add(new_customer)
            count += 1

    db.commit()
    return count