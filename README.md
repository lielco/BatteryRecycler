# BatteryRecycler

Test project for learning purposes.

Basic web server using FastAPI and Python3.11.

## Usage

- '/api/customer/{customer_id}/pickup/{pickup_id}', methods=['GET'], unauthenticated
- '/api/customer/{customer_id}/pickup", methods=['POST'], unauthenticated
- '/api/customer/{customer_id}/pickup/{pickup_id}/approval', methods=['PATCH'], unauthenticated
- '/admin/rules', methods=['GET', 'PUT'], unauthenticated

## Instructions

- pip install -r requirements.txt
- uvicorn app:app --host 0.0.0.0 --port 8000
- py ./demo/run_demo.py
