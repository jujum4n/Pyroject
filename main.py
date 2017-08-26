#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QInputDialog
import csv
import sys
import design
import qdarkstyle
import os
import resources


class Pyroject(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/colored_cube.png"));
        self.listWidget.itemDoubleClicked.connect(self.open_file)

        self.current_directory = ''
        self.current_todo_file = ''
        self.current_cost_file = ''
        self.current_file_edited = ''
        self.open_file_path = ''


        self.open_directory(os.getcwd())

        self.naviLineEdit.returnPressed.connect(self.open_current)


        self.newProjectButton.clicked.connect(self.projectNew)

        self.todoSaveButton.clicked.connect(self.todoSave)
        self.todoAddButton.clicked.connect(self.todoAddRow)
        self.todoRemoveButton.clicked.connect(self.todoRemoveRow)
        todoLabels = ['Status', 'Description', 'Notes']
        self.todoTableWidget.setHorizontalHeaderLabels(todoLabels)
        self.todoTableWidget.horizontalHeader().setVisible(True)
        self.todoTableWidget.setColumnWidth(0, self.todoTableWidget.width() / 6)
        self.todoTableWidget.setColumnWidth(1, self.todoTableWidget.width() / 3)
        self.todoTableWidget.setColumnWidth(2, (self.todoTableWidget.width() / 2))

        self.saveTextEditButton.clicked.connect(self.saveText)

        self.costSaveButton.clicked.connect(self.costSave)
        self.costAddButton.clicked.connect(self.costAddRow)
        self.costRemoveButton.clicked.connect(self.costRemoveRow)
        costLabels = ['Cost', 'Description']
        self.costTableWidget.setHorizontalHeaderLabels(costLabels)
        self.costTableWidget.horizontalHeader().setVisible(True)
        self.costTableWidget.setColumnWidth(0, self.costTableWidget.width() / 6)
        self.costTableWidget.setColumnWidth(1, self.costTableWidget.width() * .8332)

    def saveText(self):
        if self.open_file_path:
            file = open(self.open_file_path, 'w')
            file.write(self.plainTextEdit.toPlainText())
            file.close()
    def todoAddRow(self):
        num_rows = self.todoTableWidget.rowCount()
        self.todoTableWidget.insertRow(num_rows)


    def todoRemoveRow(self):
        num_rows = self.todoTableWidget.rowCount()
        self.todoTableWidget.removeRow(num_rows-1)

    def costAddRow(self):
        num_rows = self.costTableWidget.rowCount()
        self.costTableWidget.insertRow(num_rows)


    def costRemoveRow(self):
        num_rows = self.costTableWidget.rowCount()
        self.costTableWidget.removeRow(num_rows-1)

    def open_current(self):
        self.current_directory = self.naviLineEdit.text()
        self.open_directory(self.current_directory)


    def open_directory(self, folder):
        # If the user has chosen a folder, and it is not empty
        if folder and os.listdir(folder):
            self.listWidget.clear()
            self.listWidget.addItem('..')  # add file to the listWidget
            row = self.listWidget.count()
            ite = self.listWidget.item(row - 1)
            ite.setBackground(QColor('#a59f80'))
            ite.setForeground(QColor('black'))
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                # If it is a directory, and it is not a dot file or __ file
                if os.path.isdir(file_path) and not file_name.startswith('.') and not file_name.startswith('__'):
                    # If it is empty add a bit of text
                    if not os.listdir(file_path):
                        self.listWidget.addItem(file_name)  # add file to the listWidget
                        self.current_directory = os.path.join(folder)
                        row = self.listWidget.count()
                        ite = self.listWidget.item(row-1)
                        ite.setBackground(QColor('#4A4A4A'))
                    else:
                        self.listWidget.addItem(file_name)  # add file to the listWidget
                        self.current_directory = os.path.join(folder)
                        row = self.listWidget.count()
                        ite = self.listWidget.item(row-1)
                        ite.setBackground(QColor('#5d3954'))
                        ite.setIcon(QIcon(":/icons/new folder.png"))
                elif os.path.isdir(file_path) == False:
                    file_types = ['.cpp', '.py', '.txt', '.html', '.h', '.c', '.sol', '.js', '.rs', '.sh', '.java', '.config']
                    for x in file_types:
                        if file_name.endswith(x):
                            self.listWidget.addItem(file_name)  # add file to the listWidget
                            self.current_directory = os.path.join(folder)
                            row = self.listWidget.count()
                            ite = self.listWidget.item(row-1)
                            ite.setBackground(QColor('#9c0000'))
                            ite.setIcon(QIcon(":/icons/paperfulloftext.png"))

                    if file_name.endswith('.todo'):
                        self.listWidget.addItem(file_name)  # add file to the listWidget
                        self.current_directory = os.path.join(folder)
                        row = self.listWidget.count()
                        ite = self.listWidget.item(row - 1)
                        ite.setBackground(QColor('teal'))
                        ite.setIcon(QIcon(":/icons/excel.png"))
                    if file_name.endswith('.cost'):
                        self.listWidget.addItem(file_name)  # add file to the listWidget
                        self.current_directory = os.path.join(folder)
                        row = self.listWidget.count()
                        ite = self.listWidget.item(row - 1)
                        ite.setBackground(QColor('#b31b1b'))

                        ite.setIcon(QIcon(":/icons/pic.png"))
                    if file_name.endswith('.note'):
                        self.listWidget.addItem(file_name)  # add file to the listWidget
                        self.current_directory = os.path.join(folder)
                        row = self.listWidget.count()
                        ite = self.listWidget.item(row - 1)
                        ite.setBackground(QColor('#A0522D'))
                        ite.setIcon(QIcon(":/icons/note.png"))

            self.naviLineEdit.setText(self.current_directory)


    def open_file(self):
        ite = self.listWidget.currentItem()
        file_name = ite.text()
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.isdir(file_path) == False and not file_name.startswith('.') and not file_name.startswith('__') and not file_name.endswith('.todo') and not file_name.endswith('.cost'):
            f = open(file_path, 'r')
            data = f.read()
            self.plainTextEdit.setPlainText('')
            self.plainTextEdit.setPlainText(data)
            f.close()
            self.stackedWidget.setCurrentIndex(0)
            self.fileNameLineEdit.setText(file_name)
            self.open_file_path = file_path
            if file_name.endswith('.note'):
                self.fileNameLineEdit.setStyleSheet("background: #A0522D")
            else:
                self.fileNameLineEdit.setStyleSheet("background: #9c0000")
        if os.path.isdir(file_path) == True and not file_name.startswith('.') and not file_name.startswith('__'):
            file_path = os.path.join(self.current_directory, file_name)
            self.open_directory(file_path)
        if file_name == '..':
            try:
                os.chdir(self.current_directory)
                os.chdir('..')
                self.open_directory(os.path.abspath(os.curdir))
                self.current_directory = os.path.abspath(os.curdir)
            except:
                pass

        if file_name.endswith('.todo'):
            self.handleTodoOpen(self.current_directory+'/'+file_name)
            self.current_todo_file = file_name
            self.todoFileNameLineEdit.setText(self.current_todo_file)
            self.open_file_path = file_path
            self.todoFileNameLineEdit.setStyleSheet("background: #008080")

        if file_name.endswith('.cost'):
            self.handleCostOpen(self.current_directory+'/'+file_name)
            self.current_cost_file = file_name
            self.costFileNamelineEdit.setText(self.current_cost_file)
            self.open_file_path = file_path
            self.costFileNamelineEdit.setStyleSheet("background: #b31b1b;")

    def todoSave(self):
        self.handleTodoSave(self.current_directory+'/' + self.current_todo_file)

    def costSave(self):
        self.handleCostSave(self.current_directory + '/' + self.current_cost_file)

    def handleTodoSave(self, path):
        with open(path, 'w') as stream:
            writer = csv.writer(stream)
            for row in range(self.todoTableWidget.rowCount()):
                rowdata = []
                for column in range(self.todoTableWidget.columnCount()):
                    item = self.todoTableWidget.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)

    def handleTodoOpen(self, path):
        with open(path, 'r') as stream:
            self.todoTableWidget.setRowCount(0)
            self.todoTableWidget.setColumnCount(0)
            for rowdata in csv.reader(stream):
                row = self.todoTableWidget.rowCount()
                self.todoTableWidget.insertRow(row)
                self.todoTableWidget.setColumnCount(len(rowdata))
                for column, data in enumerate(rowdata):
                    item = QTableWidgetItem(data)
                    self.todoTableWidget.setItem(row, column, item)
            self.stackedWidget.setCurrentIndex(1)
            labels = ['Status', 'Description', 'Notes']
            self.todoTableWidget.setHorizontalHeaderLabels(labels)
            self.todoTableWidget.horizontalHeader().setVisible(True)
            self.todoTableWidget.verticalHeader().setVisible(False)
            self.todoTableWidget.setColumnWidth(0, self.todoTableWidget.width() / 6)
            self.todoTableWidget.setColumnWidth(1, self.todoTableWidget.width() / 3)
            self.todoTableWidget.setColumnWidth(2, (self.todoTableWidget.width() / 2))

    def handleCostOpen(self, path):
        with open(path, 'r') as stream:
            self.costTableWidget.setRowCount(0)
            self.costTableWidget.setColumnCount(0)
            for rowdata in csv.reader(stream):
                row = self.costTableWidget.rowCount()
                self.costTableWidget.insertRow(row)
                self.costTableWidget.setColumnCount(len(rowdata))
                for column, data in enumerate(rowdata):
                    item = QTableWidgetItem(data)
                    self.costTableWidget.setItem(row, column, item)
            self.stackedWidget.setCurrentIndex(2)
            labels = ['Cost', 'Description']
            self.costTableWidget.setHorizontalHeaderLabels(labels)
            self.costTableWidget.horizontalHeader().setVisible(True)
            self.costTableWidget.verticalHeader().setVisible(False)
            self.costTableWidget.setColumnWidth(0, self.costTableWidget.width() / 6)
            self.costTableWidget.setColumnWidth(1, self.costTableWidget.width() * .8332)

    def handleCostSave(self, path):
        with open(path, 'w') as stream:
            writer = csv.writer(stream)
            for row in range(self.costTableWidget.rowCount()):
                rowdata = []
                for column in range(self.costTableWidget.columnCount()):
                    item = self.costTableWidget.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)


    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        self.open_directory(directory)

    def costNew(self):
        cwd = self.current_directory
        items = cwd.split('/')
        if items[-1] == '':
            items.pop(-1)
        os.chdir(cwd)
        if not os.path.exists('"' + items[-1] + '.cost"'):
            try:
                self.newFile(items[-1] + '.cost')
                os.system('echo "," > "' + items[-1] + '.cost"')
            except:
                pass
        self.current_directory = cwd



    def projectNew(self):
        cwd = self.current_directory
        os.chdir(cwd)
        text, ok = QInputDialog.getText(self, 'New Project', 'Cool Project Name:')
        if ok:
            if not os.path.exists(text):
                os.system('mkdir "' + text + '"')
                self.current_directory = cwd + '/' + text
                os.chdir(text)
                self.todoNew()
                self.noteNew()
                self.costNew()
                os.chdir("..")
                self.current_directory = os.getcwd()
                self.open_current()

    def todoNew(self):
        cwd = self.current_directory
        items = cwd.split('/')
        if items[-1] == '':
            items.pop(-1)
        os.chdir(cwd)
        if not os.path.exists('"' + items[-1] + '.todo"'):
            try:
                self.newFile(items[-1] + '.todo')
                os.system('echo ",," > "' + items[-1] + '.todo"')
            except:
                pass
        self.current_directory = cwd

    def noteNew(self):
        cwd = self.current_directory
        items = cwd.split('/')
        if items[-1] == '':
            items.pop(-1)
        os.chdir(cwd)
        if not os.path.exists('"' + items[-1] + '.note"'):
            try:
                self.newFile(items[-1] + '.note')
                os.system('echo "empty" > "' + items[-1] + '.note"')
            except:
                pass
        self.current_directory = cwd

    def newFile(self, file_name):
        os.system('touch "' + file_name + '"')
        self.open_current()

def main():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = Pyroject()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()