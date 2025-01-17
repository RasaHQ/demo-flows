from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions.db import get_restaurants


class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_restaurant_form"

    def validate_cuisine(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""
        restaurants = get_restaurants(tracker.sender_id)
        cuisine_list = set([
            r.cuisine.lower()
            for r in restaurants
        ])

        if slot_value.lower() in cuisine_list:
            return {"cuisine": slot_value}
        else:
            return {"cuisine": None}

    def validate_restaurant_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate restaurant name."""
        restaurants = get_restaurants(tracker.sender_id)
        restaurant_names = set([
            r.name.lower()
            for r in restaurants
        ])

        if slot_value.lower() in restaurant_names:
            return {"restaurant_name": slot_value}
        else:
            return {"restaurant_name": None}
