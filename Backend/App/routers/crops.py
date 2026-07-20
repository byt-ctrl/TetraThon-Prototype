from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter()


@router.get("/crops", response_model=list[schemas.CropOut])
def get_crops(db: Session = Depends(get_db)):
    return db.query(models.Crop).all()
