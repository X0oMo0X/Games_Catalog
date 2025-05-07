from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class DeveloperBase(BaseModel):
    name: str
    description: str

class DeveloperCreate(DeveloperBase):
    pass

class DeveloperOut(DeveloperBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class GameBase(BaseModel):
    title: str
    genre: str
    release_year: int
    developer_id: int

class GameCreate(GameBase):
    pass

class GameOut(GameBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ReviewBase(BaseModel):
    content: str
    rating: float
    game_id: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None