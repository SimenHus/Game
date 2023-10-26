import sys
import pathlib

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame

PATH = pathlib.Path(__file__)
RESOURCES = PATH.parent.joinpath('Resources')

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

        self.connectionStatusWidget = QLabel('Not connected')
        self.status.addWidget(self.connectionStatusWidget)


        widget = QFrame(self)
        self.setCentralWidget(widget)


    @Slot()
    def exit(self) -> None:
        print('Exiting...')
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    
    with open(f'{RESOURCES}\\styleVariables.txt', 'r') as f: varList = f.readlines()
    with open(f'{RESOURCES}\\style.qss', 'r') as f: styleSheet = f.read()
    for var in varList:
        name, value = var.split('=')
        styleSheet = styleSheet.replace(name, value)
    app.setStyleSheet(styleSheet)
    sys.exit(app.exec())