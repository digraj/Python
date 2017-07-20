#! /usr/local/bin/python3.4

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()
    return lines


def getAverageBySignal(signalName):
    counter = 0
    addition = 0
    inputs = loadFile()
    names = inputs[0].split()
    for i in range(len(names)):
        counter = counter + 1
        if (signalName == names[i]):
            found = counter

    for i in range(2, len(inputs)):
        numbers = inputs[i].split()
        for j in range(len(numbers)):
            if (j == found):
                addition = addition + float(numbers[j])

    average = addition / (len(inputs) - 2)

    return round(average, 2)

def getAverageByDay(day):
    inputs = loadFile()
    addition = 0
    length = len(inputs)
    for i in range(len(inputs)):
        broken = inputs[i].split()
        if (day == broken[0]):
            date = i

    required_date = inputs[date].split()
    for i in range(1, len(broken)):
        addition = addition + float(required_date[i])

    average = addition / (len(broken) -1)

    return round(average, 2)


def split(l, n):
    temp = []
    output = []
    for i in range(len(l)):
        if (len(temp) % n == 0) and i != 0:
            output.append(temp)
            temp = []
        temp.append(l[i])
    if (temp != []):
        output.append(temp)

    return output


def getPalindromes():
    answer = []
    m = 0
    for i in range(100, 999):
        for j in range(100, 999):
            k = i * j
            m = list(str(k))
            length = len(m)
            m.reverse()
            m = "".join(m)
            if m == str(k) and k not in answer and length > 5:
                answer.append(k)

#    answer = answer.sort()
    return sorted(answer)

    pass


def getWords(sentence, c):
    output = []
    words = sentence.split()
    for word in words:
        if c == word[-1] or c == word[0]:
            if word not in output:
                output.append(word)

    return output

def getCumulativeSum():
    sum = 0
    output = []
    for i in range(1, 100):
        sum = sum + i
        output.append(sum)

    return output


def transpose(mat):
    row = len(mat)
    col = len(mat[0])
    output = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(mat[j][i])
        output.append(temp)

    return output


def partition(stream):
    bits = len(stream)
    previous = stream[0]
    temp = ""
    output = []
    for i in range(1, bits):
        if stream[i] == previous:
            temp = temp + previous
        else:
            temp = temp + previous
            output.append(temp)
            temp = ""
            previous = stream[i]
    if temp != "":
        temp = temp + previous
        output.append(temp)

    return output


def getTheSolution():
    pass


if __name__ == "__main__":
    '''
    answer = loadFile()
    average_signal = getAverageBySignal("T1")
    print(average_signal)
    average_date = getAverageByDay("03/12")
    print(average_date)
    v = [15, 23, 28, 19, 22, 29]
    broken = split(v, 2)
    print(broken)
    words = getWords("the power of this machine matches that of the one we had last year", "e")
    print(words)
    mat = [[9, 1], [1, 3], [3, 1]]
    trans = transpose(mat)
    print(trans)
    series = partition("00011110111100000100")
    print(series)
    addition = getCumulativeSum()
    print(addition)
    pallindrome = getPalindromes()
    print(pallindrome)
    print(len(pallindrome))'''