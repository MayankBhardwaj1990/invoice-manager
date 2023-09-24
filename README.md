Invoice Manager

Welcome to Invoice Manager! This project is a Django-based web application designed to manage invoices and invoice items. This README will guide you through setting up the project, activating the virtual environment, and using Postman to test the APIs.


1. Setup and Installation
Follow the appropriate steps based on your operating system.

Windows
Clone the Repository:
git clone https://github.com/MayankBhardwaj1990/invoice-manager.git
cd invoice_manager

2. Setup Virtual Environment:

Open a command prompt and navigate to the project directory.
cd path\to\your\project\directory
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

macOS and Linux
Clone the Repository:
git clone https://github.com/MayankBhardwaj1990/invoice-manager.git
cd invoice_manager

Setup Virtual Environment:

Open a terminal and navigate to the project directory.

cd /path/to/your/project/directory
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Running the Server
Run the Django development server:
python manage.py runserver

The server will start at http://127.0.0.1:8000/.

Testing with Postman
We'll be using Postman to interact with the APIs. Here are the endpoints and their respective request and response formats.

Endpoints
1. Generate Invoice:

Endpoint: http://127.0.0.1:8000/api/generate_invoice
Method: POST
Request Body: None(Hit send and an invoice would be created with a unique id with a datetime stamp)

Response structure

{
    "id": "invoice_id",
    "date": "YYYY-MM-DD"
}

2.Generate Invoice Item:

Endpoint: http://127.0.0.1:8000/api/generate_invoice_item
Method: POST
Request Body:
{
    "invoice": "invoice_id",
    "units": 5,
    "description": "Product Description",
    "amount": 100.0
}

3.Get Invoices:

Endpoint: http://127.0.0.1:8000/api/get_invoices
Method: GET
Response Structure:
[
    {
        "id": "invoice_id",
        "date": "YYYY-MM-DD"
    },
    {
        "id": "invoice_id",
        "date": "YYYY-MM-DD"
    }
]

4.Get Invoice:

Endpoint: http://127.0.0.1:8000/api/get_invoice/{invoice_id}
Method: GET
Response Structure:
{
    "id": "invoice_id",
    "date": "YYYY-MM-DD"
}

5.Get Invoice Items:

Endpoint: http://127.0.0.1:8000/api/get_invoice_items/{invoice_id}
Method: GET
Response Structure:
[
    {
        "id": "invoice_item_id",
        "invoice": "invoice_id",
        "units": 5,
        "description": "Product Description",
        "amount": 100.0
    },
    {
        "id": "invoice_item_id",
        "invoice": "invoice_id",
        "units": 2,
        "description": "Another Product",
        "amount": 50.0
    }
]


