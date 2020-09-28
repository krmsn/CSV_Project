# import modules for writing.

import csv
from datetime import datetime

# 

open_file_dv = open("death_valley_2018_simple.csv", "r")

csv_file_dv = csv.reader(open_file_dv, delimiter = ",")

header_row_dv = next(csv_file_dv)

print(header_row_dv)

for index_dv, column_header_dv in enumerate(header_row_dv):
    print(index_dv, column_header_dv)

# create empty lists for storing highs, lows, and dates for each entry.

highs_dv = []
lows_dv = []
dates_dv = []

x_dv = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(x_dv)

# fetch data from rows; 
# send entries from column five to the "highs" list - 
# send entries from column six to the "lows" list -
# send dates from each entry to the "dates" list.

for row_dv in csv_file_dv:
    try:
        high_dv = int(row_dv[4])
        low_dv = int(row_dv[5])
        date_dv = datetime.strptime(row_dv[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for entry {date_dv}")
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(date_dv)


# import and draw plot parameters;

import matplotlib.pyplot as plt

plt.plot(dates_dv, highs_dv, c = "red", alpha = 0.5)
plt.plot(dates_dv, lows_dv, c = "blue", alpha = 0.5)

plt.title("Daily High & Low Temperatures\nDeath Valley - 2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor = "blue", alpha = 0.1)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", labelsize = 16)

plt.show()
