from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QPushButton, QGraphicsScene, QGraphicsView)
from PySide6.QtGui import QPixmap

from common import *


class SettingsWindow(QGraphicsView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setScene(QGraphicsScene(self))

        self.startButton = QPushButton('Start')
        self.settingsButton = QPushButton('Settings')
        self.exitButton = QPushButton('Exit')

        sceneStartButton = self.scene().addWidget(self.startButton)
        sceneSettingsButton = self.scene().addWidget(self.settingsButton)
        sceneExitButton = self.scene().addWidget(self.exitButton)

        vertDist = 40
        sceneStartButton.setPos(0, -vertDist)
        sceneSettingsButton.setPos(0, 0)
        sceneExitButton.setPos(0, vertDist)


class TitleScreen(QGraphicsView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setScene(QGraphicsScene(self))

        self.startButton = QPushButton('Start')
        self.settingsButton = QPushButton('Settings')
        self.exitButton = QPushButton('Exit')

        sceneStartButton = self.scene().addWidget(self.startButton)
        sceneSettingsButton = self.scene().addWidget(self.settingsButton)
        sceneExitButton = self.scene().addWidget(self.exitButton)

        vertDist = 40
        sceneStartButton.setPos(0, -vertDist)
        sceneSettingsButton.setPos(0, 0)
        sceneExitButton.setPos(0, vertDist)

class CombatWindow(QGraphicsView):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setScene(QGraphicsScene(self))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        arnold = QPixmap(RESOURCES.joinpath('Arnold.jpg'))
        arnold = arnold.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)

        chuck = QPixmap(RESOURCES.joinpath('ChuckNorris.jpeg'))
        chuck = chuck.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)

        self.scene().addPixmap(arnold)
        self.scene().addPixmap(chuck)
