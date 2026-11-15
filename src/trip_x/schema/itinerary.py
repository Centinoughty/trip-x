import re
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


def parse_currency_decimal(value):
    if isinstance(value, Decimal):
        return value

    if isinstance(value, (int, float)):
        return Decimal(str(value))

    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Decimal value cannot be empty")

        numeric = re.sub(r"[^0-9.\-]", "", cleaned)
        if numeric in {"", ".", "-", "-."}:
            raise ValueError(f"Invalid decimal value: {value!r}")

        return Decimal(numeric)

    raise TypeError(f"Unsupported value for decimal conversion: {type(value).__name__}")


class Activity(BaseModel):
    name: str
    description: str
    estimated_cost: Decimal = Field(ge=0)
    duration: float = Field(gt=0)

    @field_validator("estimated_cost", mode="before")
    @classmethod
    def normalize_estimated_cost(cls, value):
        return parse_currency_decimal(value)


class DailyPlan(BaseModel):
    day: int = Field(ge=1)
    location: str
    activities: list[Activity]
    transportation: str
    estimated_daily_cost: Decimal = Field(ge=0)

    @field_validator("estimated_daily_cost", mode="before")
    @classmethod
    def normalize_estimated_daily_cost(cls, value):
        return parse_currency_decimal(value)


class BudgetBreakdown(BaseModel):
    transportation: Decimal = Field(ge=0)
    accommodation: Decimal = Field(ge=0)
    food: Decimal = Field(ge=0)
    activities: Decimal = Field(ge=0)
    miscellaneous: Decimal = Field(ge=0)
    total_estimated_cost: Decimal = Field(ge=0)

    @field_validator("transportation", "accommodation", "food", "activities", "miscellaneous", "total_estimated_cost", mode="before")
    @classmethod
    def normalize_budget_amount(cls, value):
        return parse_currency_decimal(value)


class Itinerary(BaseModel):
    destination: str
    summary: str

    daily_plans: list[DailyPlan]
    budget: BudgetBreakdown

    recommendations: list[str]
    important_notes: list[str]
