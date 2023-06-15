from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Form, HTTPException, status as status_
from quote_manager import QuoteManager
from rules import Rules
from schemas.schemas import Pickup, PickupApproval, PickupStatus, QuoteResponse

pickups = {}
router = APIRouter()
rules = Rules()

@router.get("/api/customer/{customer_id}/pickup/{pickup_id}", response_model=Pickup)
def get_pickup_details(customer_id: str, pickup_id: str):
    """
    This endpoint gets pickup_id and return the relevant pickup details
    """
    
    pickup = pickups.get(pickup_id)
    if not pickup:
        print(f"Entity {pickup_id} not found")
        raise HTTPException(status_code=status_.HTTP_404_NOT_FOUND, 
                            detail=f"Entity {pickup_id} not found")
    return pickups.get(pickup_id)

@router.post("/api/customer/{customer_id}/pickup", response_model=QuoteResponse)
def generate_pickup_quote(customer_id, 
                          battery_capacity: Annotated[int, Form(ge=1, description="The battery's capacity in mAH")], 
                          battery_age: Annotated[int, Form(ge=1, description="The battery's age in years")],
                          battery_type: Annotated[str, Form(description="Type of the battery")],
                          amount: Annotated[int, Form(ge=1, description="The amount of batteries that you have")],
                          us_state: Annotated[str, Form(max_length=2, min_length=2, 
                                                        description="The state you are located in in two letter abbreviation",
                                                        example="NY")]):
    id = uuid4().hex
    quote_manager = QuoteManager()
    pickup = Pickup(id=id, 
                    customer_id=customer_id, 
                    battery_type=battery_type, 
                    battery_capacity=battery_capacity, 
                    battery_age=battery_age,
                    amount=amount,
                    us_state=us_state,
                    status=PickupStatus.PENDING)
    quote = quote_manager.calculate_quote(pickup)
    pickup.quote = quote
    pickups[id] = pickup
     
    return QuoteResponse(pickup_id=id, quote=quote)

@router.patch("/api/customer/{customer_id}/pickup/{pickup_id}/approval", response_model=Pickup)
def approve_pickup(customer_id: str, pickup_id: str, pickup_approval: PickupApproval):
    pickup = pickups.get(pickup_id)
    if not pickup:
        print(f"Entity {pickup_id} not found")
        raise HTTPException(status_code=status_.HTTP_404_NOT_FOUND, 
                            detail=f"Entity {pickup_id} not found")

    update_data = pickup_approval.dict(exclude_unset=True)
    updated_item = pickup.copy(update=update_data)
    pickups[pickup_id] = updated_item
    return updated_item