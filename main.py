import sys


from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget


from Combat.layout import CombatWindow
from common import *


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client side application")
        self.setGeometry(0, 0, 800, 500)

        # Main menu bar
        self.menu = self.menuBar()
        menu_file = self.menu.addMenu("File")
        menu_about = self.menu.addMenu("&About")

        exit = menu_file.addAction('Exit')
        exit.triggered.connect(self.exit)

        about = menu_about.addAction("About Qt")
        about.triggered.connect(qApp.aboutQt)

        # Status bar
        self.status = self.statusBar()

        self.connectionStatusWidget = QLabel('This is a status bar')
        self.status.addWidget(self.connectionStatusWidget)


        widget = CombatWindow(self)
        self.setCentralWidget(widget)


    @Slot()
    def exit(self) -> None:
        print('Exiting...')
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    
    with open(STYLEVAR, 'r') as f: varList = f.readlines()
    with open(STYLE, 'r') as f: styleSheet = f.read()
    for var in varList:
        name, value = var.split('=')
        styleSheet = styleSheet.replace(name, value)
    app.setStyleSheet(styleSheet)
    sys.exit(app.exec())