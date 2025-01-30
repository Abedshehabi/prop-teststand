from typing import Any

from PySide6.QtCore import Qt  #type:ignore
from PySide6.QtWidgets import QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from qretproptools.gui.full_Gui.BaseDashboard import BaseDashboard

class DevicesDashboardWidget(BaseDashboard):
    def __init__(self,
                 name: str,
                 *args: Any,
                 **kwargs: Any,
                 ) -> None:
        super().__init__(*args, **kwargs)


        label = QLabel(f"This is the {name} dashboard")
        label.setFixedSize(200, 10)  # Set the dimensions (width, height)

        layout = QVBoxLayout()
        layout.addWidget(label, 1)

        # Create a table to display the device information
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Device Name", "IP Address", "Port", "Sensors"])


        self.errorButton = QPushButton("Find devices on network")
        self.errorButton.clicked.connect(self.populate_table)
        layout.addWidget(self.errorButton, 1)

        #layout.setAlignment(Qt.AlignTop)  # type:ignore # QT not typed



        # Create a black box with specific dimensions
        black_box = QWidget()
        black_box.setStyleSheet("background-color: black;")

        layout.addWidget(black_box, 10)

        # Add the table to the black box
        black_box_layout = QVBoxLayout(black_box)
        black_box_layout.addWidget(self.table)

        self.setLayout(layout)

        #"Find devices on network" button will display the device information in the black box
        #So error button will be replaced with smth else?

        # Add the device information to the table when you click "Find devices on network" button

    def populate_table(self):
        self.table.setItem(0, 0, QTableWidgetItem("ESP-32"))
        self.table.setItem(0, 1, QTableWidgetItem("192.168.1.2"))
        self.table.setItem(0, 2, QTableWidgetItem("80"))
        self.table.setItem(0, 3, QTableWidgetItem("Temperature, Pressure, Load cell"))

        self.table.setItem(1, 0, QTableWidgetItem("Camera"))
        self.table.setItem(1, 1, QTableWidgetItem("192.168.1.4"))
        self.table.setItem(1, 2, QTableWidgetItem("80"))
        self.table.setItem(1, 3, QTableWidgetItem("Resolution, FPS"))

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


        # # Add the device information to the table
        # table.setItem(0, 0, QTableWidgetItem("Device 1"))
        # table.setItem(0, 1, QTableWidgetItem("Device 2"))
        # table.setItem(0, 2, QTableWidgetItem("Device 3"))
        # table.setItem(0, 3, QTableWidgetItem("Device 4"))

        # # Add the table to the black box
        # layout.addWidget(table)
        # black_box.setLayout(layout)
        # # Add the black box to the layout
        # layout.addWidget(black_box)
        # self.setLayout(layout)

