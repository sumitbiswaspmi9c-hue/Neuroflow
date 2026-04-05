from fastapi import FastAPI
from pydantic import BaseModel

# ✅ NEW IMPORTS (safe)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import os

print("🚀 NeuroFlow starting...")

app = FastAPI(title="NeuroFlow AI")

# ✅ SERVE STATIC FILES (SAFE)
app.mount("/static", StaticFiles(directory="static"), name="static")


# ✅ Lazy imports (VERY IMPORTANT)
def get_agents():
    from app.agents.primary_agent import handle_user_request
    from app.agents.notes_agent import get_all_plans
    return handle_user_request, get_all_plans


def init_db():
    try:
        from app.db.database import Base, engine
        Base.metadata.create_all(bind=engine)
        print("✅ DB initialized")
    except Exception as e:
        print("❌ DB ERROR:", str(e))


@app.on_event("startup")
def startup():
    init_db()


# ✅ Request Model
class UserRequest(BaseModel):
    user_input: str


# ✅ Health route (DO NOT TOUCH)
@app.get("/")
def home():
    return {"status": "running"}


# ✅ UI ROUTE (SAFE ADDITION)
@app.get("/ui")
def serve_ui():
    return FileResponse("static/index.html")


# ✅ Plan API
@app.post("/plan")
def plan_task(request: UserRequest):
    try:
        handle_user_request, _ = get_agents()

        result = handle_user_request(request.user_input)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }


# ✅ Fetch Plans
@app.get("/plans")
def fetch_plans():
    try:
        _, get_all_plans = get_agents()

        plans = get_all_plans()

        return {
            "status": "success",
            "count": len(plans),
            "data": [
                {
                    "id": plan.id,
                    "user_input": plan.user_input,
                    "tasks": plan.tasks,
                    "schedule": plan.schedule
                }
                for plan in plans
            ]
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }
