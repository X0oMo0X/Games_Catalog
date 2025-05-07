import stat
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..security import get_password_hash, create_access_token, verify_password
from datetime import timedelta

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Проверка на существующего пользователя
    db_user = db.query(models.User).filter(
        (models.User.email == user.email) | 
        (models.User.username == user.username)
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email or username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=stat.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": str(db_user.id)},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}