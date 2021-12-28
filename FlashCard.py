from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
import databaseCommands as DBCOM

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.WORDS = []
        self.front = ""
        self.translation = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 597)
        MainWindow.setMinimumSize(QtCore.QSize(412, 597))
        MainWindow.setMaximumSize(QtCore.QSize(412, 597))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/macbp/Desktop/FlashcardPythonPyQt5/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(10, 10, 391, 281))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(35)
        self.TextLabel.setFont(font)
        self.TextLabel.setAutoFillBackground(False)
        self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(184, 0, 180, 168);\n"
"border: 3px solid rgb(184,  0,  180);\n"
"border-radius: 20px;\n"
"")
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setWordWrap(True)
        self.TextLabel.setObjectName("TextLabel")
        self.ShowTranslation_B = QtWidgets.QPushButton(self.centralwidget)
        self.ShowTranslation_B.setGeometry(QtCore.QRect(22, 310, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(39)
        self.ShowTranslation_B.setFont(font)
        self.ShowTranslation_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowTranslation_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 0, 168);\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color: rgb(255, 103, 0)")
        self.ShowTranslation_B.setObjectName("ShowTranslation_B")
        self.right_B = QtWidgets.QPushButton(self.centralwidget)
        self.right_B.setGeometry(QtCore.QRect(210, 390, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(39)
        self.right_B.setFont(font)
        self.right_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 255, 16, 168);\n"
"border: 2px solid;\n"
"border-radius: 30px;\n"
"border-color: rgb(0, 153, 10)")
        self.right_B.setObjectName("right_B")
        self.left_B = QtWidgets.QPushButton(self.centralwidget)
        self.left_B.setGeometry(QtCore.QRect(20, 390, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(39)
        self.left_B.setFont(font)
        self.left_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 255, 16, 168);\n"
"border: 2px solid;\n"
"border-radius: 30px;\n"
"border-color: rgb(0, 153, 10)")
        self.left_B.setObjectName("left_B")
        self.Delete_B = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_B.setGeometry(QtCore.QRect(20, 490, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(39)
        self.Delete_B.setFont(font)
        self.Delete_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 0, 2, 168);\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color: rgb(128, 0, 0)")
        self.Delete_B.setObjectName("Delete_B")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 412, 24))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_Flashcard = QtWidgets.QAction(MainWindow)
        self.actionNew_Flashcard.setObjectName("actionNew_Flashcard")
        self.actionDelete_Current_Card = QtWidgets.QAction(MainWindow)
        self.actionDelete_Current_Card.setObjectName("actionDelete_Current_Card")
        self.actionDelete_All = QtWidgets.QAction(MainWindow)
        self.actionDelete_All.setObjectName("actionDelete_All")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionGo_To_Start = QtWidgets.QAction(MainWindow)
        self.actionGo_To_Start.setObjectName("actionGo_To_Start")
        self.menuFile.addAction(self.actionNew_Flashcard)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGo_To_Start)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_Current_Card)
        self.menuFile.addAction(self.actionDelete_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionClose.triggered.connect(self.exit_M)
        self.actionNew_Flashcard.triggered.connect(self.add_new_MB)
        self.right_B.clicked.connect(self.nextWord)
        self.left_B.clicked.connect(self.preWord)
        self.ShowTranslation_B.clicked.connect(self.showTranslation)
        self.actionGo_To_Start.triggered.connect(self.gotoStart)
        self.actionDelete_Current_Card.triggered.connect(self.deleteCurrent_BM)
        self.Delete_B.clicked.connect(self.deleteCurrent_BM)
        self.actionDelete_All.triggered.connect(self.deleteAll)
        self.gotoStart()

    def deleteAll(self):
        DBCOM.DELETE_ALL()
        self.gotoStart()

    def deleteCurrent_BM(self):
        card = self.front + "|" + self.translation
        DBCOM.DELETE(card)
        self.gotoStart()

    def showTranslation(self):
        text = self.TextLabel.text()
        if len(self.WORDS) == 0:
            pass
        else:
            if text == self.front:
                self.TextLabel.setText(self.translation)
                self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
    "background-color: rgba(0, 106, 255, 168);\n"
    "border: 3px solid rgb(0, 42, 102);\n"
    "border-radius: 20px;\n"
    "")
            elif text == self.translation:
                self.TextLabel.setText(self.front)
                self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
    "background-color: rgba(184, 0, 180, 168);\n"
    "border: 3px solid rgb(184,  0,  180);\n"
    "border-radius: 20px;\n"
    "")

    def preWord(self):
        try:
            index = int(self.WORDS.index(f'{self.front}|{self.translation}'))-1
            if index == -1:
                raise IndexError
            card = self.WORDS[index]
            card = card.split("|")
            self.front = card[0]
            self.translation = card[1]
            self.TextLabel.setText(self.front)
            self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(184, 0, 180, 168);\n"
"border: 3px solid rgb(184,  0,  180);\n"
"border-radius: 20px;\n"
"")
        except:
            pass

    def nextWord(self):
        try:
            card = self.WORDS[int(self.WORDS.index(f'{self.front}|{self.translation}'))+1]
            card = card.split("|")
            self.front = card[0]
            self.translation = card[1]
            self.TextLabel.setText(self.front)
            self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(184, 0, 180, 168);\n"
"border: 3px solid rgb(184,  0,  180);\n"
"border-radius: 20px;\n"
"")
        except:
            pass

    def gotoStart(self):
        self.WORDS = [i for index in DBCOM.VIEW() for i in index]
        self.WORDS.reverse()
        try:
            self.front = str(self.WORDS[0]).split("|")[0]
            self.translation = str(self.WORDS[0]).split("|")[1]
            self.TextLabel.setText(self.front)
            self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
    "background-color: rgba(184, 0, 180, 168);\n"
    "border: 3px solid rgb(184,  0,  180);\n"
    "border-radius: 20px;\n"
    "")
        except IndexError:
            self.TextLabel.setText(self.front)
            self.TextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
    "background-color: rgba(184, 0, 180, 168);\n"
    "border: 3px solid rgb(184,  0,  180);\n"
    "border-radius: 20px;\n"
    "")
            self.front = ""
            self.translation = ""

    def exit_M(self):
        from sys import exit
        exit()

    def add_new_MB(self):
        textF, okF = QInputDialog.getText(MainWindow, "New Card", "Enter The Front Side Of The Card:")
        if okF:
            textT, okT = QInputDialog.getText(MainWindow, "New Card", "Enter The Translation:")
            if okT:
                cardInfo = f"{textF}|{textT}"
                DBCOM.ADD(cardInfo)
                self.gotoStart()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashCards"))
        self.TextLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.TextLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ShowTranslation_B.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Show Translation</span></p></body></html>"))
        self.ShowTranslation_B.setText(_translate("MainWindow", "Show Translation"))
        self.right_B.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Next</span></p></body></html>"))
        self.right_B.setText(_translate("MainWindow", "==>"))
        self.left_B.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Previous</span></p></body></html>"))
        self.left_B.setText(_translate("MainWindow", "<=="))
        self.Delete_B.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Delete Current Card</span></p></body></html>"))
        self.Delete_B.setText(_translate("MainWindow", "Delete Current"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Flashcard.setText(_translate("MainWindow", "New Flashcard"))
        self.actionNew_Flashcard.setShortcut(_translate("MainWindow", "Meta+N"))
        self.actionDelete_Current_Card.setText(_translate("MainWindow", "Delete Current Card"))
        self.actionDelete_Current_Card.setShortcut(_translate("MainWindow", "Meta+Backspace"))
        self.actionDelete_All.setText(_translate("MainWindow", "Delete All"))
        self.actionDelete_All.setShortcut(_translate("MainWindow", "Meta+Shift+Backspace"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Meta+Q"))
        self.actionGo_To_Start.setText(_translate("MainWindow", "Go To Start"))
        self.actionGo_To_Start.setShortcut(_translate("MainWindow", "Meta+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
