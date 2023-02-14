from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
from sys import argv, exit
import Main
from Tom_GUI.TomUi import Ui_MainWindow


class MainThread(QThread):

    def __init__(self):

        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.TaskExe()


startFunctions = MainThread()


class Gui_run(QMainWindow):

    def __init__(self):

        super().__init__()

        self.Tom_ui = Ui_MainWindow()

        self.Tom_ui.setupUi(self)

        self.Tom_ui.pushButton.clicked.connect(self.startFunc)

        self.Tom_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.Tom_ui.movies = QtGui.QMovie(
            "G.U.I Material\ExtraGui\Earth.gif")

        self.Tom_ui.GIF.setMovie(self.Tom_ui.movies)

        self.Tom_ui.movies.start()

        self.Tom_ui.movies_2 = QtGui.QMovie(
            "G.U.I Material\ExtraGui\initial.gif")

        self.Tom_ui.GIF_2.setMovie(self.Tom_ui.movies_2)

        self.Tom_ui.movies_2.start()

        self.Tom_ui.movies_3 = QtGui.QMovie(
            "G.U.I Material\B.G\Iron_Template_1.gif")

        self.Tom_ui.GIF_3.setMovie(self.Tom_ui.movies_3)

        self.Tom_ui.movies_3.start()

        self.Tom_ui.movies_4 = QtGui.QMovie(
            "G.U.I Material\ExtraGui\Health_Template.gif")

        self.Tom_ui.GIF_4.setMovie(self.Tom_ui.movies_4)

        self.Tom_ui.movies_4.start()

        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):

        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time

        self.Tom_ui.textBrowser.setText(labbel)


def main():
    Gui_App = QApplication(argv)

    Gui_Tom = Gui_run()

    Gui_Tom.show()

    exit(Gui_App.exec_())


if __name__ == "__main__":
    main()
