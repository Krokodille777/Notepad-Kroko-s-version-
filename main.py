from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel,QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
       #Windows Properties
        self.setWindowTitle("Notepad - Kroko's Version")  
        self.setGeometry(100, 100, 800, 600)

        #Menu Bar
        main_menu = QMenuBar(self)

        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.close)



        #Layout 
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

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
        edit_menu.addAction("Change Font")
        mainLayout.addWidget(main_menu)

        #NotePad Area & Input

        text_area = QLabel("Enter text here...", self)
        


        text_area.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        text_area.setStyleSheet("background-color: white; border: 1px solid black; color: black;")
        text_area.setFixedSize(780, 520)

        text_area.setTextInteractionFlags(Qt.TextEditable | Qt.TextSelectableByMouse)
        text_area.enterEvent = lambda event: text_area.setStyleSheet("background-color: #e6f7ff; border: 1px solid black; color: black; font-size: 14px;")
        text_area.leaveEvent = lambda event: text_area.setStyleSheet("background-color: white; border: 1px solid black; color: black;")
        mainLayout.addWidget(text_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())