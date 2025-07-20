def daily_reminder():
    # Prompt for a single task
    task = input("Please enter your task description: ")
    priority = input("Enter the priority level (high, medium, low): ").lower()
    time_bound = input("Is this task time-bound? (yes or no): ").lower()

    # Initialize the reminder message
    reminder_message = f"Reminder: You have a task '{task}' with {priority} priority."

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            reminder_message += " This task is very important."
        case "medium":
            reminder_message += " This task is of moderate importance."
        case "low":
            reminder_message += " This task is of low importance."
        case _:
            reminder_message += " (Invalid priority level specified.)"

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder_message += " This requires immediate attention today!"
    
    # Print the customized reminder
    print(reminder_message)
