
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(0, 0, 821, 611))
        self.BG.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.BG.setObjectName("BG")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(529, 528, 121, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid white;")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(529, 442, 251, 61))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid white;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.GIF = QtWidgets.QLabel(self.centralwidget)
        self.GIF.setGeometry(QtCore.QRect(520, 190, 301, 251))
        self.GIF.setText("")
        self.GIF.setPixmap(QtGui.QPixmap("G.U.I Material\ExtraGui\Earth.gif"))
        self.GIF.setScaledContents(True)
        self.GIF.setObjectName("GIF")
        self.GIF_2 = QtWidgets.QLabel(self.centralwidget)
        self.GIF_2.setGeometry(QtCore.QRect(0, -42, 401, 191))
        self.GIF_2.setText("")
        self.GIF_2.setPixmap(QtGui.QPixmap("G.U.I Material\ExtraGui\initial.gif"))
        self.GIF_2.setScaledContents(True)
        self.GIF_2.setObjectName("GIF_2")
        self.GIF_3 = QtWidgets.QLabel(self.centralwidget)
        self.GIF_3.setGeometry(QtCore.QRect(10, 113, 341, 311))
        self.GIF_3.setStyleSheet("border: 1px solid white;")
        self.GIF_3.setText("")
        self.GIF_3.setPixmap(QtGui.QPixmap("G.U.I Material\B.G\Iron_Template_1.gif"))
        self.GIF_3.setScaledContents(True)
        self.GIF_3.setObjectName("GIF_3")
        self.GIF_4 = QtWidgets.QLabel(self.centralwidget)
        self.GIF_4.setGeometry(QtCore.QRect(486, 30, 281, 141))
        self.GIF_4.setStyleSheet("border: 1px solid white;")
        self.GIF_4.setText("")
        self.GIF_4.setPixmap(QtGui.QPixmap("G.U.I Material\ExtraGui\Health_Template.gif"))
        self.GIF_4.setScaledContents(True)
        self.GIF_4.setObjectName("GIF_4")
        self.terminal = QtWidgets.QLabel(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(9, 434, 511, 151))
        self.terminal.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.terminal.setText("")
        self.terminal.setObjectName("terminal")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 528, 121, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid white;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BG.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

