
from pprint import pprint as pp

class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNumber = experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCost = unitCost
        self.unitCount = unitCount
        self.totalCost = unitCost * unitCount


    def __str__(self):
        my_str = ("{0:03d}" + ", " + str(self.experimentDate) + ", $" + "{1:06.2f}" + ": " + str(self.virusName)).format(self.experimentNumber, self.totalCost)
        return my_str

class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def __str__(self):
        my_str = str(self.techID) + ", " + str(self.techName) + ": " + "{0:02d}".format(len(self.experiments)) + " Experiments"
        return my_str

    def addExperiment(self, experiment):
        self.experiments[experiment.experimentNumber] = experiment

    def getExperiment(self, expNo):
        return self.experiments.get(expNo)

    def loadExperimentsFromFile(self, fileName):
        file_ptr = open(fileName, "r")
        data = file_ptr.readlines()
        for i in range(2, len(data)):
            my_data = data[i].split()
            myExp = Experiment(int(my_data[0]), my_data[1], my_data[2], int(my_data[3]), float(my_data[4].lstrip("$")))
            self.addExperiment(myExp)

    def generateTechActivity(self):
        name = self.techName
        id = self.techID
        my_str = id + ", " + name
        answer = []
        for key, value in self.experiments.items():
            answer.append(str(value))
        answer.sort()
        for item in answer:
            my_str = my_str + "\n" + item

        return my_str

class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}

    def __str__(self):
        my_str = self.labName + ": " + "{0:02d}".format(len(self.technicians)) + " Technicians"
        num = []
        for key, value in self.technicians.items():
            num.append(str(value))
        num.sort()

        for item in num:
            my_str = my_str + "\n" + item
        return my_str

    def addTechnician(self, technician):
        self.technicians[technician.techName] = technician

    def getTechnicians(self, *args):
        answer = []
        for name in args:
            if name in self.technicians:
                answer.append(name)

        return answer

    def generateLabActivity(self):
        my_str = ""
        answer = []
        keys = []
        values = []
        for key in sorted(list(self.technicians.keys())):
            values = self.technicians[key]
            my_str = my_str + values.generateTechActivity() + "\n\n"
        my_str.strip()
        return my_str[:-2]


if __name__ == "__main__":
    x = Experiment(31, "04/01/2015", "Alphatorquevirus", 09.0, 10.0)
    y = Technician("Digraj", "69069-29232")
    y.loadExperimentsFromFile("report 75471-28954.txt")
    activity = y.generateTechActivity()
    print(activity)
    z = Laboratory("Digraj")
    z.addTechnician(y)
    z.generateLabActivity()
    print(z.generateLabActivity())