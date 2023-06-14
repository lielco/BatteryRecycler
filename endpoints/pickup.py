from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Form
from rules import Rules

pickup = {}

router = APIRouter()

@router.get("/api/customer/{customer_id}/pickup/{pickup_id}")
def get_pickup_details(customer_id: str, pickup_id: str):
    return pickup.get(pickup_id)

@router.post("/api/customer/{customer_id}/pickup")
def generate_pickup_quote(customer_id, 
                          battery_capacity: Annotated[int, Form()], 
                          battery_age: Annotated[int, Form()],
                          battery_type: Annotated[str, Form()],
                          amount: Annotated[int, Form()],
                          state: Annotated[str, Form()]):
    id = uuid4().hex
    qoute = calculate_quote(battery_capacity, battery_age, battery_type, amount, state)
    pickup[id] = {
        "pickup_id": id,
        "customer_id": customer_id,
        "battery_capacity": battery_capacity,
        "battery_age": battery_age,
        "battery_type": battery_type,
        "amount" : amount,
        "state": state,
        "quote": qoute
    }

    return { "pickup_id": id, "quote": qoute }

def calculate_quote(battery_capacity: int, battery_age: int, battery_type: str, amount: int,  zipcode: str):
    rules = Rules.get_rules()