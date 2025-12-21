from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QComboBox, QCheckBox
from PySide6.QtCore import Qt

class FontDialog(QDialog):
    def __init__(self, text_widget, parent=None):
        super().__init__(parent)
        self.text_widget = text_widget  
        
        self.setWindowTitle("Change Font")
        self.setGeometry(150, 150, 400, 250)
        layout = QVBoxLayout()
        
        label = QLabel("Change Font", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(label)
        
        size_layout = QHBoxLayout()
        size_label = QLabel("Font Size: ", self)
        self.size_select = QComboBox(self)
        self.size_select.addItems(["12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "48", "72"])
        size_layout.addWidget(size_label)
        size_layout.addWidget(self.size_select)
        layout.addLayout(size_layout)
        
        family_layout = QHBoxLayout()
        family_label = QLabel("Font Family: ", self)
        self.family_select = QComboBox(self)
        self.family_select.addItems(["Arial", "Courier New", "Times New Roman"])
        family_layout.addWidget(family_label)
        family_layout.addWidget(self.family_select)
        layout.addLayout(family_layout)
        
        color_layout = QHBoxLayout()
        color_label = QLabel("Font Color: ", self)
        self.color_select = QComboBox(self)
        self.color_select.addItems(["Black", "Red", "Blue", "Green"])
        color_layout.addWidget(color_label)
        color_layout.addWidget(self.color_select)
        layout.addLayout(color_layout)
        
        style_layout = QHBoxLayout()
        style_label = QLabel("Font Style: ", self)
        self.style_select = QComboBox(self)
        self.style_select.addItems(["Normal", "Bold", "Italic", "Underline"])
        style_layout.addWidget(style_label)
        style_layout.addWidget(self.style_select)
        layout.addLayout(style_layout)
        
        self.apply_shadows = QCheckBox("Apply Shadow Effect", self)
        layout.addWidget(self.apply_shadows)
        
        apply_button = QPushButton("Apply", self)
        apply_button.clicked.connect(self.applyChanges)
        layout.addWidget(apply_button)
        
        self.setLayout(layout)

    def applyChanges(self):
        size = self.size_select.currentText()
        family = self.family_select.currentText()
        color = self.color_select.currentText().lower()
        style = self.style_select.currentText()
        
        style_sheet = f"""
            font-size: {size}px;
            font-family: {family};
            color: {color};
            font-weight: {'bold' if style == 'Bold' else 'normal'};
            font-style: {'italic' if style == 'Italic' else 'normal'};
            text-decoration: {'underline' if style == 'Underline' else 'none'};
        """

        current_style = self.text_widget.styleSheet()
        print("Font Settings applied successfully!")
        base_style = "background-color: white; border: 1px solid black;"
        self.text_widget.setStyleSheet(base_style + style_sheet)
        
        self.close()