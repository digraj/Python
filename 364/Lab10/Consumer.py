import sys

from PySide.QtGui import *
from BasicUI import *
from pprint import pprint as pp

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)
        self.Componentname = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4, self.txtComponentName_5]
        self.Componentname += [self.txtComponentName_6, self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9, self.txtComponentName_10]
        self.Componentname += [self.txtComponentName_11, self.txtComponentName_12, self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15]
        self.Componentname += [self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18, self.txtComponentName_19, self.txtComponentName_20]

        self.Componentcount = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4, self.txtComponentCount_5]
        self.Componentcount += [self.txtComponentCount_6, self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9, self.txtComponentCount_10]
        self.Componentcount += [self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15]
        self.Componentcount += [self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19, self.txtComponentCount_20]

        self.btnClear.clicked.connect(self.clearAll)

        self.chkGraduate.stateChanged.connect(self.enableSave)
        self.cboCollege.currentIndexChanged.connect(self.enableSave)
        self.txtStudentName.textChanged.connect(self.enableSave)
        self.txtStudentID.textChanged.connect(self.enableSave)

        for component in self.Componentname:
            component.textChanged.connect(self.enableSave)
        for count in self.Componentcount:
            count.textChanged.connect(self.enableSave)

        self.btnSave.clicked.connect(self.saveData)
        self.btnLoad.clicked.connect(self.loadData)


    def saveData(self):
        components = []
        counts = []
        for i in range(20):
            component = self.Componentname[i].text()
            count = self.Componentcount[i].text()
            if component == "" or count == "":
                pass
            else:
                components.append(component)
                counts.append(count)
        self.id = self.txtStudentID.text()
        self.name = self.txtStudentName.text()
        self.graduate = self.chkGraduate.isChecked()
        self.college = self.cboCollege.currentText()

        file_ptr = open("target.xml", "w")
        file_ptr.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Content>\n")
        if self.graduate:
            file_ptr.write("    <StudentName graduate=\"true\">" + self.name + "</StudentName>\n")
        else:
            file_ptr.write("    <StudentName graduate=\"false\">" + self.name + "</StudentName>\n")
        file_ptr.write("    <StudentID>" + self.id + "</StudentID>\n")
        file_ptr.write("    <College>" + self.college + "</College>\n")
        file_ptr.write("    <Components>\n")
        for i in range(len(components)):
            component = components[i]
            count = counts[i]
            file_ptr.write("        <Component name=\"" + component + "\" count=\"" + count + "\" />\n")
        file_ptr.write("    </Components>\n")
        file_ptr.write("</Content>")

    def enableSave(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setDisabled(True)

    def clearAll(self):
        self.txtStudentName.setText("")
        self.txtStudentID.setText("")
        self.chkGraduate.setChecked(False)
        for component in self.Componentname:
            component.setText("")
        for count in self.Componentcount:
            count.setText("")
        self.cboCollege.setCurrentIndex(0)
        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        file_ptr = open(filePath, "r")
        data = file_ptr.readlines()
        name = data[2].split(">")
        graduate = name[0].split("\"")
        graduate = graduate[1]
        name = name[1].split("<")
        name = name[0]
        userid = data[3].split(">")
        userid = userid[1].split("<")
        userid = userid[0]
        college = data[4].split(">")
        college = college[1].split("<")
        college = college[0]
        components = []
        counts = []
        for i in range(6, len(data) - 2):
            component = data[i].split("\"")
            count = component[3]
            component = component[1]
            components.append(component)
            counts.append(count)

        for i in range(0, 20):
            if i < len(components):
                self.Componentname[i].setText(components[i])
                self.Componentcount[i].setText(counts[i])

        self.txtStudentName.setText(name)
        self.txtStudentID.setText(userid)
        if graduate == "true":
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)

        index_rcv = self.cboCollege.findText(college)
        self.cboCollege.setCurrentIndex(index_rcv)
        self.btnSave.setDisabled(False)
        self.btnLoad.setEnabled(False)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="PNG files (*.png)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
