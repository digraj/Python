import glob
from pprint import pprint as pp

def getFileNames():
    filenames = glob.glob("./Sources/*")
    filenames.sort()
    return filenames

def makeDict(filename):
    file_ptr = open(filename)
    file_data = file_ptr.readlines()
    dict = {}
    for i in range(3, len(file_data)):
        row = file_data[i].split(",")
        row[0] = row[0].strip()
        row[1] = row[1].strip()
        row[1] = row[1].lstrip("$")
        dict.update({row[0]:row[1]})
    return dict

def identifyCheapest(componentSet):
    names = getFileNames()
    dict_CDW = makeDict(names[0])
    dict_Gov = makeDict(names[1])
    dict_Tar = makeDict(names[2])
    dict_Bay = makeDict(names[3])
    price = []
    name = []
    answer_dict = {}
    for component in componentSet:
        if component in dict_CDW.keys():
            price.append(float(dict_CDW.get(component)))
            name.append("CDW")
        if component in dict_Gov.keys():
            price.append(float(dict_Gov.get(component)))
            name.append("GovConnection")
        if component in dict_Tar.keys():
            name.append("Target")
            price.append(float(dict_Tar.get(component)))
        if component in dict_Bay.keys():
            name.append("eBay")
            price.append(float(dict_Bay.get(component)))
        for i in range(len(price)):
            if price[i] == min(price):
                break
        name_ans = name[i]
        ans = (min(price), name_ans)
        answer_dict.update({component: ans})

    return answer_dict

def getAllComponents():
    names = getFileNames()
    dict = {}
    for filename in names:
        file_ptr = open(filename)
        file_data = file_ptr.readlines()
        for i in range(3, len(file_data)):
            row = file_data[i].split(",")
            row[0] = row[0].strip()
            row[1] = row[1].strip()
            row[1] = row[1].lstrip("$")
            dict.update({row[0]:row[1]})

    return dict

def getComponentsToAdd():
    names = getFileNames()
    dict_CDW = makeDict(names[0])
    dict_Gov = makeDict(names[1])
    dict_Tar = makeDict(names[2])
    dict_Bay = makeDict(names[3])
    all_components = getAllComponents()
    add_ebay = []
    add_cwd = []
    add_gov = []
    add_tar = []
    answer_dict = {}
    for key in all_components.keys():
        if key not in dict_Bay:
            add_ebay.append(key)
        if key not in dict_CDW:
            add_cwd.append(key)
        if key not in dict_Tar:
            add_tar.append(key)
        if key not in dict_Gov:
            add_gov.append(key)

    answer_dict.update({"eBay": set(add_ebay)})
    answer_dict.update({"CDW": set(add_cwd)})
    answer_dict.update({"GovConnection": set(add_gov)})
    answer_dict.update({"Target": set(add_tar)})

    return answer_dict

def transpose(mat):
    row = len(mat)
    col = len(mat[0])
    output = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(float(mat[j][i]))
        output.append(temp)

    return output

def getSummary():
    file_ptr = open("./signals.txt")
    file_data = file_ptr.readlines()
    signal_name = file_data[0].split()
    signal_name = signal_name[1:]
    full_data = []
    answer_dict = {}
    for i in range(2, len(file_data)):
        data = file_data[i].split()
        data = data[1:]
        full_data.append(data)
    full_data = transpose(full_data)
    for i in range(0, len(full_data)):
        average = sum(full_data[i])/len(full_data[i])
        maximum = max(full_data[i])
        minimum = min(full_data[i])
        answer_dict.update({signal_name[i]:(round(minimum, 3), round(average, 3), round(maximum, 3))})

    return answer_dict

def saveContinuousData(start, end, targetFileName):
    file_ptr = open("./signals.txt")
    file_data = file_ptr.readlines()
    top_2 = file_data[:2]
    start = start / 0.125
    end = end / 0.125
    needed_lined = file_data[int(start + 2):int(end + 3)]
    file_out = open(targetFileName, "w")
    for data in top_2:
        file_out.write(data)
    for data in needed_lined:
        file_out.write(data)

    return

def getSampledSignal(signalName):
    file_ptr = open("./signals.txt")
    file_data = file_ptr.readlines()
    signal_name = file_data[0].split()
    signal_name = signal_name[1:]
    answer = []
    for index in range(len(signal_name)):
        if (signalName == signal_name[index]):
            break
    full_data = []
    answer_dict = {}
    for i in range(2, len(file_data)):
        data = file_data[i].split()
        data = data[1:]
        full_data.append(data)
    full_data = transpose(full_data)
    required = full_data[index]
    for i in range(0, len(required), 8):
        answer.append(required[i])

    return answer


if __name__ == "__main__":
    answer1 = identifyCheapest({"Intel i7-4700HQ", "Intel i7-6970HQ"})
#    pp(answer1)
    answer2 = getComponentsToAdd()
#    pp(answer2)
    answer3 = getSummary()
#    pp(answer3)
    answer4 = getSampledSignal("ISO610")
#    pp(answer4)
    saveContinuousData(6.0, 7.875, "myfinalout.txt")