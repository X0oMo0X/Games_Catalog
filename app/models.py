from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Developer(Base):
    __tablename__ = "developers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    games = relationship("Game", back_populates="developer")

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    release_year = Column(Integer)
    developer_id = Column(Integer, ForeignKey("developers.id"))
    developer = relationship("Developer", back_populates="games")
    reviews = relationship("Review", back_populates="game")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    rating = Column(Float)
    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="reviews")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)