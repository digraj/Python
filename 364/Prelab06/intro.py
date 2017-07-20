#! /usr/bin/env python3.4

def      getMaxProduct(l1):
    out = [0] * (len(l1) - 1)
    for I in (range(len(l1) - 2)):
        out[I] = l1[I] * l1[I+1] * l1[I+2]
    answer = max(out)

    return answer

def getMaxOccurrence(l1):
    temp = [0] * (max(l1) + 1)
    for I in range(len(l1)):
        temp[l1[I]] += 1
    maximum = max(temp)
    answer = temp.index(maximum)
    return answer

def 1removeDuplicates(l1):
    out = []
    for I in range(len(l1)):
        if not l1[I] in out:
            out.append(l1[I])
    return out

def getElementwiseSum(l1, 1l2):
    size1 = len(l1)
    size2 = len(l2)
    if size1 > size2:
        out = l1
        for I in range(size2):
            out[I] = l1[I] + l2[I]
    else:
        out = l2
        for I in range(size2):
            out[I] = l1[I] + l2[I]

    return out


def getColumnSum(mat):
    row = len(mat)
    col = len(mat[0])
    sum = [0] * col
    for I in range(row):
        for J in range(col):
            sum[J] = mat[I][J] + sum[J]
    return sum

def getFormattedNames(ln):
    answer = []
    for temp in ln:
        name = temp[2]+", "+temp[0]+" "+temp[1]+"."
        answer.append(name)
    return answer

def findName(l, s):
    for name in l:
        broken = name.split(" ")
        if s in broken:
            return name

def getFormattedSSN(ssn):
    temp_1 = ssn % 10000
    ssn = (ssn - temp_1) / 10000
    temp_2 = ssn % 100
    ssn = (ssn - temp_2) / 100
    temp_3 = ssn % 1000
    ssn = (ssn - temp_3) / 1000
    formatted = str(int(temp_3)).zfill(3)+"-"+str(int(temp_2)).zfill(2)+"-"+str(int(temp_1)).zfill(4)

    return formatted

def getNumberAverage(l):
    counter = 0
    sum = 0
    for data in l:
        if (isinstance(data, int) or isinstance(data, float)) and not isinstance(data, bool):
            sum += data
            counter += 1
    answer = sum / counter
    return answer


def getTailMax(l, m):
    new_l = l[-m:]
    new_l.sort()
    max_num = new_l[-1]
    return max_num

def getHeadAverage(l, n):
    average = sum(l[:n])/len(l[:n])
    return average

if __name__ == "__main__":
    print("\n\n")
    print("1.  Testing Function getHeadAverage")
    print("---------------------------------------------")
    l = [2, 3, 4, 5, 6, 7, 8]
    n = 4
    answer1 = getHeadAverage(l, n)
    print("Answer = ", answer1, "\n\n")


    print("2.  Testing Function getTailMax")
    print("---------------------------------------------")
    l = [2, 3, 8, 5, 6, 7, 8]
    m = 3
    answer2 = getTailMax(l, m)
    print("Answer = ", answer2, "\n\n")

    print("3.  Testing Function getNumberAverage")
    print("---------------------------------------------")
    l = [2, 1.001, 4.5739, "hi", True, False]
    answer3 = getNumberAverage(l)
    print("Answer = ", answer3, "\n\n")

    print("4.  Testing Function getFormattedSSN")
    print("---------------------------------------------")
    ssn = 5
    answer4 = getFormattedSSN(ssn)
    print("Answer = ", answer4, "\n\n")


    print("5.  Testing Function findName")
    print("---------------------------------------------")
    l = ["George Smith", "Mark Johnson", "Digraj Jain", "Apoorv Sharma"]
    s = "Jain"
    answer5 = findName(l, s)
    print("Answer = ", answer5, "\n\n")

    print("6.  Testing Function getColumnSum")
    print("---------------------------------------------")
    mat = [[4.5, 3.2, 1.1], [2.0, 696, 13.0], [7, 3.1, 9.0], [0.2, 121, 888]]
    answer6 = getColumnSum(mat)
    print("Answer = ", answer6, "\n\n")

    print("7.  Testing Function getFormattedNames")
    print("---------------------------------------------")
    ln = [["George", "W", "Bush"], ["Kunwar Digraj", "S", "Jain"]]
    answer7 = getFormattedNames(ln)
    print("Answer = ", answer7, "\n\n")

    print("8.  Testing Function getElementwiseSum")
    print("---------------------------------------------")
    l1 = [1, 3, 5, 7, 9, 11]
    l2 = [6, 4, 2]
    answer8 = getElementwiseSum(l1, l2)
    print("Answer = ", answer8, "\n\n")

    print("9.  Testing Function removeDuplicates")
    print("---------------------------------------------")
    l1 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    answer9 = removeDuplicates(l1)
    print("Answer = ", answer9, "\n\n")

    print("10. Testing Function getMaxOccurrence")
    print("---------------------------------------------")
    l1 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 1, 2, 1, 1, 1, 1, 1, 13, 2]
    answer10 = getMaxOccurrence(l1)
    print("Answer = ", answer10, "\n\n")

    print("11. Testing Function getMaxProduct")
    print("---------------------------------------------")
    l1 = [3, 7, -2, 2, 3, 5]
    answer11 = getMaxProduct(l1)
    print("Answer = ", answer11, "\n\n")
