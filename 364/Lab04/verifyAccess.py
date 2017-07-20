import glob
from pprint import pprint as pp

def getFiles():
    filenames = glob.glob('./*.txt')
    filenames.sort()
    return filenames

def userID_Name():
    filenames = getFiles()
    access_cards_dict = {}
    access_cards_dict_2 = {}
    permissions_dict = {}
    temp = []
    file_access_cards = open(filenames[0])
    info = [0] * 2
    access_cards = file_access_cards.readlines()
    for i in range(2, len(access_cards) - 1):
        data = access_cards[i]
        info = data.split('|')
        #print(info)
        info[0] = info[0].strip()
        info[1] = info[1].strip()
        access_cards_dict.update({info[1]: info[0]})
        access_cards_dict_2.update({info[0]: info[1]})
    return access_cards_dict

def getUserPermissions():
    filenames = getFiles()
    access_cards_dict = {}
    access_cards_dict_2 = {}
    permissions_dict = {}
    temp = []
    file_access_cards = open(filenames[0])
    info = [0] * 2
    access_cards = file_access_cards.readlines()
    for i in range(2, len(access_cards) - 1):
        data = access_cards[i]
        info = data.split('|')
        #print(info)
        info[0] = info[0].strip()
        info[1] = info[1].strip()
        access_cards_dict.update({info[1]: info[0]})
        access_cards_dict_2.update({info[0]: info[1]})
#    pp(access_cards_dict_2)

    file_permissions = open(filenames[2])
    permissions = file_permissions.readlines()
    for i in range(2, len(permissions)):
        data = permissions[i]
        key, value = data.split(" - ")
        key = key.strip()
        value = value.strip()
        key_name = access_cards_dict.get(key)
        if key_name not in permissions_dict:
            permissions_dict[key_name] = []
        permissions_dict[key_name].append(value)

    for key, val in permissions_dict.items():
        val = set(val)
        permissions_dict.update({key: val})

    return permissions_dict


def getFloorPermissions():
    filenames = getFiles()
    access_cards_dict = {}
    access_cards_dict_2 = {}
    permissions_dict = {}
    temp = []
    file_access_cards = open(filenames[0])
    info = [0] * 2
    access_cards = file_access_cards.readlines()
    for i in range(2, len(access_cards) - 1):
        data = access_cards[i]
        info = data.split('|')
        #print(info)
        info[0] = info[0].strip()
        info[1] = info[1].strip()
        access_cards_dict.update({info[1]: info[0]})
        access_cards_dict_2.update({info[0]: info[1]})

    file_permissions = open(filenames[2])
    permissions = file_permissions.readlines()
    for i in range(2, len(permissions)):
        data = permissions[i]
        key, value = data.split(" - ")
        key = key.strip()
        value = value.strip()
        key_name = access_cards_dict.get(key)
        if value not in permissions_dict:
            permissions_dict[value] = []
        permissions_dict[value].append(key_name)

    for key, val in permissions_dict.items():
        val = set(val)
        permissions_dict.update({key: val})

    return permissions_dict


def getFloorRooms():
    filenames = getFiles()
    access_log_dict = {}
    access_log_dict_2 = {}
    permissions_dict = {}
    temp = []
    file_access_log = open(filenames[1])
    info = [0] * 2
    access_logs = file_access_log.readlines()
    for i in range(2, len(access_logs)):
        data = access_logs[i]
        info = data.split('-')
        info = info[-2:]
        info[0] = info[0].strip()
        info[1] = info[1].strip()
        access_log_dict.update({info[1]: info[0]})
        access_log_dict_2.update({info[0]: info[1]})
        if info[0] not in permissions_dict:
            permissions_dict[info[0]] = []
        permissions_dict[info[0]].append(info[1])
    for key, val in permissions_dict.items():
        val = set(val)
        permissions_dict.update({key: val})

    return permissions_dict

def isAccessGrantedFor(userName, attempt):
    permissions = getUserPermissions()
    if userName not in permissions:
        return False
    if attempt[0] in permissions[userName]:
        return True
    else:
        return False


def checkAttempts():
    access_cards_dict = getUserPermissions()
    access_users = userID_Name()
    filenames = getFiles()
    add_list = []
    file_log_file = open(filenames[1])
    log_file = file_log_file.readlines()
    for i in range(0, len(log_file)):
        data = log_file[i]
        info = data.split('-')
        id = info[0:5]
        id = "-".join(id)
        id = id.strip()
        key, val = info[-2:]
        key = key.strip()
        val = val.strip()
        key_name = access_users.get(id)
        if key in access_cards_dict[key_name]:
            temp = (key_name, key, val, True)
        else:
            temp = (key_name, key, val, False)
        add_list.append(temp)

    return add_list

def getAttemptsOf(userName):
    all_attempts = checkAttempts()
    answer = []
    for i in range(0, len(all_attempts)):
        name, cust, room, attempt = all_attempts[i]
        if name == userName:
            to_add = (cust, room, attempt)
            answer.append(to_add)
    return sorted(answer)


def getUserAttemptSummary():
    filenames = getFiles()
    access_cards_dict = {}
    access_cards_dict_2 = {}
    permissions_dict = {}
    answer_dict = {}
    temp = []
    names = []
    file_access_cards = open(filenames[0])
    info = [0] * 2
    access_cards = file_access_cards.readlines()
    for i in range(2, len(access_cards) - 1):
        data = access_cards[i]
        info = data.split('|')
        #print(info)
        info[0] = info[0].strip()
        names.append(info[0])
#    pp(names)
    for name in names:
        all_attempts = getAttemptsOf(name)
        true = 0
        false = 0
        for every in all_attempts:
            dc1, dc2, boolean = every
            if boolean == True:
                true = true + 1
            else:
                false = false + 1
        answer_dict.update({name: (true, false)})

    return answer_dict


def getFloorAttemptSummary():
    all_attempts = checkAttempts()
    answer_dict = {}
    rooms_bool = []
    true = 0
    false = 0
#    pp(all_attempts)
    for every in all_attempts:
        name, floor, room, boolean = every
        temp = (floor, boolean)
        rooms_bool.append(temp)
    rooms_bool = sorted(rooms_bool)
    old_name = rooms_bool[0][0]
    for name, boolean in rooms_bool:
        if (old_name == name):
            if boolean == True:
                true = true + 1
            else:
                false = false + 1
        else:
            answer_dict.update({old_name: (true, false)})
            true = 0
            false = 0
            old_name = name
            if boolean == True:
                true = true + 1
            else:
                false = false + 1

    return answer_dict




def getRoomAttemptSummary():
    pass

if __name__ == "__main__":
    answer1 = getUserPermissions()
    pp(answer1)
    answer2 = getFloorPermissions()
    pp(answer2)
    answer3 = getFloorRooms()
    pp(answer3)
    answer4 = checkAttempts()
    pp(answer4)
    answer5 = isAccessGrantedFor('Reed, Bobby', ('Equipments', 'Room46'))
    print(answer5)
    answer6 = getAttemptsOf("Gray, Tammy")
    print(answer6)
    answer7 = getUserAttemptSummary()
    pp(answer7)
    answer8 = getFloorAttemptSummary()
    pp(answer8)

