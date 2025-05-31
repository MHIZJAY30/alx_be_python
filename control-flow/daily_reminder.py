# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process input using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to get it done as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan it into your schedule.")
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is a low priority task, but it still requires completion today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority input. Please enter high, medium, or low.")