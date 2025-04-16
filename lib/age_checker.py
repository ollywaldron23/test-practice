from datetime import datetime, date

def AgeChecker(date_of_birth):

    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        if age >= 16:
            return "Access granted!"
        else:
            return "Access denied!"
    except (ValueError, TypeError):
        raise ValueError("Date string is in the incorrect format!")
    



