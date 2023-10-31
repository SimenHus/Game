from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                               QFrame, QWidget, QLayout, QStackedWidget, QHBoxLayout,
                               QSizePolicy)
from PySide6.QtGui import QPixmap

from common import *

class CombatWindow(QStackedWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.leftCombatant = QLabel(self)
        arnold = QPixmap(RESOURCES.joinpath('Arnold.jpg'))
        self.leftCombatant.setPixmap(arnold)
        self.leftCombatant.setScaledContents(True)
        self.leftCombatant.resize(100, 100)


        layout.addWidget(self.leftCombatant)

        self.setLayout(layout)
