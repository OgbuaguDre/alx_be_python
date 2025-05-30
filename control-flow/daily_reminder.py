# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize base message based on priority
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        # For unrecognized priority, print a separate message and exit
        print(f"Reminder: '{task}' has an unrecognized priority level.")
        exit()

# Append urgency based on time-bound flag
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

# Print the final reminder message
print(f"Reminder: '{task}' is a {priority_message} {time_message}")
