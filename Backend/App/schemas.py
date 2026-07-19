from pydantic import BaseModel


class LocationOut(BaseModel):
    id: int
    name: str
    state: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class CropOut(BaseModel):
    id: int
    name: str
    typical_duration_days: int
    category: str

    class Config:
        from_attributes = True