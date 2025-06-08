# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_datetime)

def calculate_future_date(days):
    """
    Calculates the future date after adding the specified number of days to the current date.
    Prints the result in YYYY-MM-DD format.
    
    Args:
        days (int): Number of days to add
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future Date after", days, "days:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    
    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
