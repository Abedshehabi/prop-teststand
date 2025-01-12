from typing import Any

from PySide6.QtCore import Qt  #type:ignore
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

from qretproptools.gui.full_Gui.BaseDashboard import BaseDashboard


class DevicesDashboardWidget(BaseDashboard):
    def __init__(self,
                 name: str,
                 *args: Any,
                 **kwargs: Any,
                 ) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"This is the {name} dashboard"))
        self.setLayout(layout)

        self.errorButton = QPushButton("Find devices on network")
        self.errorButton.clicked.connect(lambda: self.openErrorWindow("This is Abed's error message.\n You're so silly frosh!",
                                                                      "Why'd you click this???"))
        layout.addWidget(self.errorButton)

        layout.setAlignment(Qt.AlignTop)  # type:ignore # QT not typed
