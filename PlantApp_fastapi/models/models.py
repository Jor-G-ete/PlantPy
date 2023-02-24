from datetime import datetime
from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    code: int
    error: bool
    response: dict


class Plant(BaseModel):
    # Description attributes
    name: str
    color: str = Field(max_length=10)
    size: str = Field(max_length=3)
    born_in: datetime | datetime = datetime.now()
    level: int

    # Characteristic attributes
    heigth: float | float = 0
    width: float | float = 0

    # Needs
    sunligth: float | float = 0
    water: float | float = 0
    humidty: float | float = 0
    nutrients: float | float = 0

    # Variables
    last_time_watered: datetime | datetime = born_in
    last_time_fertilised: datetime | datetime = born_in
