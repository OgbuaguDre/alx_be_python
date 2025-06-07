# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Returns the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def calculate_future_date(days):
    """
    Returns the future date after adding the specified number of days to the current date.
    
    Args:
        days (int): Number of days to add

    Returns:
        str: Future date in YYYY-MM-DD format
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

def main():
    current = display_current_datetime()
    print("Current Date and Time:", current)

    try:
        days_input = int(input("Enter the number of days to add: "))
        future = calculate_future_date(days_input)
        print("Future Date after", days_input, "days:", future)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
