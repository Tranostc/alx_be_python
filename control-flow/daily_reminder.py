def daily_reminder():
    # Prompt for a single task
    task = input("Finish your project report: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder_message = f"'{task}' is a {priority} priority task"

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            reminder_message += " Please finishthe project report!"
        case "medium":
            reminder_message += ". Consider completing it soon."
        case "low":
            reminder_message += ". Consider completing it when you have free time."
        case _:
            reminder_message = "Invalid priority level specified."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes" and priority in ["high", "medium", "low"]:
        reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"

    # Print the customized reminder
    print("Please finish the project report")
