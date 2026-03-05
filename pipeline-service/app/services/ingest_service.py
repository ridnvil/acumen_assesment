import requests # type: ignore
from sqlalchemy.orm import Session # type: ignore
from ..models import CustomerModel
from ..core.config import MOCK_SERVER_URL

if MOCK_SERVER_URL is None:
    raise ValueError("MOCK_SERVER_URL is not set")


def process_ingest(page: int, limit: int, db: Session):
    FLASK_API = "{}/customers?page={}&limit={}".format(MOCK_SERVER_URL, page, limit)    

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