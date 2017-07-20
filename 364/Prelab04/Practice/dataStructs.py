import glob
from pprint import pprint as pp

def getFileNames():
    names = glob.glob("./purchases/*")
    names.sort()
    return names

def getItemDict():
    names = getFileNames()
    items_file = open(names[0])
    items = items_file.readlines()
    item_dict = {}
    for i in range(2, len(items)):
        item_row = items[i].split()
        item_row[0] = item_row[0].strip()
        item_row[1] = item_row[1].strip()
        item_row[1] = item_row[1].lstrip("$")
        item_dict.update({item_row[0]:item_row[1]})

    return item_dict

def getPurchaseReport():
    names = getFileNames()
    vegetable_dict = {}
    answer_dict = {}
    item_dict = getItemDict()
    m = 0
    for filename in names[1:]:
        file_ptr = open(filename)
        file = file_ptr.readlines()
        for i in range(2, len(file)):
            item_row = file[i].split()
            item_row[0] = item_row[0].strip()
            item_row[1] = item_row[1].strip()
            vegetable_dict.update({item_row[0]:item_row[1]})
        total_price = 0
        for key, val in vegetable_dict.items():
            price = item_dict.get(key)
            total_price = total_price + (float(price) * float(val))
        answer_dict.update({m:round(total_price, 2)})
        m = m + 1
        vegetable_dict = {}

    return answer_dict

def getTotalSold():
    names = getFileNames()
    item_dict = getItemDict()
    for key, val in item_dict.items():
        item_dict.update({key:(int(0))})
    for filename in names[1:]:
        file_ptr = open(filename)
        file = file_ptr.readlines()
        for i in range(2, len(file)):
            item_row = file[i].split()
            item_row[0] = item_row[0].strip()
            item_row[1] = item_row[1].strip()
            item_dict[item_row[0]] += int(item_row[1])
    return item_dict

if __name__ == "__main__":
    vegetable_dict = getPurchaseReport()
    sold_dict = getTotalSold()
    pp(vegetable_dict)
    print("\n")
    pp(sold_dict)