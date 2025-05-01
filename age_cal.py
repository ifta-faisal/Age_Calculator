from datetime import datetime

def calculate_age(dob):
    # Current date
    today = datetime.today()
    
    # Convert the date of birth (dob) to a datetime object
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Calculate age based on current date and date of birth
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age

# Take date of birth as input
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
age = calculate_age(dob_input)

# Output the age
print(f"Your age is: {age} years old.")
