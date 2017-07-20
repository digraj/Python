import glob
import re
from pprint import pprint as pp

def getFileNames(name):
    filenames = glob.glob("./"+name+"/*")
    filenames.sort()
    return filenames

def isNameValid(signalName):
    pattern = r"^([A-Z]{3})(\-)([0-9]{3})$"
    if re.match(pattern, signalName):
        return True
    return False

def loadSignal(signalName, signalFolder):
    names = []
    if not isNameValid(signalName):
        raise ValueError(signalName+" is not valid")
    filenames = getFileNames(signalFolder)

    for name in filenames:
        name = name.split("/")
        name = (name[2].split("."))[0]
        names.append(name)

    if signalName not in names:
        raise OSError(signalName+".txt does not exist in the "+signalFolder+" folder.")

    file_ptr = open("./"+signalFolder+"/"+signalName+".txt")
    data = file_ptr.readlines()
    c = 0
    answer = []
    for value in data:
        value = value.rstrip()
        try:
            float(value)
            answer.append(float(value))
        except:
            c += 1

    return (answer, c)

def isSignalAcceptable(signal, valueRange, maxCount):
    maximum = valueRange[1]
    minimum = valueRange[0]
    invalid = 0
    if signal == []:
        raise ValueError("Signal contains no data.")
    for data in signal:
        if not data <= maximum and data >= minimum:
            invalid += 1
    if invalid <= maxCount:
        return True
    return False


if __name__ == "__main__":
    print("-------CHECKING isNameValid---------------")
    answer = isNameValid("AFE-667")
    print(answer)
    print("\n\n-------CHECKING loadsignal----------------")
    v, c = loadSignal("REY-386", "Signals")
    print(len(v), c)
    print("\n\n-------CHECKING isSignalAcceptable--------")
    z = []
    answer = isSignalAcceptable(v, (-12, 11.7), 20)
    print(answer)