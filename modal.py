import PySide6
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt



class FontDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Font")
        self.setGeometry(150, 150, 300, 200)
        layout = QVBoxLayout()
        label = QLabel("Font change functionality is not implemented yet.", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        close_button = QPushButton("Close", self)


        close_button.clicked.connect(self.close)

        layout.addWidget(close_button)
        self.setLayout(layout)

    def openDialog(self):
        self.exec()
