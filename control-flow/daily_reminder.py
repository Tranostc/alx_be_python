
def daily_reminder():
    # Prompt for a single task
    task = input("Enter your task: ")  # Customize the prompt message here

    # Prompt for the task's priority with input validation
    while True:
        priority = input("Priority (high/medium/low): ").lower()  # Customize priority options
        if priority in {"high", "medium", "low"}:
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")  # Customize error message here

    # Prompt for whether the task is time-bound with input validation
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()  # Customize the prompt message here
        if time_bound in {"yes", "no"}:
            break
        print("Invalid response. Please enter 'yes' or 'no'.")  # Customize error message here

    # Initialize the reminder message
    reminder = f"'{task}' is a {priority} priority task"

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"  # Customize this message
            else:
                reminder += ". It's important to complete this soon."  # Customize this message
        case "medium":
            if time_bound == "yes":
                reminder += " that requires attention today."  # Customize this message
            else:
                reminder += ". Consider addressing this in the near future."  # Customize this message
        case "low":
            if time_bound == "yes":
                reminder += " that should be done today if possible."  # Customize this message
            else:
                reminder += ". Consider completing it when you have free time."  # Customize this message

    # Print the customized reminder
    print(f"\nReminder: { Finish your project report}")  # Customize the output format her
