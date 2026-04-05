from app.db.database import SessionLocal
from app.db.models import Plan
from datetime import datetime


def save_plan(user_input, tasks, schedule):
    print("Notes Agent Running")

    db = SessionLocal()

    try:
        new_plan = Plan(
            user_input=user_input,
            tasks=str(tasks),        
            schedule=str(schedule),
            created_at=datetime.now()
        )

        db.add(new_plan)
        db.commit()

        print("Plan saved successfully")

    except Exception as e:
        print("DB ERROR:", str(e))

    finally:
        db.close()


def get_all_plans():
    print("Fetching all plans")

    db = SessionLocal()

    try:
        plans = db.query(Plan).all()
        return plans

    except Exception as e:
        print("FETCH ERROR:", str(e))
        return []

    finally:
        db.close()