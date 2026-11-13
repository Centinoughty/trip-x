from datetime import date
from decimal import Decimal
from pydantic import ValidationError
import pytest

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
