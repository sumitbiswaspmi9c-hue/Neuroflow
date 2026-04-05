def schedule_tasks(tasks, user_input):
    print("Calendar Agent Running")

    schedule = []
    day = 1

    time_slots = [
        "9 AM - 11 AM",
        "11:30 AM - 1:30 PM",
        "3 PM - 5 PM",
        "6 PM - 8 PM"
    ]

    priority_order = {"Critical": 1, "High": 2, "Medium": 3}
    tasks_sorted = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))

    for i, task in enumerate(tasks_sorted):
        schedule.append({
            "day": f"Day {day}",
            "task": task["task"],
            "priority": task["priority"],
            "time": time_slots[i % len(time_slots)],
            "estimated_time": task["estimated_time"]
        })

       
        if (i + 1) % len(time_slots) == 0:
            day += 1

    return schedule
