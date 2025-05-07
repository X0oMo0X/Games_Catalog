from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # type: ignore
from .. import models, schemas
from ..database import get_db
from ..security import get_current_user

router = APIRouter(
    prefix="/developers",
    tags=["developers"]
)

@router.post("/", response_model=schemas.DeveloperOut)
def create_developer(
    developer: schemas.DeveloperCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_developer = models.Developer(**developer.dict())
    db.add(db_developer)
    db.commit()
    db.refresh(db_developer)
    return db_developer

@router.get("/", response_model=list[schemas.DeveloperOut])
def read_developers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Developer).offset(skip).limit(limit).all()