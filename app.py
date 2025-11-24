# Welcome message
print("Welcome to my Python program!")
# Get daily study hours from user
hours = input("How many hours did you study today? ")
# Convert input to number with error handling and calculate weekly hours
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
weekly_hours = hours * 7 # Calculate estimated weekly study hours
# Display result clearly
print(f"You are on track to study about {weekly_hours} hours this week.")
