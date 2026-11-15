from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, model_validator
from typing import Literal


class TripRequest(BaseModel):
    destination: str = Field(min_length=2, description="Desired travel destination")
    
    start_date: date
    end_date: date

    members: int = Field(ge=1, le=50, description="Number of travelers")
    
    budget: Decimal = Field(gt=0, description="Total budget of the trip")
    currency: str = Field(default="INR")

    interests: list[str] = Field(default_factory=list, description="Travel interests such as food, adventure, culture")

    travel_style: Literal["budget", "moderate", "luxury"] = "moderate"
    accommodation_type: Literal["hostel", "budget_hotel", "mid_range", "luxury"] = "mid_range"

    additional_req: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date < self.start_date:
            raise ValueError("End date must be after start date")

        return self
