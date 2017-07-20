import moduleTasks as mt
import glob
import os
from pprint import pprint as pp

def getFiles(name):
    filenames = glob.glob("./"+name+"/*")
    filenames.sort()
    names = []
    for name in filenames:
        name = name.split("/")
        name = (name[2].split("."))[0]
        names.append(name)
    return names

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    answer = {}
    for name in signalNames:
        try:
            v, c = mt.loadSignal(name, signalFolder)
        except ValueError:
            answer.update({name:None})
            continue
        except OSError:
            answer.update({name:None})
            continue
        if len(v) <= maxNonfloatCount:
            answer.update({name:v})
        else:
            answer.update({name:[]})

    return answer


def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):

    for key, value in signalsDictionary.items():
        if value != None and value != []:
            if mt.isSignalAcceptable(value, valueRange, maxCount):
                    try:
                        file_out = open("./"+targetFolder+"/"+key+".txt", "w")
                    except OSError:
                        os.mkdir(targetFolder)
                        file_out = open("./"+targetFolder+"/"+key+".txt", "w")
                    for num in value[:-1]:
                        file_out.write("{0:.3f}".format(num)+"\n")
                    file_out.write("{0:.3f}".format(value[-1]))

if __name__ == "__main__":
    print("-------CHECKING loadSignals---------------")
    signalNames = getFiles("Signals")
    signalNames.append("GTF-765")
    answer = loadSignals(signalNames, "Signals", 245)
    print(answer)
    print("\n\n-------CHECKING loadsignal----------------")
    saveSignals(answer, (-12, 11.7), 20, "ValidSignalsNew2")