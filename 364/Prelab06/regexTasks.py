import re
from pprint import pprint as pp

def getWords(sentence, letter):
    answer = []
    pattern = r"\b\w+"
    s = re.findall(pattern, sentence)
    pattern = r"\b^"+letter+"\w*[^"+letter+"]$|\\b[^"+letter+"]\w*"+letter+"$"
    for word in s:
        p = re.findall(pattern, word, re.I)
        if p != []:
            answer.append(word)
    return answer

def extractFloats(s):
    pattern = r"-?[0-9]*\.[0-9]+\b|\+?[0-9]*\.[0-9]+\b"
    letters = re.findall(pattern, s)

    return letters

def getURLParts(url):
    answer = []
    pattern = r"(www.*?)/"
    answer = re.findall(pattern, url)
    pattern = r"/(\w*?)/"
    letters = re.findall(pattern, url)
    for letter in letters:
        if letter != "":
            answer.append(letter)
    pattern = r"/(\w*?)\?"
    letters = re.findall(pattern, url)
    for letter in letters:
        if letter != "":
            answer.append(letter)
    return tuple(answer)

def getQueryParameters(url):
    answer = []
    pattern = r"(\w*)=(\w*[\.|-]?\w*)"
    queries = re.findall(pattern, url)

    return queries

def findFunctions(filename):
    file_ptr = open(filename)
    data = file_ptr.readlines()
    queries = []
    parameters = []
    answer = []
    pattern = r"\bdef"
    for line in data:
        if re.match(pattern, line):
            queries.append(line)
    pattern_func = r"def (\w*)"
    pattern_param = r"(\w*)(,|\))"
    for line in queries:
        function = re.findall(pattern_func, line)
        param = re.findall(pattern_param, line)
        for p in param:
            parameters.append(p[0])
        answer.append((function[0], parameters))
        parameters = []

    return answer

if __name__ == "__main__":
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    answer1 = getWords(s, "t")
    print(answer1)
    s = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    answer2 = extractFloats(s)
    s = "The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts."
    answer3 = extractFloats(s)
    print(answer2)
    print(answer3)
    url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    answer4 = getURLParts(url)
    print(answer4)
    url = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    answer5 = getQueryParameters(url)
    print(answer5)
    filename = "intro.py"
    answer6 = findFunctions(filename)
    pp(answer6)
