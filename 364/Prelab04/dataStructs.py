#! /usr/bin/env python3.4

import glob
from pprint import pprint as pp

def uniqueLetters(s):
    answer = []
    letters = list(s)
    for i in range(len(letters)):
        if letters[i] not in answer:
            answer.append(letters[i])

    answer.sort(reverse=True)
    return "".join(answer)

def scaleSet(s, num):
    numbers = list(s)
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        answer[i] = round(numbers[i] * num, 2)

    return set(answer)

def printNames(aSet):
    names = list(aSet)
    names.sort()
    for i in range(len(names)):
        print(names[i])

def getStateName(stateAbb):
    states = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    for key, val in states.items():
        if (stateAbb == val):
            return key

def getZipCodes(stateName):
    states = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    codes = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
    answer = []
    name = states[stateName]
    for key, val in codes.items():
        if name == val:
            answer.append(key)

    answer = set(answer)

    return answer

def printSortedMap(s):
    answer = []
    for (lastname, firstname, mi), weight in s.items():
        o = "{1} {2} {0} has a weight of {3} lb.".format(lastname, firstname, mi, weight)
        answer.append(o)

    answer.sort()
    for item in answer:
        print(item)

def switchNames(s):
    answer = {}
    for (lastname, firstname, mi), val in s.items():
        new_key = firstname + " " + lastname
        answer.update({new_key:val})

    return answer

def getPossibleMatches(record, n):
    answer = []
    for key, (month, date, year) in record.items():
        if n == month or n == date or n == year:
            answer.append(key)

    answer = set(answer)

    return answer

def getPurchaseReport():
    price_dict = {}
    answer = {}
    files = glob.glob('./purchases/*')
    data = [0] * len(files)
    files.sort()
    temp = [0] * 2
    total_value = 0
    prices_file = open(files[0], 'r')
    data = prices_file.readlines()
    for i in range(2, len(data)):
        info = data[i]
        temp = info.split('$')
        temp[0] = temp[0].rstrip()
        temp[1] = float(temp[1])
        price_dict.update({temp[0]:temp[1]})

    for i in range(1, len(files)):
        data_file = open(files[i], 'r')
        data = data_file.readlines()
        total_value = 0
        for j in range(2, len(data)):
            info = data[j]
            temp = info.split()
            temp[0] = temp[0].rstrip()
            temp[1] = int(temp[1])
            total_value = total_value + (temp[1] * price_dict[temp[0]])
        answer.update({i-1:round(total_value, 2)})

    return answer

def getTotalSold():
    price_dict = {}
    answer = {}
    files = glob.glob('./purchases/*')
    data = [0] * len(files)
    files.sort()
    temp = [0] * 2
    total_value = 0
    prices_file = open(files[0], 'r')
    data = prices_file.readlines()
    for i in range(2, len(data)):
        info = data[i]
        temp = info.split('$')
        temp[0] = temp[0].rstrip()
        price_dict.update({temp[0]:0})

    for i in range(1, len(files)):
        data_file = open(files[i], 'r')
        data = data_file.readlines()
        for j in range(2, len(data)):
            info = data[j]
            temp = info.split()
            temp[0] = temp[0].rstrip()
            temp[1] = int(temp[1])
            price_dict[temp[0]] = price_dict[temp[0]] + temp[1]

    return price_dict

if __name__ == "__main__":
    print("-----TESTING uniqueLetters-----")
    letters = "ABDBDARWET"
    answer1 = uniqueLetters(letters)
    print(answer1, "\n\n")

    print("-----TESTING scaleSet-----")
    s = {3.12, 5.0, 7.2, 15.24}
    answer2 = scaleSet(s, 2.1)
    print(answer2, "\n\n")

    print("-----TESTING printNames-----")
    names = {"Harsh", "Digraj", "Apoorv"}
    printNames(names)
    print("\n")

    print("-----TESTING getStateName-----")
    answer4 = getStateName("CA")
    print(answer4, "\n\n")

    print("-----TESTING getZipCodes-----")
    answer5 = getZipCodes("California")
    print(answer5, "\n\n")

    print("-----TESTING printSortedMap-----")
    s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    printSortedMap(s)
    print("\n\n")

    print("-----TESTING switchNames-----")
    answer7 = switchNames(s)
    print(answer7, "\n\n")

    print("-----TESTING getPossibleMatches-----")
    names_bday = {"Digraj": (12, 3, 1996), "Apoorv": (9, 25, 1996), "Pushkal": (11, 9, 1997)}
    answer8 = getPossibleMatches(names_bday, 9)
    print(answer8, "\n\n")

    print("-----TESTING getPurchaseReport-----")
    answer9 = getPurchaseReport()
    pp(answer9)
    print("\n\n")

    print("-----TESTING getTotalSold-----")
    answer10 = getTotalSold()
    pp(answer10)
    print("\n\n")