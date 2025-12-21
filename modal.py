import PySide6
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QComboBox, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from main import MainWindow

class FontDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Font")
        self.setGeometry(150, 150, 300, 200)
        layout = QVBoxLayout()
        label = QLabel("Change Font", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(label)
        size_and_family_layout = QHBoxLayout()
        size_label = QLabel("Font Size: ", self)

        size_select = QComboBox(self)
        size_select.addItem ("12")
        size_select.addItem ("14")
        size_select.addItem ("16")
        size_select.addItem ("18")
        size_select.addItem ("20")
        size_select.addItem ("22")
        size_select.addItem ("24")
        size_select.addItem ("26")
        size_select.addItem ("28")
        size_select.addItem ("30")
        size_select.addItem ("32")
        size_select.addItem ("48")
        size_select.addItem ("72")
        size_section = QHBoxLayout()
        size_section.addWidget(size_select)

        size_and_family_layout.addLayout(size_section)
        size_and_family_layout.addWidget(size_label)

        family_label = QLabel("Font Family: ", self)
        family_select = QComboBox(self)
        family_select.addItem("Arial")
        family_select.addItem("Courier New")
        family_select.addItem("Times New Roman")
        family_section = QHBoxLayout()
        family_section.addWidget(family_select)

        size_and_family_layout.addWidget(family_label)
        size_and_family_layout.addLayout(family_section)
        layout.addLayout(size_and_family_layout)

        color_n_style_layout = QHBoxLayout()
        color_label = QLabel("Font Color: ", self)
        color_select = QComboBox(self)
        color_select.addItem("Black")
        color_select.addItem("Red")
        color_select.addItem("Blue")
        color_select.addItem("Green")
        color_section = QHBoxLayout()
        color_section.addWidget(color_select)

        color_n_style_layout.addLayout(color_section)
        color_n_style_layout.addWidget(color_label)
        layout.addLayout(color_n_style_layout)

        style_label = QLabel("Font Style: ", self)
        style_select = QComboBox(self)
        style_select.addItem("Normal")
        style_select.addItem("Bold")
        style_select.addItem("Italic")
        style_select.addItem("Underline")
        
        style_sectiom = QHBoxLayout()
        style_sectiom.addWidget(style_select)

       
        color_n_style_layout.addLayout(style_sectiom)
        color_n_style_layout.addWidget(style_label)
        layout.addLayout(color_n_style_layout)

        apply_shadows = QCheckBox("Apply Shadow Effect", self)
        layout.addWidget(apply_shadows)

        apply_button = QPushButton("Apply", self)
        apply_button.clicked.connect(self.applyChanges)
        layout.addWidget(apply_button)

        self.setLayout(layout)

    def applyChanges(self):
            #Потверждаем изменения шрифта
            #findChild используется для поиска виджетов внутри диалога
            #findChildren используется для поиска всех виджетов определенного типа внутри диалога
            size_select = self.findChild(QComboBox)
            family_select = self.findChildren(QComboBox)[1]
            color_select = self.findChildren(QComboBox)[2]
            style_select = self.findChildren(QComboBox)[3]
            main_window = MainWindow()
            text = main_window.findChild(QLabel)
            text.setStyleSheet(f"font-size: {size_select.currentText()}px; font-family: {family_select.currentText()}; color: {color_select.currentText().lower()}; font-weight: {'bold' if style_select.currentText() == 'Bold' else 'normal'}; font-style: {'italic' if style_select.currentText() == 'Italic' else 'normal'}; text-decoration: {'underline' if style_select.currentText() == 'Underline' else 'none'};")
            self.close()



    def openDialog(self):
        self.exec()

    
        

