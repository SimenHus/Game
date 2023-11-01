from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                               QFrame, QWidget, QLayout, QStackedWidget, QHBoxLayout,
                               QSizePolicy, QGraphicsScene, QGraphicsView)
from PySide6.QtGui import QPixmap

from common import *

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
