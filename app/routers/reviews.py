from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..security import get_current_user

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.post("/", response_model=schemas.ReviewOut)
def create_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/", response_model=list[schemas.ReviewOut])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Review).offset(skip).limit(limit).all()