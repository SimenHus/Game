import sys


from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtGui import QCloseEvent, QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QStackedWidget


from Modules.GUI import TitleScreen, SettingsWindow, CombatWindow
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


        self.TitleScreen = TitleScreen()
        self.CombatWindow = CombatWindow()
        self.SettingsWindow = SettingsWindow()

        self.TitleScreen.startButton.pressed.connect(self.startGame)
        self.TitleScreen.exitButton.pressed.connect(self.exit)

        self.widget = QStackedWidget(self)
        self.widget.addWidget(self.TitleScreen)
        self.widget.addWidget(self.CombatWindow)
        self.widget.addWidget(self.SettingsWindow)
        self.setCentralWidget(self.widget)


    @Slot()
    def startGame(self) -> None:
        self.widget.setCurrentWidget(self.CombatWindow)

    @Slot()
    def mainMenu(self) -> None:
        self.widget.setCurrentWidget(self.TitleScreen)

    @Slot()
    def enterSettings(self) -> None:
        self.widget.setCurrentWidget(self.SettingsWindow)

    @Slot()
    def exit(self) -> None:
        self.close()

    def closeEvent(self, event: QCloseEvent) -> None:
        print('Exiting...')
        

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.isAutoRepeat(): return
        key = event.keyCombination().key()
        if key == Qt.Key.Key_Escape: self.mainMenu()

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