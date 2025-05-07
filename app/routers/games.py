from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..security import get_current_user

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.post("/", response_model=schemas.GameOut)
def create_game(
    game: schemas.GameCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

@router.get("/", response_model=list[schemas.GameOut])
def read_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Game).offset(skip).limit(limit).all()