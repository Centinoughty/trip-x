from decimal import Decimal
from pydantic import BaseModel, Field


class Activity(BaseModel):
    name: str
    description: str
    estimated_cost: Decimal = Field(ge=0)
    duration: float = Field(gt=0)


class DailyPlan(BaseModel):
    day: int = Field(ge=1)
    location: str
    activities: list[Activity]
    transportation: str
    estimated_daily_cost: Decimal = Field(ge=0)


class BudgetBreakdown(BaseModel):
    transportation: Decimal = Field(ge=0)
    accommodation: Decimal = Field(ge=0)
    food: Decimal = Field(ge=0)
    activities: Decimal = Field(ge=0)
    miscellaneous: Decimal = Field(ge=0)

    total_estimated_cost: Decimal = Field(ge=0)


class Itinerary(BaseModel):
    destination: str
    summary: str

    daily_plans: list[DailyPlan]
    budget: BudgetBreakdown

    recommendations: list[str]
    important_notes: list[str]
