def daily_reminder():
    # Get task input
    task = input("Finish your project: ")

    # Validate priority with loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in {"high", "medium", "low"}:
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Validate time-bound status with loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in {"yes", "no"}:
            break
        print("Invalid response. Please enter 'yes' or 'no'.")

    # Base message template
    reminder = f"'{task}' is a {priority} priority task"

    # Time sensitivity check
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        # Priority-based suggestions
        match priority:
            case "high":
                reminder += ". Complete this first in your schedule"
            case "medium":
                reminder += ". Address this after urgent tasks"
            case "low":
                reminder += ". Consider this during downtime"

    print(f"\nReminder: {reminder}")
