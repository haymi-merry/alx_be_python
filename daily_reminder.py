task = input("Enter your task: ").strip()
priority = input("priority (high/medium/low): ").strip()
time_bound = input("Is it time bound? (yes/no): ").strip().lower()

if priority == "high" and time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
elif priority == "high" and time_bound == "no":
    print(f"Reminder: '{task}' is a high priority task that should be completed soon.")
elif priority == "medium" and time_bound == "yes":
    print(f"Reminder: '{task}' is a medium priority task that needs to be done today.")
elif priority == "medium" and time_bound == "no":
    print(f"Reminder: '{task}' is a medium priority task that can be scheduled for later.")
elif priority == "low" and time_bound == "yes":
    print(f"Reminder: '{task}' is a low priority task that should be done today if possible.")
elif priority == "low" and time_bound == "no":
    print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print("Invalid input. Please check the priority and time bound values.")

print("Have a productive day!")