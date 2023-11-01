from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QPushButton, QGraphicsScene, QGraphicsView)


class MainMenu(QGraphicsView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setScene(QGraphicsScene(self))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.startButton = QPushButton('Start')
        self.settingsButton = QPushButton('Settings')
        self.exitButton = QPushButton('Exit')


        item = self.scene().addWidget(self.startButton)
        # self.scene().addWidget(self.settingsButton)
        # self.scene().addWidget(self.exitButton)