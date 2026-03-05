from flask import Blueprint, jsonify, request
from app.utils import get_customers_from_json

main_bp = Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    return "Server is healty"

@main_bp.route('/customers', methods=['GET'])
def list_customers():
    customers = get_customers_from_json()
    
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return jsonify({"error": "Parameter must numbers"}), 400
    
    start = (page - 1) * limit
    end = start + limit

    paginated_data = customers[start:end]
    response = {
        "data": paginated_data,
        "total": len(customers),
        "page": page,
        "limit": limit 
    }
    return jsonify(response)

@main_bp.route('/customers/<string:id>', methods=['GET'])
def get_customer(id):
    customers = get_customers_from_json()
    customer = next((customer for customer in customers if customer['customer_id'] == id), None)
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"message": "Customer not found"}), 404