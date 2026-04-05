from app.agents.task_agent import create_tasks
from app.agents.calendar_agent import schedule_tasks
from app.agents.notes_agent import save_plan


def handle_user_request(user_input):

    print("Primary Agent: Received request")

    
    tasks = create_tasks(user_input)
    print("Task Agent Done")

    
    schedule = schedule_tasks(tasks, user_input)
    print("Calendar Agent Done")

    save_plan(user_input, tasks, schedule)
    print("Notes Agent Saved Data")

    return {
        "workflow": {
            "input": user_input,
            "steps": [
                "Task Generation",
                "Schedule Creation",
                "Memory Storage"
            ],
            "agents_used": [
                "Primary Agent",
                "Task Agent",
                "Calendar Agent",
                "Notes Agent"
            ]
        },
        "output": {
            "tasks": tasks,
            "schedule": schedule
        },
        "insight": "A structured workflow has been generated to optimize your time and productivity",
        "status": "completed"
    }