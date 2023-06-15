# BatteryRecycler

Test project for learning purposes.

Basic web server using FastAPI and Python3.11.

## Usage

- '/api/customer/{customer_id}/pickup/{pickup_id}', methods=['GET'], unauthenticated
- '/api/customer/{customer_id}/pickup", methods=['POST'], unauthenticated
- '/api/customer/{customer_id}/pickup/{pickup_id}/approval', methods=['PATCH'], unauthenticated
- '/admin/rules', methods=['GET', 'PUT'], unauthenticated

## Instructions to run the server

- pip install -r requirements.txt
- uvicorn app:app --host 0.0.0.0 --port 8000

## Instructions to run the demo

- py ./demo/run_demo.py

The demo uses a rule file located at the demo folder.

Please use that schema if you'd like to use a custom rule file.

You can also access the SwaggerUI using http://127.0.0.1:8000/docs
