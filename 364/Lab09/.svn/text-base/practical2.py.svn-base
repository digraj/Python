import re
from pprint import pprint as pp

def getNumericData(sentence):
    pattern = r"\-?\+?[0-9]+[\.a-zA-Z0-9]+\+?\-?[0-9]*"
    matches = re.findall(pattern, s)
    for i in range(len(matches)):
        if matches[i][-1] == ".":
            matches[i] = matches[i][:-1]

    return matches


def parseSimple(fileName):
    file_ptr = open(fileName)
    data = file_ptr.readlines()
    data = data[1:-1]
    answer_dict = {}
    pattern = r"\"([\w|\s|\.|,|#|-]*)\""
    for item in data:
        matches = re.findall(pattern, item)
        answer_dict.update({str(matches[0]):str(matches[1])})

    return answer_dict

def parseLine(fileName):
    file_ptr = open(fileName)
    answer_dict = {}
    data = file_ptr.readlines()
    pattern = r"\"([\w|\s|\.|,|#|-]*)\""
    matches = re.findall(pattern, data[0])
    i = 0
    while i < len(matches) - 1:
        answer_dict.update({str(matches[i]):str(matches[i+1])})
        i += 2
    return answer_dict

def parseComplex(fileName):
    file_ptr = open(fileName)
    data = file_ptr.readlines()
    data = data[1:-1]
    answer_dict = {}
    match = []
    pattern = r"\"?([\w|\.|-]+)\"?"
    for item in data:
        matches = re.findall(pattern, item)
        if isinstance(matches[1], int):
            answer_dict.update({matches[0]:int(matches[1])})
        elif isinstance(matches[1], bool):
            answer_dict.update({matches[0]:bool(matches[1])})
        else:
            answer_dict.update({matches[0]:(matches[1])})

    return answer_dict

def parseComposite(fileName):
    pass

if __name__ == "__main__":
    s = "With the electron's -1.6022e-19 some choices -110, -32.0 and +55. Assume 3.1415 and 2.7 Na is +6.0221E+023."
    answer1 = getNumericData(s)
    # print("TESTING getNumericData")
    # print(answer1)
    answer2 = parseSimple("simple.json")
    # pp(answer2)
    answer3 = parseLine("simple2.json")
    pp(answer2)
    pp(answer3)
    answer4 = parseComplex("complex.json")
    pp(answer4)
