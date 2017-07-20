import operations as op
import re

from pprint import pprint as pp

def readFile(filename):
    file_ptr = open(filename)
    data = file_ptr.readlines()
    newData = []
    finalItem = []
    for item in data[2:]:
        pattern = r"[^\s*]+"
        matched = re.findall(pattern, item)
        newData.append(matched)

    return newData

def getTotalDuration(eventName):
    data = readFile("Events.txt")
    totalDays = 0
    totalWeeks = 0
    totalHours = 0
    for item in data:
        if str(item[0]) == str(eventName):
            if item[1][-1] == "h":
                totalHours = totalHours + int(item[1][:-1]) * int(item[2])
            if item[1][-1] == "d":
                totalDays = totalDays + int(item[1][:-1]) * int(item[2])
            if item[1][-1] == "w":
                totalWeeks = totalWeeks + int(item[1][:-1]) * int(item[2])

    newDuration = op.Duration(totalWeeks, totalDays, totalHours)
    return newDuration

def rankEventsByDuration(*args):
    pass

if __name__ == "__main__":
    answer = getTotalDuration("Event17")
    print(answer)