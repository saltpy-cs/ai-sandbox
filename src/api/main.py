from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
from database import Base, SessionLocal, engine
from seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_database()
    yield


app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/1/passenger/{passenger_id}")
def get_passenger(passenger_id: int, db: Session = Depends(get_db)):
    passenger = db.query(models.Passenger).filter(models.Passenger.id == passenger_id).first()
    if passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return {
        "id": passenger.id,
        "name": passenger.name,
        "age": passenger.age,
        "sex": passenger.sex,
        "class": passenger.pclass,
        "survived": passenger.survived,
    }


@app.get("/api/1/passenger")
def list_passengers(sex: Optional[str] = None, survived: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(models.Passenger)
    if sex is not None:
        query = query.filter(models.Passenger.sex == sex)
    if survived is not None:
        query = query.filter(models.Passenger.survived == survived)
    passengers = query.all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "sex": p.sex,
            "class": p.pclass,
            "survived": p.survived,
        }
        for p in passengers
    ]
