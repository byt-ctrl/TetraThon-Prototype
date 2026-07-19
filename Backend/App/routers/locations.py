from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter()


@router.get("/locations", response_model=list[schemas.LocationOut])
@router.get("/api/locations", response_model=list[schemas.LocationOut])
def get_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()
