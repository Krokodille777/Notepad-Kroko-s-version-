from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTextEdit, QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from modal import FontDialog
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Windows Properties
        self.setWindowTitle("Notepad - Kroko's Version")  
        self.setGeometry(100, 100, 800, 600)

        # Layout 
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Menu Bar
        main_menu = QMenuBar(self)

        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)
        file_menu.addSeparator()
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Save As")
        file_menu.addSeparator()
        file_menu.addAction("Print")

        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addSeparator()
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addSeparator()
        edit_menu.addAction("Select All")
        
       
        change_font_action = QAction("Change Font", self)
        change_font_action.triggered.connect(self.openEditFontDialog)
        edit_menu.addAction(change_font_action)
        
        mainLayout.addWidget(main_menu)

        # NotePad Area
        self.text_area = QTextEdit("", self)
        self.text_area.setStyleSheet("background-color: white; border: 1px solid black; color: black; font-size: 20px; font-family: Courier New;")
        self.text_area.setFixedSize(780, 520)
        
        mainLayout.addWidget(self.text_area)

    def openEditFontDialog(self):
        dialog = FontDialog(self.text_area, self)
        dialog.exec()

    def undo(self):
        self.text_area.undo()
    def redo(self):
        self.text_area.redo()
    
    def cut(self):
        self.text_area.cut()
    def copy(self):
        self.text_area.copy()
    def paste(self):
        self.text_area.paste()
    def selectAll(self):
        self.text_area.selectAll()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())