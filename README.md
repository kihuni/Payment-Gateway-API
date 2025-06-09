# 💳 Payment Gateway API for Small Businesses

A simple, RESTful API that allows small businesses to accept payments via PayPal. Built with Django REST Framework.

## 🚀 Features

✅ Accept payments with minimal customer data: name, email, amount

✅ Integration with PayPal 

✅ Versioned RESTful API (/api/v1/)

✅ No user authentication required

✅ Clear payment status responses

✅ CI/CD with GitHub Actions

✅ Fully tested using Django’s test framework

## Tech Stack

- Backend: Django, Django REST Framework

- Payment Gateway: PayPal SDK 

- CI/CD: GitHub Actions

## API Endpoints

1. Initiate a Payment
Endpoint:
`POST /api/v1/payments/`

Request Body:

```
{
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "amount": 50.00
}
```

response:

```
{
  "status": "success",
  "message": "Payment initiated successfully.",
  "payment_id": "PAY-123"
}

```
![image](https://github.com/user-attachments/assets/664a34e0-fc68-4c7f-acf7-bc14d6abc65f)


2. Retrieve Payment Status
   
Endpoint:
`GET /api/v1/payments/<payment_id>/`

Response:

```
{
  "payment": {
    "id": "PAY-123",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "amount": 50.00,
    "status": "completed"
  },
  "status": "success",
  "message": "Payment details retrieved successfully."
}

```
![image](https://github.com/user-attachments/assets/17bbb3ff-8b0c-4f69-bbf5-c029a4d4b646)


##  Running the Service Locally

1. Clone the repository

```
git clone https://github.com/kihuni/Payment-Gateway-API.git
cd Payment-Gateway-API
```
2. Create and activate a virtual environment
   
```
python -m venv env
source env/bin/activate  

On Windows:
env\Scripts\activate

```

3. Install dependencies

```
pip install -r requirements.txt

```

4. Add environment variables
   
Create a .env file:

```
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret

```
5. Run migrations and start the server

```
python manage.py migrate
python manage.py runserver

```

## ✅ Running Tests

Run the full test suite:
```
python manage.py test

```

These tests cover:

- Successful payment initiation

- Invalid payloads

- Payment status retrieval


##  CI/CD with GitHub Actions

Workflow File: .github/workflows/django.yml

```
name: Django CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    env:
      SECRET_KEY: ${{ secrets.SECRET_KEY }}
      PAYPAL_CLIENT_ID: ${{ secrets.PAYPAL_CLIENT_ID }}
      PAYPAL_CLIENT_SECRET: ${{ secrets.PAYPAL_CLIENT_SECRET }}

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python '3.10'
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        python manage.py test

```

## Deployment

To deploy on services like Render, Railway, or Heroku:

1. Push your code to GitHub.

2. Connect the GitHub repo to the hosting platform.

3. Set environment variables on the platform:

- PAYPAL_CLIENT_ID

- PAYPAL_CLIENT_SECRET

- SECRET_KEY

4. Make sure your requirements.txt are set correctly.
