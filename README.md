# Mock Server API With Flask & Pipeline Service with FastAPI

This API build using **Flask** for handle data from JSON file and **FastAPI** for handle data with database. This prject containt list of customers, pagination, customer by id, ingest data to database, and healt check endpoint.

---

## Structure Projects

With the standart quality code python, this is the structure of the project:

```text
ACUMEN/
├── bruno_api_client/       # Koleksi API Testing (Bruno)
│
├── mock-server/            # [Flask] Data mock of customers (Mock)
│   ├── app/                # Logika utama aplikasi Flask
│   │   ├── routes/         # Definisi endpoint API
│   │   ├── __init__.py     # Factory Pattern initialization
│   │   └── utils.py        # Helper untuk membaca file JSON
│   ├── data/               
│   │   └── customers.json  # Database dummy format JSON
│   ├── .dockerignore       # File yang diabaikan oleh Docker
│   ├── Dockerfile          # Konfigurasi container Mock Server
│   ├── requirements.txt    # Library dependencies (Flask)
│   └── run.py              # Entry point aplikasi
│
├── pipeline-service/       # [FastAPI] Data provided from database and insert to database (Pipeline)
│   ├── app/                
│   │   ├── api/            # Layer Transport (Endpoint FastAPI)
│   │   │   └── endpoints.py
│   │   ├── core/           # Configuration Database & Connection
│   │   │   └── database.py
│   │   ├── services/       # Layer Bussiness Logic
│   │   ├── main.py         # Entry point & Initialize FastAPI
│   │   ├── models.py       # SQLAlchemy Models
│   │   └── schemas.py      # Pydantic Schemas (Validasi I/O)
│   ├── .dockerignore       
│   ├── Dockerfile          # Configuration container Pipeline Service
│   └── requirements.txt    # Library dependencies
│
├── .gitignore              # Ignore upload .venv, pycache on git
├── docker_compose.yml      # Run all service using compose
└── README.md               # Documentation
```

# API Documentation Mock Server

## Health Check
### Endpoint: `/api/health`
### Method: `GET`
```code
GET http://127.0.0.1:5000/api/health
```

## List Of Customers
### Endpoint: `/api/customers`
### Param: `page` and `limit`
### Method: `GET`

```code
GET http://127.0.0.1:5000/api/customers?page=1&limit=10
```
### Response: Status Code: `200 OK`
```json
{
  "data": [
    {
      "account_balance": 1500000.0,
      "address": "Jl. Merdeka No. 10, Jakarta",
      "created_at": "2023-01-15T08:30:00Z",
      "customer_id": "CUST-001",
      "date_of_birth": "1985-05-12",
      "email": "budi.santoso@email.com",
      "first_name": "Budi",
      "last_name": "Santoso",
      "phone": "+6281234567890"
    },
  ],
  "limit": 1,
  "page": 1,
  "total": 25
}
```


## Customer By ID
### Endpoint: `/api/customers/<string:id>`
### Method: `GET`
```code
GET http://127.0.0.1:5000/api/customers/CUST-001
```
### Response: Status Code: `200 OK`
```json
{
    "account_balance": 1500000.0,
    "address": "Jl. Merdeka No. 10, Jakarta",
    "created_at": "2023-01-15T08:30:00Z",
    "customer_id": "CUST-001",
    "date_of_birth": "1985-05-12",
    "email": "budi.santoso@email.com",
    "first_name": "Budi",
    "last_name": "Santoso",
    "phone": "+6281234567890"
}
```

### Response Status Code: `404`
```json
{
    "message": "Customer not found"
}
```
---

# API Documentation Pipeline Service
## Health Check
### Endpoint: `/api/health`
### Method: `GET`
```code
GET http://127.0.0.1:8000/api/health
```
### Response
```json
{
  "message": "Server is healthy"
}
```
---
## Ingest Data
### Endpoint: `/api/ingest`
### Method: `POST`
### Param: `page` and `limit` for handle pagination
### Request Body: None
### Response: Status Code: `200 OK`
```json
{
  "status": "success",
  "inserted": 15
}
```
---
## List Of Customers
### Endpoint: `/api/customers`
### Method: `GET`
### Param: `page` and `limit`
### Response Status Code: `200 OK`
```json
{
  "data": [
    {
      "customer_id": "CUST-001",
      "first_name": "Budi",
      "last_name": "Santoso",
      "email": "budi.santoso@email.com",
      "phone": "+6281234567890",
      "address": "Jl. Merdeka No. 10, Jakarta",
      "date_of_birth": "1985-05-12",
      "account_balance": 1500000.0,
      "created_at": "2023-01-15T08:30:00"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 1
}
```
---
## Customer By ID
### Endpoint: `/api/customers/<string:id>`
### Method: `GET`
### Response Status Code: `200 OK`
```json
{
  "customer_id": "CUST-001",
  "first_name": "Budi",
  "last_name": "Santoso",
  "email": "budi.santoso@email.com",
  "phone": "+6281234567890",
  "address": "Jl. Merdeka No. 10, Jakarta",
  "date_of_birth": "1985-05-12",
  "account_balance": 1500000.0,
  "created_at": "2023-01-15T08:30:00"
}
```
### Response Status Code `404`
```json
{
  "detail": "Customer not found"
}
```

---

# Deploy
For deploy using docker compose with command:
```bash
docker-compose up
```