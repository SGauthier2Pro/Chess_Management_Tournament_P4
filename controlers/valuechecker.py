"""verificateur de données"""

import datetime
import time


def is_valid_date(date_to_test):
    """methode de test de date renvoi True ou False"""
    year = 0
    month = 0
    day = 0
    valid_date = True

    try:
        day, month, year = date_to_test.split('/')
    except ValueError:
        valid_date = False

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        valid_date = False

    return valid_date


def compare_dates(dates, date_to_compare):
    """compare deux date et renvoi True si identique"""
    compare_date = False
    if dates:
        for date in dates:
            first_date = date
            second_date = date_to_compare

            formatted_date1 = time.strptime(first_date, "%d/%m/%Y")
            formatted_date2 = time.strptime(second_date, "%d/%m/%Y")

            if formatted_date1 == formatted_date2:
                compare_date = True

    return compare_date


def is_valid_int(int_to_test):
    try:
        int(int_to_test)
        return True

    except ValueError:
        return False


def is_valid_gender(gender_to_test):
    if gender_to_test in ["M", "F", "ND"]:
        return True
    else:
        return False
