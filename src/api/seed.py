import csv
import io
import urllib.request

from database import SessionLocal
from models import Passenger

# Stanford CS109 Titanic dataset — 887 passengers, no PassengerId column
_CSV_URL = (
    "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
)


def seed_database():
    db = SessionLocal()
    try:
        if db.query(Passenger).count() > 0:
            return

        with urllib.request.urlopen(_CSV_URL) as response:
            content = response.read().decode("utf-8")

        reader = csv.DictReader(io.StringIO(content))
        passengers = [
            Passenger(
                id=i,
                name=row["Name"],
                age=float(row["Age"]) if row.get("Age") else None,
                sex=row["Sex"],
                pclass=int(row["Pclass"]),
                survived=bool(int(row["Survived"])),
            )
            for i, row in enumerate(reader, start=1)
        ]

        db.bulk_save_objects(passengers)
        db.commit()
        print(f"Seeded {len(passengers)} passengers.")
    finally:
        db.close()
