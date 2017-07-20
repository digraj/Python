# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *
#
class myCalc(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(myCalc, self).__init__(parent)
        self.setupUi(self)
        #My Created variables
        self.num = ""
        self.operator = ""
        self.numList = [0, 0]
        self.currAnswer = 0


        self.numbers = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btnDot]
        self.operations = [self.btnMultiply, self.btnMinus, self.btnPlus, self.btnDivide, self.btnEqual, self.btnClear]
        self.display = self.txtDisplay

        self.btnPlus.clicked.connect(self.addition)
        self.btnMinus.clicked.connect(self.subtraction)
        self.btnDivide.clicked.connect(self.division)
        self.btnMultiply.clicked.connect(self.multiplication)
        self.btnEqual.clicked.connect(self.equalTo)
        self.btnClear.clicked.connect(self.clearAll)
        self.btnClear.clicked.connect(self.clearAll)
        self.cboDecimal.currentIndexChanged.connect(self.decimalDisplay)
        if self.chkSeparator.isChecked():
            self.thDivider()
        self.chkSeparator.stateChanged.connect(self.thDivider)

        for number in self.numbers:
            number.clicked.connect(self.makeNum)

    def thDivider(self):
        display = self.currAnswer
        if self.cboDecimal.currentText() == "0":
            temp = "{0:.0f}".format(display)
        else:
            if self.chkSeparator.isChecked():
                temp = "{0:,.{1}f}".format(display, int(self.cboDecimal.currentText()))
            else:
                temp = "{0:.{1}f}".format(display, int(self.cboDecimal.currentText()))
        self.display.setText(str(temp))


    def decimalDisplay(self):
        display = self.currAnswer
        if self.cboDecimal.currentText() == "0":
            temp = "{0:.0f}".format(display)
        else:
            if self.chkSeparator.isChecked():
                temp = "{0:,.{1}f}".format(display, int(self.cboDecimal.currentText()))
            else:
                temp = "{0:.{1}f}".format(display, int(self.cboDecimal.currentText()))
        self.display.setText(str(temp))



    def clearAll(self):
        self.num = ""
        self.operator = ""
        self.numList = [0, 0]
        self.currAnswer = 0.0
        self.display.setText("0.")

    def equalTo(self):
        if (self.operator) == "+":
            self.currAnswer = self.numList[0] + float(self.num)
        if (self.operator) == "-":
            self.currAnswer = self.numList[0] - float(self.num)
        if (self.operator) == "/":
            self.currAnswer = self.numList[0] / float(self.num)
        if (self.operator) == "*":
            self.currAnswer = self.numList[0] * float(self.num)
        self.addNumToList()
        self.num = ""
        print("Current Answer")
        print(self.currAnswer)
        self.numList = [0, 0]
        self.num = self.currAnswer
        self.thDivider()

    def finishPrev(self, operation):
        if (self.operator) == "+":
            self.currAnswer = self.numList[0] + float(self.num)
        elif (self.operator) == "-":
            self.currAnswer = self.numList[0] - float(self.num)
        elif (self.operator) == "/":
            self.currAnswer = self.numList[0] / float(self.num)
        elif (self.operator) == "*":
            self.currAnswer = self.numList[0] * float(self.num)
        elif operation == "+":
            self.currAnswer = self.numList[0] + float(self.num)
        elif operation == "-":
            self.currAnswer = self.numList[0] + float(self.num)
        elif operation == "/":
            self.currAnswer = self.numList[0] + float(self.num)
        elif operation == "*":
            self.currAnswer = self.numList[0] + float(self.num)

    def addition(self):
        print("-----Addition-----")
        self.finishPrev("+")
        self.operator = "+"
        self.num = str(self.currAnswer)
        self.addNumToList()
        self.num = ""

    def subtraction(self):
        print("-----Subtraction-----")
        self.finishPrev("-")
        self.operator = "-"
        self.num = str(self.currAnswer)
        self.addNumToList()
        self.num = ""

    def division(self):
        print("-----Division-----")
        self.finishPrev("/")
        self.operator = "/"
        self.num = str(self.currAnswer)
        self.addNumToList()
        self.num = ""

    def multiplication(self):
        self.finishPrev("*")
        self.operator = "*"
        self.num = str(self.currAnswer)
        self.addNumToList()
        self.num = ""

    def addNumToList(self):
        currentOut = self.numList[0]
        self.numList[0] = (float(self.num))
        self.displayCurrent()
        self.numList[1] = (float(currentOut))

        print("Current List")
        print(self.numList)

    def displayCurrent(self):
        display = float(self.num)
        if self.cboDecimal.currentText() == "0":
            temp = "{0:.0f}".format(display)
        else:
            if self.chkSeparator.isChecked():
                temp = "{0:,.{1}f}".format(display, int(self.cboDecimal.currentText()))
            else:
                temp = "{0:.{1}f}".format(display, int(self.cboDecimal.currentText()))
        self.display.setText(str(temp))

    def makeNum(self):
        button = self.sender()
        self.num = self.num + button.text()
        print(self.num)
        self.display.setText(self.num)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = myCalc()
    currentForm.show()
    currentApp.exec_()
