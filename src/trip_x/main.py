import json
from datetime import date
from decimal import Decimal

from trip_x.agent.planner import TravelPlanner
from trip_x.schema.trip import TripRequest


def _json_output(payload):
    if hasattr(payload, "model_dump"):
        payload = payload.model_dump(mode="json")
    return json.dumps(payload, ensure_ascii=False, indent=2)


def main():
    try:
        trip_request = TripRequest(
            destination="Japan",
            start_date=date(2027, 3, 1),
            end_date=date(2027, 3, 8),
            members=2,
            budget=Decimal("150000"),
            currency="INR",
            interests=[
                "culture",
                "food",
                "adventure",
            ],
            travel_style="moderate",
            accommodation_type="mid_range",
            additional_req=[
                "Prefer public transportation",
                "Avoid overcrowded tourist attractions",
                "Include local food experiences",
            ],
        )

        planner = TravelPlanner()
        itinerary = planner.generate_itinerary(trip_request)
        print(_json_output(itinerary))
    except Exception as exc:
        error_payload = {
            "error": {
                "type": type(exc).__name__,
                "message": str(exc),
            }
        }
        print(_json_output(error_payload))


if __name__ == "__main__":
    main()