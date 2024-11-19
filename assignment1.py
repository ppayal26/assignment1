#!/usr/bin/env python3

"""
OPS435 Assignment 1
Program: assignment1.py
Author: "ppayal1"
The python code in this file is original work written by the author.
"""

import sys

def leap_year_check(year):
    """Determine if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def month_days(year, month):
    """Determine the number of days in a given month."""
    days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year_check(year):
        return 29
    return days_in_months.get(month, 0)

def increment_date(year, month, day):
    """Move the date to the next day."""
    if day < month_days(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def validate_date(date_string):
    """Validate the input date format and logical correctness."""
    try:
        year, month, day = map(int, date_string.split('-'))
        if 1 <= month <= 12 and 1 <= day <= month_days(year, month):
            return True
    except (ValueError, AttributeError):
        pass
    return False

def calculate_weekends(start_date, end_date):
    """Calculate the number of weekend days in the given range."""
    weekend_count = 0
    y1, m1, d1 = map(int, start_date.split('-'))
    y2, m2, d2 = map(int, end_date.split('-'))

    while (y1, m1, d1) <= (y2, m2, d2):
        # Formula to find the day of the week (0 = Sunday, ..., 6 = Saturday)
        k = d1
        m = m1 - 2 if m1 > 2 else m1 + 10
        if m1 <= 2:
            y1 -= 1
        day_of_week = (k + (13 * m - 1) // 5 + y1 % 100 +
                       (y1 % 100) // 4 + (y1 // 100) // 4 - 2 * (y1 // 100)) % 7
        if day_of_week in {0, 6}:  # 0 = Sunday, 6 = Saturday
            weekend_count += 1

        # Restore original year if it was altered
        if m1 <= 2:
            y1 += 1

        y1, m1, d1 = increment_date(y1, m1, d1)

    return weekend_count

def show_usage():
    """Display the usage instructions for incorrect input."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    exit(1)

def main():
    if len(sys.argv) != 3:
        show_usage()

    start_date, end_date = sys.argv[1], sys.argv[2]
    if not (validate_date(start_date) and validate_date(end_date)):
        show_usage()

    # Ensure the start_date is earlier
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekend_days = calculate_weekends(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")

if __name__ == "__main__":
    main()

