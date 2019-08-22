import matplotlib.pyplot as plt
import numpy as np
import os

#sheets directory should be in same dir as this script
files = os.listdir(os.getcwd() + "/sheets")
#get data
data = []
#filename: "Job Hunt Tracking - SheetX.csv"
files = sorted(files, key=lambda x: int(x[25:x.index(".")]))
for filename in files:
    with open("sheets/" + filename) as f:
        for i, line in enumerate(f):
            if i > 1 and i < 9:
                data.append(line)
print(data)
def get_date(idx):
    START = "June 10th"
    month_i, day = 0, 10
    for i in range(idx):
        if day < 30:
            day += 1
        else:
            if (month_i == 1 or month_i == 2) and day == 30:
                day += 1
            else:
                month_i += 1
                day = 1
    months = ["June", "July", "August", "September"]
    return "{} {}".format(months[month_i], day)

#Put a date ticker at every interval
date_ticks_ind = []
date_ticks = []
INTERVAL = 12
for i in range(len(data)):
    if i%INTERVAL == 0:
        date_ticks_ind.append(i)
        date_ticks.append(get_date(i))

#get data in individual arrays
applying = []
interviewing = []
prepping = []
for line in data:
    line = line.split(",")
    for i in range(1,4):
        time_spent = int(line[i]) if line[i] != "" else 0
        if i == 1:
            applying.append(time_spent)
        if i == 2:
            interviewing.append(time_spent)
        if i == 3:
            prepping.append(time_spent)
#graph it
plt.figure(figsize=(13,6))
width = 0.4
plt.ylabel("Time spent (minutes)")
plt.title("Job hunting - Time Spent")
plt.ylim(0, 250)
plt.yticks(np.arange(0, 251, 30))
ind = np.arange(len(data))
plt.xticks(np.array(date_ticks_ind), date_ticks)

p1 = plt.bar(ind, prepping, width)
p2 = plt.bar(ind, interviewing, width, bottom=prepping)
p3 = plt.bar(ind, applying, width, bottom=[x+y for x,y in zip(prepping, interviewing)])
plt.legend((p1[0], p2[0], p3[0]), ("Prepping", "Interviewing", "Applying"))
plt.show()

