from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTextEdit, QMenuBar, QMenu, QDialog, QLabel, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from modal import FontDialog, saveOrNotDialog, helpDialog
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
        help_menu = main_menu.addMenu("Help")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        file_menu.addSeparator()

        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.openTxt)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.saveTxt)
        file_menu.addAction(save_action)

        save_as_action = QAction("Save As", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.saveTxt)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()
        print_action = QAction("Print", self)
        print_action.setShortcut("Ctrl+P")
        file_menu.addAction(print_action)

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
        
        help_action = QAction("Help", self)
        help_action.setShortcut("F1")
        help_action.triggered.connect(lambda: helpDialog(self).exec())
        help_menu.addAction(help_action)

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
    def new(self):
        if self.text_area.toPlainText(): # If there is text, clear it
            save_dialog = saveOrNotDialog(self)
            result = save_dialog.exec()
            if result == QDialog.Accepted:
                self.text_area.clear()  

        else:
            self.text_area.clear()


    def saveTxt(self):
        options  = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.toPlainText())

    def openTxt(self):
        options  = QFileDialog.Options()
        file_path, _ =QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.setPlainText(content)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())