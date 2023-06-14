from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Form
from rules import Rules

pickup = {}
router = APIRouter()
rules = Rules()

@router.get("/api/customer/{customer_id}/pickup/{pickup_id}")
def get_pickup_details(customer_id: str, pickup_id: str):
    return pickup.get(pickup_id)

@router.post("/api/customer/{customer_id}/pickup")
def generate_pickup_quote(customer_id, 
                          battery_capacity: Annotated[int, Form()], 
                          battery_age: Annotated[int, Form()],
                          battery_type: Annotated[str, Form()],
                          amount: Annotated[int, Form()],
                          us_state: Annotated[str, Form()]):
    id = uuid4().hex
    qoute = calculate_quote(battery_capacity, battery_age, battery_type, amount, us_state)
    pickup[id] = {
        "pickup_id": id,
        "customer_id": customer_id,
        "battery_capacity": battery_capacity,
        "battery_age": battery_age,
        "battery_type": battery_type,
        "amount" : amount,
        "us_state": us_state,
        "quote": qoute
    }

    return { "pickup_id": id, "quote": qoute }

def calculate_quote(battery_capacity: int, battery_age: int, battery_type: str, amount: int,  us_state: str):
    quote = 0
    rule_list = rules.get_rules()
    prices_by_type = rule_list.get("base_price").get(battery_type, [])
    price_for_capacity = next((price for price in prices_by_type if price["capacity"] == battery_capacity), None)
    if price_for_capacity:
        base_price = price_for_capacity["price"]
        bulk_incentive = base_price * rule_list.get("bulk").get("price_factor") - base_price if amount > rule_list.get("bulk").get("minimum_amount") else 0
        quote = base_price - (battery_age * rule_list.get("age_yearly_reduction")) * (rule_list.get("distances").get(us_state)) + bulk_incentive
    else:
        print(f"Could not calculate quote for battery type {battery_type} with capacity of {battery_capacity}")

    return quote