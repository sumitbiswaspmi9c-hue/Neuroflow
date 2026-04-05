import random

def create_tasks(user_input):
    print("Task Agent Running")

    user_input = user_input.lower()

    tasks = []

    keywords = user_input.split()
    subjects = []

    for word in keywords:
        if word in ["math", "physics", "chemistry", "biology", "cs"]:
            subjects.append(word.capitalize())

    if not subjects:
        subjects = ["Math", "Physics", "Chemistry"]

    priorities = ["High", "Medium", "Critical"]

    # ✅ Generate subject tasks
    for subject in subjects:
        tasks.append({
            "task": f"Study {subject}",
            "priority": random.choice(priorities),
            "estimated_time": f"{random.randint(1,3)} hrs"
        })

    # ✅ ADD EXTRA TASKS (FIXED INDENTATION)
    if "exam" in user_input or "study" in user_input:
        tasks.append({
            "task": "Revise all subjects",
            "priority": "High",
            "estimated_time": "2 hrs"
        })
        tasks.append({
            "task": "Solve previous year papers",
            "priority": "Critical",
            "estimated_time": "3 hrs"
        })

    elif "project" in user_input:
        tasks.extend([
            {"task": "Research topic", "priority": "High", "estimated_time": "2 hrs"},
            {"task": "Build implementation", "priority": "Critical", "estimated_time": "4 hrs"}
        ])

    elif "trip" in user_input or "travel" in user_input:
        tasks.extend([
            {"task": "Book tickets", "priority": "Critical", "estimated_time": "1 hr"},
            {"task": "Plan itinerary", "priority": "High", "estimated_time": "2 hrs"}
        ])

    # ✅ Add step numbers
    for i, t in enumerate(tasks, 1):
        t["step"] = i

    return tasks