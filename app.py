print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
weekly_hours = hours * 7
print(f"You are on track to study about {weekly_hours} hours this week.")
