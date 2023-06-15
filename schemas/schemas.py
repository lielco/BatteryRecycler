from enum import Enum
from pydantic import BaseModel

class PickupStatus(str, Enum):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'

class Pickup(BaseModel):
    id: str | None = None
    customer_id: str | None = None
    battery_type: str | None = None
    battery_capacity: int | None = None
    battery_age: int | None = None
    amount: int | None = None
    us_state: str | None = None
    quote: int | None = None
    status: PickupStatus | None = None

class PickupApproval(BaseModel):
    status: PickupStatus | None = None

