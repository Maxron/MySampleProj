from app.domain.sayHelloUseCase import SayHello
from app.demo import Demo
from PyQt5.QtWidgets import QApplication, QMainWindow
from app.ui import mainwindow
import sys


def runUseCase():
    print("Hello world")
    hello = SayHello("Wei")
    hello.hello()

def runDemo():
    demo = Demo()
    demo.runDemo()


def runGUI():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def main():
    runDemo()
    runUseCase()
    runGUI()

if __name__ == '__main__':
    main()
