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

        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction("Cut", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Copy", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)
        edit_menu.addSeparator()
        
        
        select_all_action = QAction("Select All", self)
        select_all_action.setShortcut("Ctrl+A")
        select_all_action.triggered.connect(self.selectAll)
        edit_menu.addAction(select_all_action)
        
       
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())