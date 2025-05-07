from fastapi import FastAPI
from .database import Base, engine
from .routers import users, developers, games, reviews

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(developers.router)
app.include_router(games.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Games Catalog API"}