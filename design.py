# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1059, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1059, 610))
        MainWindow.setMaximumSize(QtCore.QSize(1059, 610))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(128, 128, 128);\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(165, 159, 128);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(128, 128, 128);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid white;\n"
"    \n"
"}\n"
"QInputDialog{\n"
"    background-color: rgb(165, 159, 128);\n"
"    border: 1px solid black;\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(165, 159, 128);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QListWidget{\n"
"    background-color: rgb(165, 159, 128);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid black;\n"
"    outline: 0;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color: rgb(165, 159, 128);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(165, 159, 128);\n"
"\n"
"}\n"
"QHeaderView{\n"
"    border: 1px solid black;\n"
"    gridline-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(128, 128, 128);\n"
"    alternate-background-color: rgb(165, 159, 128);\n"
"    gridline-color: rgb(0, 0, 0);\n"
"    font-size: 12pt;\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(410, 10, 641, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        self.viewText = QtWidgets.QWidget()
        self.viewText.setObjectName("viewText")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.viewText)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 641, 531))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.viewText)
        self.fileNameLineEdit.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.fileNameLineEdit.setReadOnly(True)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.saveTextEditButton = QtWidgets.QPushButton(self.viewText)
        self.saveTextEditButton.setGeometry(QtCore.QRect(550, 570, 71, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.saveTextEditButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/devedee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveTextEditButton.setIcon(icon)
        self.saveTextEditButton.setObjectName("saveTextEditButton")
        self.stackedWidget.addWidget(self.viewText)
        self.viewTable = QtWidgets.QWidget()
        self.viewTable.setObjectName("viewTable")
        self.todoTableWidget = QtWidgets.QTableWidget(self.viewTable)
        self.todoTableWidget.setGeometry(QtCore.QRect(0, 30, 641, 531))
        self.todoTableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.todoTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.todoTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.todoTableWidget.setProperty("showDropIndicator", False)
        self.todoTableWidget.setDragEnabled(True)
        self.todoTableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.todoTableWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.todoTableWidget.setAlternatingRowColors(True)
        self.todoTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.todoTableWidget.setObjectName("todoTableWidget")
        self.todoTableWidget.setColumnCount(3)
        self.todoTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.todoTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.todoTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.todoTableWidget.setHorizontalHeaderItem(2, item)
        self.todoAddButton = QtWidgets.QPushButton(self.viewTable)
        self.todoAddButton.setGeometry(QtCore.QRect(20, 570, 71, 21))
        self.todoAddButton.setObjectName("todoAddButton")
        self.todoFileNameLineEdit = QtWidgets.QLineEdit(self.viewTable)
        self.todoFileNameLineEdit.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.todoFileNameLineEdit.setObjectName("todoFileNameLineEdit")
        self.todoSaveButton = QtWidgets.QPushButton(self.viewTable)
        self.todoSaveButton.setGeometry(QtCore.QRect(550, 570, 71, 21))
        self.todoSaveButton.setIcon(icon)
        self.todoSaveButton.setObjectName("todoSaveButton")
        self.todoRemoveButton = QtWidgets.QPushButton(self.viewTable)
        self.todoRemoveButton.setGeometry(QtCore.QRect(100, 570, 71, 21))
        self.todoRemoveButton.setObjectName("todoRemoveButton")
        self.stackedWidget.addWidget(self.viewTable)
        self.viewCost = QtWidgets.QWidget()
        self.viewCost.setObjectName("viewCost")
        self.costTableWidget = QtWidgets.QTableWidget(self.viewCost)
        self.costTableWidget.setGeometry(QtCore.QRect(0, 30, 641, 531))
        self.costTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.costTableWidget.setObjectName("costTableWidget")
        self.costTableWidget.setColumnCount(2)
        self.costTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.costTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.costTableWidget.setHorizontalHeaderItem(1, item)
        self.costTableWidget.verticalHeader().setVisible(False)
        self.costFileNamelineEdit = QtWidgets.QLineEdit(self.viewCost)
        self.costFileNamelineEdit.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.costFileNamelineEdit.setObjectName("costFileNamelineEdit")
        self.costAddButton = QtWidgets.QPushButton(self.viewCost)
        self.costAddButton.setGeometry(QtCore.QRect(20, 570, 71, 21))
        self.costAddButton.setObjectName("costAddButton")
        self.costSaveButton = QtWidgets.QPushButton(self.viewCost)
        self.costSaveButton.setGeometry(QtCore.QRect(550, 570, 71, 21))
        self.costSaveButton.setIcon(icon)
        self.costSaveButton.setObjectName("costSaveButton")
        self.costRemoveButton = QtWidgets.QPushButton(self.viewCost)
        self.costRemoveButton.setGeometry(QtCore.QRect(100, 570, 71, 21))
        self.costRemoveButton.setObjectName("costRemoveButton")
        self.stackedWidget.addWidget(self.viewCost)
        self.newProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newProjectButton.setGeometry(QtCore.QRect(30, 580, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.newProjectButton.setFont(font)
        self.newProjectButton.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/doyourhomework.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newProjectButton.setIcon(icon1)
        self.newProjectButton.setObjectName("newProjectButton")
        self.naviLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.naviLineEdit.setGeometry(QtCore.QRect(10, 10, 391, 31))
        self.naviLineEdit.setStyleSheet("")
        self.naviLineEdit.setObjectName("naviLineEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 391, 531))
        self.listWidget.setStyleSheet("")
        self.listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyroject - Alpha v0.2 - By: Juju"))
        self.saveTextEditButton.setText(_translate("MainWindow", "Save"))
        item = self.todoTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.todoTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.todoTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Notes"))
        self.todoAddButton.setText(_translate("MainWindow", "+"))
        self.todoSaveButton.setText(_translate("MainWindow", "Save"))
        self.todoRemoveButton.setText(_translate("MainWindow", "-"))
        item = self.costTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.costTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        self.costAddButton.setText(_translate("MainWindow", "+"))
        self.costSaveButton.setText(_translate("MainWindow", "Save"))
        self.costRemoveButton.setText(_translate("MainWindow", "-"))
        self.newProjectButton.setText(_translate("MainWindow", "project"))

