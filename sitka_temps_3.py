# import modules for writing.

import csv
from datetime import datetime

# 

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# create empty lists for storing highs, lows, and dates for each entry.

highs = []
lows = []
dates = []

#

x = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(x)

# fetch data from rows; 
# send entries from column five to the "highs" list - 
# send entries from column six to the "lows" list -
# send dates from each entry to the "dates" list.

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(the_date)

# import and draw plot parameters;

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)
ax[0].set_title("SITKA AIRPORT, AK US")
ax[0].plot(dates, highs, c = "red", alpha = 0.5)
ax[0]

ax[1].set_title("DEATH VALLEY, CA US")

plt.plot(dates, highs, c = "red", alpha = 0.5)
plt.plot(dates, lows, c = "blue", alpha = 0.5)

plt.title("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", labelsize = 16)

plt.show()
