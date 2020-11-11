from datetime import date

# Set Date format like: YYYY, MM, DD
# Note that FIND_FIRST_DATE uses START_DATE as default start date

today = date.today()
year_start = 2020
month_start = 3
day_start = 7

START_DATE = date(year_start, month_start, day_start)
END_DATE = date(today.year, today.month, today.day)

# set to "metric" or "imperial"
UNIT_SYSTEM = "metric"
# UNIT_SYSTEM = "imperial"

# Automatically find first date where data is logged
FIND_FIRST_DATE = False