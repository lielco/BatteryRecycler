from math import floor

from fastapi import HTTPException, status
from rules import Rules
from schemas.schemas import Pickup

class QuoteManager:
    """ A class to manage quote calculation """
    def calculate_quote(self, pickup: Pickup):
        """ Calculates price quote for the given pickup based on the
        active rule list.
                
        :param pickup: The pickup response
        :type pickup: Pickup
        """
        rules = Rules()
        quote = 0
        rule_list = rules.get_rules()
        prices_by_type = rule_list.get("base_price", {}).get(pickup.battery_type, [])
        base_price = None
        for pricing in prices_by_type:
            if pricing.get("capacity") == pickup.battery_capacity:
                base_price = pricing.get("price")
                break
        
        if base_price:
            # Bulk incentive factor applies only when minimum amount is reached 
            # For example if price factor is 1.1 and amount > minimum, 10% is added to the base price
            if pickup.amount > rule_list.get("bulk").get("minimum_amount"):
                bulk_incentive = rule_list.get("bulk").get("price_factor")
            else:
                bulk_incentive = 1

            # For each year we reduce the price by the age_yearly_reduction value
            age_value_reduction = pickup.battery_age * rule_list.get("age_yearly_reduction")

            # The further away from Nevada, the lower the cost paid to the customer
            distance_factor_reduction = rule_list.get("distances").get(pickup.us_state) or 1
 
            quote = max((base_price * bulk_incentive - age_value_reduction) * distance_factor_reduction, 0)
        else:
            error_message = f"Could not calculate quote for battery type {pickup.battery_type} with capacity of {pickup.battery_capacity}"
            print(error_message)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail=f"{error_message}. "
                                        "Please make sure your inputs are correct. " 
                                        "If you're still having trouble, feel free to contact us at EMAILADDRESS "
                                        "and you'll receive a personalised quote.")

        return floor(quote)