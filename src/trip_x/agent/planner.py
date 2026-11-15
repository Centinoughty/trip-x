from trip_x.llm.model import get_llm
from trip_x.prompt.planner import TRAVEL_PLANNER_PROMPT
from trip_x.schema.itinerary import Itinerary
from trip_x.schema.trip import TripRequest


class TravelPlanner:
    def __init__(self):
        self.llm = get_llm()
        self.structured_llm = self.llm.with_structured_output(Itinerary, method="json_schema")


    def generate_itinerary(self, trip_req: TripRequest):
        messages = TRAVEL_PLANNER_PROMPT.invoke(
            {
                "trip_request": trip_req.model_dump_json(indent=2)
            }
        )

        itinerary = self.structured_llm.invoke(messages)
        return itinerary
