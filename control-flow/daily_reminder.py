while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ['high', 'medium', 'low']:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Validate time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ['yes', 'no']:
        break
    print("Invalid response. Please enter 'yes' or 'no'.")

# Build base message based on priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task that requires immediate attention today!"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task. Consider completing it soon."
    case "low":
        reminder_message = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Override if time-bound is yes
if time_bound == 'yes':
    reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"

print("Reminder:", reminder_message)
