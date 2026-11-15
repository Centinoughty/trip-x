import json
from datetime import date
from decimal import Decimal

from pydantic import ValidationError
import pytest

from trip_x.main import main
from trip_x.schema.itinerary import Itinerary
from trip_x.schema.trip import TripRequest


def test_valid_trip_request():
    trip = TripRequest(
        destination="Egypt",
        start_date=date(2026, 11, 4),
        end_date=date(2026, 11, 4),
        members=2,
        budget=Decimal("150000"),
        interests=["culture", "food"]
    )

    assert trip.destination == "Egypt"
    assert trip.members == 2
    assert trip.currency == "INR"


def test_invalid_traveler_count():
    with pytest.raises(ValidationError):
        TripRequest(
            destination="Egypt",
            start_date=date(2027, 3, 1),
            end_date=date(2027, 3, 8),
            members=0,
            budget=Decimal("150000")
        )


def test_invalid_dates():
    with pytest.raises(ValidationError):
        TripRequest(
            destination="Egypt",
            start_date=date(2027, 3, 8),
            end_date=date(2027, 3, 1),
            members=2,
            budget=Decimal("150000")
        )


def test_itinerary_accepts_currency_strings():
    itinerary = Itinerary(
        destination="Japan",
        summary="A brief trip summary",
        daily_plans=[
            {
                "day": 1,
                "location": "Tokyo",
                "activities": [
                    {
                        "name": "Temple visit",
                        "description": "Visit a historic temple.",
                        "estimated_cost": "1500 INR",
                        "duration": 3.5,
                    }
                ],
                "transportation": "Train",
                "estimated_daily_cost": "4500 INR",
            }
        ],
        budget={
            "transportation": "42000 INR",
            "accommodation": "60000 INR",
            "food": "32000 INR",
            "activities": "12000 INR",
            "miscellaneous": "8000 INR",
            "total_estimated_cost": "154000 INR",
        },
        recommendations=["Take the subway"],
        important_notes=["Carry cash"],
    )

    assert itinerary.daily_plans[0].activities[0].estimated_cost == Decimal("1500")
    assert itinerary.budget.total_estimated_cost == Decimal("154000")


def test_main_prints_valid_json(monkeypatch, capsys):
    class FakePlanner:
        def generate_itinerary(self, trip_request):
            return Itinerary(
                destination="Japan",
                summary="A brief trip summary",
                daily_plans=[
                    {
                        "day": 1,
                        "location": "Tokyo",
                        "activities": [
                            {
                                "name": "Temple visit",
                                "description": "Visit a historic temple.",
                                "estimated_cost": Decimal("1200"),
                                "duration": 3.5,
                            }
                        ],
                        "transportation": "Train",
                        "estimated_daily_cost": Decimal("2500"),
                    }
                ],
                budget={
                    "transportation": Decimal("2500"),
                    "accommodation": Decimal("4000"),
                    "food": Decimal("3000"),
                    "activities": Decimal("1200"),
                    "miscellaneous": Decimal("500"),
                    "total_estimated_cost": Decimal("11200"),
                },
                recommendations=["Take the subway"],
                important_notes=["Carry cash"],
            )

    monkeypatch.setattr("trip_x.main.TravelPlanner", FakePlanner)

    main()

    output = capsys.readouterr().out
    payload = json.loads(output)

    assert payload["destination"] == "Japan"
    assert payload["summary"] == "A brief trip summary"
    assert isinstance(payload["daily_plans"], list)
