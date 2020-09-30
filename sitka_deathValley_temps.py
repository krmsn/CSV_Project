# Import libraries:

# "csv" allows us to manipulate .csv data
# "datetime" supplies modules for manipulating date & time data
# matplotlib.pyplot will be used to assemble, graph, and present final results.

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# First, SITKA records will be processed;
# This chunk is responsible for fetching SITKA's data tables and determining the file's header row.
# Send the raw data file through "csv.reader()," which will output a new file with a custom delimiter.
# Additionally it will print indices for the "header row," which contains all the fields for the data table.

print("\nSITKA RECORDS: \n")

open_file_s = open("sitka_weather_2018_simple.csv", "r")
csv_file_s = csv.DictReader(open_file_s, delimiter = ",")
header_row_s = next(csv_file_s)
print(header_row_s)

for index_s, column_header_s in enumerate(header_row_s):
    print(index_s, column_header_s)

# Create empty lists for storing temperature highs and lows, as well as dates for each entry.

highs_s = []
lows_s = []
dates_s = []

# The for-loop assigns the desired temperature data to variables "high," "low," and "date."

# "datetime" initiates a format for interpretting and displaying dates, 
# particularly for the case of missing entries. 

# The try/except block will check for blank spaces per dated entry.
# If any are found, that row will not be processed - 
# the user will be notified that data is missing for that date.

for header_row_s in csv_file_s:
    try:
        high_s = int(header_row_s["TMAX"])
        low_s = int(header_row_s["TMIN"])
        date_s = datetime.strptime(header_row_s["DATE"], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for entry {date_s}")
    else:
        highs_s.append(high_s)
        lows_s.append(low_s)
        dates_s.append(date_s)

# Repeat process for DEATH VALLEY records.

print("\nDEATH VALLEY RECORDS: \n")

open_file_dv = open("death_valley_2018_simple.csv", "r")
csv_file_dv = csv.DictReader(open_file_dv, delimiter = ",")
header_row_dv = next(csv_file_dv)
print(header_row_dv)

for index_dv, column_header_dv in enumerate(header_row_dv):
    print(index_dv, column_header_dv)

highs_dv = []
lows_dv = []
dates_dv = []

for header_row_dv in csv_file_dv:
    try:
        high_dv = int(header_row_dv["TMAX"])
        low_dv = int(header_row_dv["TMIN"])
        date_dv = datetime.strptime(header_row_dv["DATE"], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for entry {date_dv}")
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(date_dv)

# First, split the plot page so it will show two separate plots. The plot page is designated by "fig."
# The subplots are designated "ax," and uses list indices to refer to each subplot.

# The "highs," "lows," and "dates" lists for SITKA records are each assigned as parts of the graph.
# "highs" will be shown as a red line, "lows" will be shown as blue.
# The differences between these two lines is shown by fill_between(); for this, the field is shaded blue.

fig, ax = plt.subplots(2, sharex = True)
fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize = 16)
ax[0].set_title(header_row_s["NAME"])
ax[0].plot(dates_s, highs_s, c = "red", alpha = 0.5)
ax[0].plot(dates_s, lows_s, c = "blue", alpha = 0.5)
ax[0].fill_between(dates_s, highs_s, lows_s, facecolor = "blue", alpha = 0.1)
ax[0].tick_params(axis = "x", labelsize = 13)

# Repeat process for DEATH VALLEY records.
# ("sharex" is added as an argument for subplots(), since both subplots share the same x-axis values.)

ax[1].set_title(header_row_dv["NAME"])
ax[1].plot(dates_dv, highs_dv, c = "red", alpha = 0.5)
ax[1].plot(dates_dv, lows_dv, c = "blue", alpha = 0.5)
ax[1].fill_between(dates_dv, highs_dv, lows_dv, facecolor = "blue", alpha = 0.1)
ax[1].tick_params(axis = "x", labelsize = 13, labelrotation = 45)

# Display output.

plt.show()
