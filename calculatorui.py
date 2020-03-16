#  Author: Jimi Österholm
#  File: calculatorui.py
#  Description: A basic calculator GUI and functionality

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qdarkstyle
import pyttsx3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Create a new main window for calculator
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(263, 291)

        # Setup buttons and button locations for calculator
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.number1 = QtWidgets.QPushButton(self.centralwidget)
        self.number1.setGeometry(QtCore.QRect(20, 80, 31, 23))
        self.number1.setObjectName("number1")
        self.number2 = QtWidgets.QPushButton(self.centralwidget)
        self.number2.setGeometry(QtCore.QRect(70, 80, 31, 23))
        self.number2.setObjectName("number2")
        self.number3 = QtWidgets.QPushButton(self.centralwidget)
        self.number3.setGeometry(QtCore.QRect(120, 80, 31, 23))
        self.number3.setObjectName("number3")
        self.number6 = QtWidgets.QPushButton(self.centralwidget)
        self.number6.setGeometry(QtCore.QRect(120, 120, 31, 23))
        self.number6.setObjectName("number6")
        self.number4 = QtWidgets.QPushButton(self.centralwidget)
        self.number4.setGeometry(QtCore.QRect(20, 120, 31, 23))
        self.number4.setObjectName("number4")
        self.number5 = QtWidgets.QPushButton(self.centralwidget)
        self.number5.setGeometry(QtCore.QRect(70, 120, 31, 23))
        self.number5.setObjectName("number5")
        self.number9 = QtWidgets.QPushButton(self.centralwidget)
        self.number9.setGeometry(QtCore.QRect(120, 160, 31, 23))
        self.number9.setObjectName("number9")
        self.number7 = QtWidgets.QPushButton(self.centralwidget)
        self.number7.setGeometry(QtCore.QRect(20, 160, 31, 23))
        self.number7.setObjectName("number7")
        self.number8 = QtWidgets.QPushButton(self.centralwidget)
        self.number8.setGeometry(QtCore.QRect(70, 160, 31, 23))
        self.number8.setObjectName("number8")
        self.equals = QtWidgets.QPushButton(self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(120, 200, 31, 23))
        self.equals.setObjectName("equals")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(20, 200, 31, 23))
        self.dot.setObjectName("dot")
        self.creset = QtWidgets.QPushButton(self.centralwidget)
        self.creset.setGeometry(QtCore.QRect(70, 240, 31, 23))
        self.creset.setObjectName("creset")
        self.oBracket = QtWidgets.QPushButton(self.centralwidget)
        self.oBracket.setGeometry(QtCore.QRect(20, 240, 31, 23))
        self.oBracket.setObjectName("oBracket")
        self.cBracket = QtWidgets.QPushButton(self.centralwidget)
        self.cBracket.setGeometry(QtCore.QRect(120, 240, 31, 23))
        self.cBracket.setObjectName("cBracket")
        self.number0 = QtWidgets.QPushButton(self.centralwidget)
        self.number0.setGeometry(QtCore.QRect(70, 200, 31, 23))
        self.number0.setObjectName("number0")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(210, 80, 31, 23))
        self.plus.setObjectName("plus")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(210, 160, 31, 23))
        self.divide.setObjectName("divide")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(210, 120, 31, 23))
        self.minus.setObjectName("minus")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(210, 200, 31, 23))
        self.multiply.setObjectName("multiply")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(210, 240, 31, 23))
        self.exit.setObjectName("exit")
        self.text = QtWidgets.QTextBrowser(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(20, 10, 190, 62))
        self.text.setObjectName("text")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(210, 10, 31, 31))
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button click event setup
        self.number0.clicked.connect(lambda: self.screenInput('0'))
        self.number1.clicked.connect(lambda: self.screenInput('1'))
        self.number2.clicked.connect(lambda: self.screenInput('2'))
        self.number3.clicked.connect(lambda: self.screenInput('3'))
        self.number4.clicked.connect(lambda: self.screenInput('4'))
        self.number5.clicked.connect(lambda: self.screenInput('5'))
        self.number6.clicked.connect(lambda: self.screenInput('6'))
        self.number7.clicked.connect(lambda: self.screenInput('7'))
        self.number8.clicked.connect(lambda: self.screenInput('8'))
        self.number9.clicked.connect(lambda: self.screenInput('9'))
        self.dot.clicked.connect(lambda: self.screenInput('.'))
        self.plus.clicked.connect(lambda: self.screenInput(" + "))
        self.minus.clicked.connect(lambda: self.screenInput(" - "))
        self.multiply.clicked.connect(lambda: self.screenInput(" * "))
        self.divide.clicked.connect(lambda: self.screenInput(" / "))
        self.equals.clicked.connect(lambda: self.calculate())
        self.exit.clicked.connect(lambda: sys.exit())
        self.creset.clicked.connect(lambda: self.text.clear())
        self.oBracket.clicked.connect(lambda: self.screenInput("("))
        self.cBracket.clicked.connect(lambda: self.screenInput(")"))
        self.back.clicked.connect(lambda: self.backspace())

        # Setting shortcuts for buttons
        self.number0.setShortcut("0")
        self.number1.setShortcut("1")
        self.number2.setShortcut("2")
        self.number3.setShortcut("3")
        self.number4.setShortcut("4")
        self.number5.setShortcut("5")
        self.number6.setShortcut("6")
        self.number7.setShortcut("7")
        self.number8.setShortcut("8")
        self.number9.setShortcut("9")
        self.equals.setShortcut("RETURN")
        self.oBracket.setShortcut("(")
        self.cBracket.setShortcut(")")
        self.plus.setShortcut("+")
        self.minus.setShortcut("-")
        self.multiply.setShortcut("*")
        self.divide.setShortcut("/")
        self.creset.setShortcut("SPACE")
        self.dot.setShortcut(".")
        self.exit.setShortcut("ESC")
        self.back.setShortcut("BACKSPACE")


    def retranslateUi(self, MainWindow):
        # Set the text inside the buttons and the main window title
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CALCULATOR"))
        self.number1.setText(_translate("MainWindow", "1"))
        self.number2.setText(_translate("MainWindow", "2"))
        self.number3.setText(_translate("MainWindow", "3"))
        self.number6.setText(_translate("MainWindow", "6"))
        self.number4.setText(_translate("MainWindow", "4"))
        self.number5.setText(_translate("MainWindow", "5"))
        self.number9.setText(_translate("MainWindow", "9"))
        self.number7.setText(_translate("MainWindow", "7"))
        self.number8.setText(_translate("MainWindow", "8"))
        self.equals.setText(_translate("MainWindow", "="))
        self.dot.setText(_translate("MainWindow", "."))
        self.number0.setText(_translate("MainWindow", "0"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.creset.setText(_translate("MainWindow", "C"))
        self.oBracket.setText(_translate("MainWindow", "("))
        self.cBracket.setText(_translate("MainWindow", ")"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.back.setText(_translate("MainWindow", "<<"))

    # Function to input selected button to the text screen
    # If input throws an error, print ERROR on screen
    def screenInput(self, value):
        try:
            temp = str(self.text.toPlainText())
            if temp == "ERROR":
                self.text.clear()
            self.text.insertPlainText(value)
        except:
            self.text.clear()
            self.text.insertPlainText("ERROR")

    # Function to calculate the inputted string on the text screen
    # If function throws an exception, print ERROR on screen  
    def calculate(self):
        try:
            temp = str(self.text.toPlainText())
            if temp == "ERROR":
                self.text.clear()
            calculation = str(eval(self.text.toPlainText()))
            self.engine = pyttsx3.init()
            if calculation == str(self.text.toPlainText()):
                self.engine.say("You did not calculate anything.")
                self.engine.runAndWait()
            else:
                self.engine.say(str(self.text.toPlainText()) + " = " + str(calculation))
                self.engine.runAndWait()
            self.text.clear()
            self.text.insertPlainText(calculation)
        except:
            self.text.clear()
            self.text.insertPlainText("ERROR")
            self.engine = pyttsx3.init()
            self.engine.say("ERROR")
            self.engine.runAndWait()
    # Function to remove a character from the text screen.
    def backspace(self):
        temp = self.text.toPlainText()
        temp = temp[:-1]
        self.text.clear()
        self.text.insertPlainText(temp)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
