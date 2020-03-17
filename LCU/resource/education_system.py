# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'education_system.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 868)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(571, 641))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:125}\n"
"QTabBar::tab{height:32}")
        self.tabWidget.setObjectName("tabWidget")
        self.Homepage = QtWidgets.QWidget()
        self.Homepage.setObjectName("Homepage")
        self.groupBox = QtWidgets.QGroupBox(self.Homepage)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 921, 621))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.Img_lab = QtWidgets.QLabel(self.groupBox)
        self.Img_lab.setGeometry(QtCore.QRect(740, 30, 171, 191))
        self.Img_lab.setText("")
        self.Img_lab.setObjectName("Img_lab")
        self.info_ted = QtWidgets.QTextEdit(self.groupBox)
        self.info_ted.setGeometry(QtCore.QRect(10, 30, 711, 581))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.info_ted.setFont(font)
        self.info_ted.setReadOnly(True)
        self.info_ted.setObjectName("info_ted")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Homepage)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 680, 921, 111))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 164, 73);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.plan_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.plan_btn.setGeometry(QtCore.QRect(20, 50, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.plan_btn.setFont(font)
        self.plan_btn.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 255, 255);")
        self.plan_btn.setText("")
        self.plan_btn.setObjectName("plan_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Homepage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 921, 51))
        self.groupBox_3.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 164, 73);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(11, 0, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(8, 8, 8);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.change_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.change_btn.setGeometry(QtCore.QRect(840, 20, 81, 28))
        self.change_btn.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 255, 255);")
        self.change_btn.setObjectName("change_btn")
        self.tabWidget.addTab(self.Homepage, "")
        self.Course = QtWidgets.QWidget()
        self.Course.setObjectName("Course")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Course)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 931, 791))
        self.tabWidget_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget_2.setStyleSheet("QTabBar::tab{width:170}\n"
"QTabBar::tab{height:28}\n"
"color: rgb(255, 222, 167);\n"
"\n"
"")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Elective_course = QtWidgets.QWidget()
        self.Elective_course.setObjectName("Elective_course")
        self.label = QtWidgets.QLabel(self.Elective_course)
        self.label.setGeometry(QtCore.QRect(10, 60, 901, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 241, 162);\n"
"color: rgb(255, 56, 42);\n"
"border-width: 1px;border-style: solid;\n"
"border-color: rgb(18, 18, 18);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.Elective_course)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 901, 41))
        self.groupBox_4.setObjectName("groupBox_4")
        self.line = QtWidgets.QFrame(self.Elective_course)
        self.line.setGeometry(QtCore.QRect(0, 120, 921, 20))
        self.line.setStyleSheet("border-color: rgb(30, 150, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Elective_course)
        self.stackedWidget_2.setGeometry(QtCore.QRect(140, 160, 781, 571))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Planning_course_Page = QtWidgets.QWidget()
        self.Planning_course_Page.setObjectName("Planning_course_Page")
        self.Planning_course_view = QtWidgets.QTableView(self.Planning_course_Page)
        self.Planning_course_view.setGeometry(QtCore.QRect(20, 20, 751, 511))
        self.Planning_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Planning_course_view.setObjectName("Planning_course_view")
        self.Planning_course_view.verticalHeader().setVisible(False)
        self.pushButton_7 = QtWidgets.QPushButton(self.Planning_course_Page)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 540, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.Planning_course_Page)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 540, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget_2.addWidget(self.Planning_course_Page)
        self.Program_course_Page = QtWidgets.QWidget()
        self.Program_course_Page.setObjectName("Program_course_Page")
        self.Program_course_view = QtWidgets.QTableView(self.Program_course_Page)
        self.Program_course_view.setGeometry(QtCore.QRect(20, 40, 751, 491))
        self.Program_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Program_course_view.setObjectName("Program_course_view")
        self.Program_course_view.verticalHeader().setVisible(False)
        self.label_56 = QtWidgets.QLabel(self.Program_course_Page)
        self.label_56.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.label_56.setObjectName("label_56")
        self.comboBox = QtWidgets.QComboBox(self.Program_course_Page)
        self.comboBox.setGeometry(QtCore.QRect(340, 10, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.Program_course_Page)
        self.comboBox_2.setGeometry(QtCore.QRect(600, 10, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_57 = QtWidgets.QLabel(self.Program_course_Page)
        self.label_57.setGeometry(QtCore.QRect(520, 10, 71, 21))
        self.label_57.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.pushButton_9 = QtWidgets.QPushButton(self.Program_course_Page)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 10, 61, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Program_course_Page)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 540, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.Program_course_Page)
        self.pushButton_11.setGeometry(QtCore.QRect(670, 540, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.stackedWidget_2.addWidget(self.Program_course_Page)
        self.Elective_course_Page = QtWidgets.QWidget()
        self.Elective_course_Page.setObjectName("Elective_course_Page")
        self.Elective_course_view = QtWidgets.QTableView(self.Elective_course_Page)
        self.Elective_course_view.setGeometry(QtCore.QRect(20, 20, 751, 501))
        self.Elective_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Elective_course_view.setObjectName("Elective_course_view")
        self.Elective_course_view.verticalHeader().setVisible(False)
        self.pushButton_12 = QtWidgets.QPushButton(self.Elective_course_Page)
        self.pushButton_12.setGeometry(QtCore.QRect(560, 530, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.Elective_course_Page)
        self.pushButton_13.setGeometry(QtCore.QRect(680, 530, 93, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget_2.addWidget(self.Elective_course_Page)
        self.School_elective_course_Page = QtWidgets.QWidget()
        self.School_elective_course_Page.setObjectName("School_elective_course_Page")
        self.School_elective_course_view = QtWidgets.QTableView(self.School_elective_course_Page)
        self.School_elective_course_view.setGeometry(QtCore.QRect(20, 20, 751, 501))
        self.School_elective_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.School_elective_course_view.setObjectName("School_elective_course_view")
        self.School_elective_course_view.verticalHeader().setVisible(False)
        self.pushButton_14 = QtWidgets.QPushButton(self.School_elective_course_Page)
        self.pushButton_14.setGeometry(QtCore.QRect(560, 530, 93, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.School_elective_course_Page)
        self.pushButton_15.setGeometry(QtCore.QRect(680, 530, 93, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget_2.addWidget(self.School_elective_course_Page)
        self.free_choice_course_Page = QtWidgets.QWidget()
        self.free_choice_course_Page.setObjectName("free_choice_course_Page")
        self.free_choice_course_view = QtWidgets.QTableView(self.free_choice_course_Page)
        self.free_choice_course_view.setGeometry(QtCore.QRect(20, 150, 751, 371))
        self.free_choice_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.free_choice_course_view.setObjectName("free_choice_course_view")
        self.free_choice_course_view.verticalHeader().setVisible(False)
        self.label_58 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_58.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_59.setGeometry(QtCore.QRect(30, 50, 51, 21))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_60.setGeometry(QtCore.QRect(30, 80, 51, 21))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_61.setGeometry(QtCore.QRect(30, 110, 51, 21))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_62.setGeometry(QtCore.QRect(290, 20, 51, 21))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_63.setGeometry(QtCore.QRect(290, 50, 71, 21))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.free_choice_course_Page)
        self.label_64.setGeometry(QtCore.QRect(290, 80, 72, 21))
        self.label_64.setObjectName("label_64")
        self.lineEdit = QtWidgets.QLineEdit(self.free_choice_course_Page)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.free_choice_course_Page)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 50, 181, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.free_choice_course_Page)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 80, 181, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.free_choice_course_Page)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 110, 181, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.free_choice_course_Page)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 20, 181, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.free_choice_course_Page)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 50, 151, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.free_choice_course_Page)
        self.comboBox_4.setGeometry(QtCore.QRect(360, 80, 151, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_16 = QtWidgets.QPushButton(self.free_choice_course_Page)
        self.pushButton_16.setGeometry(QtCore.QRect(370, 110, 81, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.free_choice_course_Page)
        self.pushButton_17.setGeometry(QtCore.QRect(680, 530, 93, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.free_choice_course_Page)
        self.pushButton_18.setGeometry(QtCore.QRect(560, 530, 93, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.stackedWidget_2.addWidget(self.free_choice_course_Page)
        self.Rehearsal_course_Page = QtWidgets.QWidget()
        self.Rehearsal_course_Page.setObjectName("Rehearsal_course_Page")
        self.Rehearsal_course_view = QtWidgets.QTableView(self.Rehearsal_course_Page)
        self.Rehearsal_course_view.setGeometry(QtCore.QRect(20, 20, 751, 501))
        self.Rehearsal_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Rehearsal_course_view.setObjectName("Rehearsal_course_view")
        self.Rehearsal_course_view.verticalHeader().setVisible(False)
        self.pushButton_19 = QtWidgets.QPushButton(self.Rehearsal_course_Page)
        self.pushButton_19.setGeometry(QtCore.QRect(670, 530, 93, 28))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.Rehearsal_course_Page)
        self.pushButton_20.setGeometry(QtCore.QRect(550, 530, 93, 28))
        self.pushButton_20.setObjectName("pushButton_20")
        self.stackedWidget_2.addWidget(self.Rehearsal_course_Page)
        self.layoutWidget = QtWidgets.QWidget(self.Elective_course)
        self.layoutWidget.setGeometry(QtCore.QRect(4, 160, 111, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Planning_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Planning_course_btn.setObjectName("Planning_course_btn")
        self.verticalLayout.addWidget(self.Planning_course_btn)
        self.Program_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Program_course_btn.setObjectName("Program_course_btn")
        self.verticalLayout.addWidget(self.Program_course_btn)
        self.Elective_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Elective_course_btn.setObjectName("Elective_course_btn")
        self.verticalLayout.addWidget(self.Elective_course_btn)
        self.School_elective_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.School_elective_course_btn.setObjectName("School_elective_course_btn")
        self.verticalLayout.addWidget(self.School_elective_course_btn)
        self.free_choice_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.free_choice_course_btn.setObjectName("free_choice_course_btn")
        self.verticalLayout.addWidget(self.free_choice_course_btn)
        self.Rehearsal_course_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Rehearsal_course_btn.setObjectName("Rehearsal_course_btn")
        self.verticalLayout.addWidget(self.Rehearsal_course_btn)
        self.tabWidget_2.addTab(self.Elective_course, "")
        self.Elective_course_res = QtWidgets.QWidget()
        self.Elective_course_res.setObjectName("Elective_course_res")
        self.details_view_2 = QtWidgets.QTableView(self.Elective_course_res)
        self.details_view_2.setGeometry(QtCore.QRect(0, 440, 921, 311))
        self.details_view_2.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.details_view_2.setObjectName("details_view_2")
        self.details_view_2.verticalHeader().setVisible(False)
        self.course_view_2 = QtWidgets.QTableView(self.Elective_course_res)
        self.course_view_2.setGeometry(QtCore.QRect(0, 30, 921, 411))
        self.course_view_2.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.course_view_2.setObjectName("course_view_2")
        self.course_view_2.verticalHeader().setVisible(False)
        self.course_res_lab = QtWidgets.QLabel(self.Elective_course_res)
        self.course_res_lab.setGeometry(QtCore.QRect(0, 0, 191, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.course_res_lab.setFont(font)
        self.course_res_lab.setObjectName("course_res_lab")
        self.timer_lab = QtWidgets.QLabel(self.Elective_course_res)
        self.timer_lab.setGeometry(QtCore.QRect(660, 0, 271, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.timer_lab.setFont(font)
        self.timer_lab.setText("")
        self.timer_lab.setObjectName("timer_lab")
        self.tabWidget_2.addTab(self.Elective_course_res, "")
        self.Withdrawal = QtWidgets.QWidget()
        self.Withdrawal.setObjectName("Withdrawal")
        self.label_4 = QtWidgets.QLabel(self.Withdrawal)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 901, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 241, 162);\n"
"color: rgb(255, 56, 42);\n"
"border-width: 1px;border-style: solid;\n"
"border-color: rgb(18, 18, 18);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Withdrawal)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 901, 41))
        self.groupBox_6.setObjectName("groupBox_6")
        self.line_3 = QtWidgets.QFrame(self.Withdrawal)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 921, 20))
        self.line_3.setStyleSheet("border-color: rgb(30, 150, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.drop_course_view = QtWidgets.QTableView(self.Withdrawal)
        self.drop_course_view.setGeometry(QtCore.QRect(0, 160, 921, 581))
        self.drop_course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.drop_course_view.setObjectName("drop_course_view")
        self.drop_course_view.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.Withdrawal, "")
        self.Invalid_Elective = QtWidgets.QWidget()
        self.Invalid_Elective.setObjectName("Invalid_Elective")
        self.label_3 = QtWidgets.QLabel(self.Invalid_Elective)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 901, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 241, 162);\n"
"color: rgb(255, 56, 42);\n"
"border-width: 1px;border-style: solid;\n"
"border-color: rgb(18, 18, 18);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Invalid_Elective)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 901, 41))
        self.groupBox_5.setObjectName("groupBox_5")
        self.line_2 = QtWidgets.QFrame(self.Invalid_Elective)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 921, 20))
        self.line_2.setStyleSheet("border-color: rgb(30, 150, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.null_course_res_view = QtWidgets.QTableView(self.Invalid_Elective)
        self.null_course_res_view.setGeometry(QtCore.QRect(10, 150, 901, 581))
        self.null_course_res_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.null_course_res_view.setObjectName("null_course_res_view")
        self.null_course_res_view.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.Invalid_Elective, "")
        self.Class_Schedule = QtWidgets.QWidget()
        self.Class_Schedule.setObjectName("Class_Schedule")
        self.course_view = QtWidgets.QTableView(self.Class_Schedule)
        self.course_view.setGeometry(QtCore.QRect(0, 30, 921, 411))
        self.course_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.course_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.course_view.setLineWidth(2)
        self.course_view.setObjectName("course_view")
        self.course_view.verticalHeader().setVisible(False)
        self.details_view = QtWidgets.QTableView(self.Class_Schedule)
        self.details_view.setGeometry(QtCore.QRect(0, 440, 921, 311))
        self.details_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.details_view.setObjectName("details_view")
        self.details_view.verticalHeader().setVisible(False)
        self.timer_lab_2 = QtWidgets.QLabel(self.Class_Schedule)
        self.timer_lab_2.setGeometry(QtCore.QRect(660, 0, 271, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.timer_lab_2.setFont(font)
        self.timer_lab_2.setText("")
        self.timer_lab_2.setObjectName("timer_lab_2")
        self.course_res_lab_2 = QtWidgets.QLabel(self.Class_Schedule)
        self.course_res_lab_2.setGeometry(QtCore.QRect(0, 0, 191, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.course_res_lab_2.setFont(font)
        self.course_res_lab_2.setObjectName("course_res_lab_2")
        self.tabWidget_2.addTab(self.Class_Schedule, "")
        self.tabWidget.addTab(self.Course, "")
        self.assess = QtWidgets.QWidget()
        self.assess.setObjectName("assess")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.assess)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 0, 921, 791))
        self.tabWidget_3.setStyleSheet("QTabBar::tab{width:184}\n"
"QTabBar::tab{height:30}")
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.evaluate_post_wid = QtWidgets.QWidget()
        self.evaluate_post_wid.setObjectName("evaluate_post_wid")
        self.post_lab = QtWidgets.QLabel(self.evaluate_post_wid)
        self.post_lab.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.post_lab.setFont(font)
        self.post_lab.setStyleSheet("color: rgb(255, 30, 10);")
        self.post_lab.setObjectName("post_lab")
        self.tabWidget_3.addTab(self.evaluate_post_wid, "")
        self.teaching_evaluate_wid = QtWidgets.QWidget()
        self.teaching_evaluate_wid.setObjectName("teaching_evaluate_wid")
        self.teaching_lab = QtWidgets.QLabel(self.teaching_evaluate_wid)
        self.teaching_lab.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.teaching_lab.setFont(font)
        self.teaching_lab.setStyleSheet("color: rgb(255, 30, 10);")
        self.teaching_lab.setObjectName("teaching_lab")
        self.tabWidget_3.addTab(self.teaching_evaluate_wid, "")
        self.graduate_evaluate_wid = QtWidgets.QWidget()
        self.graduate_evaluate_wid.setObjectName("graduate_evaluate_wid")
        self.graduate_evaluate_lab = QtWidgets.QLabel(self.graduate_evaluate_wid)
        self.graduate_evaluate_lab.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.graduate_evaluate_lab.setFont(font)
        self.graduate_evaluate_lab.setStyleSheet("color: rgb(255, 30, 10);")
        self.graduate_evaluate_lab.setObjectName("graduate_evaluate_lab")
        self.tabWidget_3.addTab(self.graduate_evaluate_wid, "")
        self.tabWidget.addTab(self.assess, "")
        self.Resource = QtWidgets.QWidget()
        self.Resource.setObjectName("Resource")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.Resource)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 951, 801))
        self.tabWidget_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_5.setStyleSheet("QTabBar::tab{width:220}")
        self.tabWidget_5.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_5.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 0, 911, 181))
        self.groupBox_12.setStyleSheet("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_31 = QtWidgets.QLabel(self.groupBox_12)
        self.label_31.setGeometry(QtCore.QRect(10, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.classroom_Academic_term_cob = QtWidgets.QComboBox(self.groupBox_12)
        self.classroom_Academic_term_cob.setGeometry(QtCore.QRect(100, 40, 261, 20))
        self.classroom_Academic_term_cob.setObjectName("classroom_Academic_term_cob")
        self.label_32 = QtWidgets.QLabel(self.groupBox_12)
        self.label_32.setGeometry(QtCore.QRect(10, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.classroom_Campus_cob = QtWidgets.QComboBox(self.groupBox_12)
        self.classroom_Campus_cob.setGeometry(QtCore.QRect(100, 80, 241, 20))
        self.classroom_Campus_cob.setObjectName("classroom_Campus_cob")
        self.label_33 = QtWidgets.QLabel(self.groupBox_12)
        self.label_33.setGeometry(QtCore.QRect(10, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.classroom_Teaching_building_cob = QtWidgets.QComboBox(self.groupBox_12)
        self.classroom_Teaching_building_cob.setGeometry(QtCore.QRect(100, 120, 241, 20))
        self.classroom_Teaching_building_cob.setObjectName("classroom_Teaching_building_cob")
        self.label_34 = QtWidgets.QLabel(self.groupBox_12)
        self.label_34.setGeometry(QtCore.QRect(350, 110, 51, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.classroom_class_cob = QtWidgets.QComboBox(self.groupBox_12)
        self.classroom_class_cob.setGeometry(QtCore.QRect(410, 120, 241, 20))
        self.classroom_class_cob.setObjectName("classroom_class_cob")
        self.classroom_query_btn = QtWidgets.QPushButton(self.groupBox_12)
        self.classroom_query_btn.setGeometry(QtCore.QRect(310, 150, 81, 28))
        self.classroom_query_btn.setObjectName("classroom_query_btn")
        self.classroom_firstpage_btn = QtWidgets.QPushButton(self.tab_4)
        self.classroom_firstpage_btn.setGeometry(QtCore.QRect(400, 720, 41, 21))
        self.classroom_firstpage_btn.setObjectName("classroom_firstpage_btn")
        self.classroom_endpage_btn = QtWidgets.QPushButton(self.tab_4)
        self.classroom_endpage_btn.setGeometry(QtCore.QRect(590, 720, 41, 21))
        self.classroom_endpage_btn.setObjectName("classroom_endpage_btn")
        self.Previous_btn_2 = QtWidgets.QPushButton(self.tab_4)
        self.Previous_btn_2.setGeometry(QtCore.QRect(450, 720, 61, 21))
        self.Previous_btn_2.setObjectName("Previous_btn_2")
        self.classroom_next_btn = QtWidgets.QPushButton(self.tab_4)
        self.classroom_next_btn.setGeometry(QtCore.QRect(520, 720, 61, 21))
        self.classroom_next_btn.setObjectName("classroom_next_btn")
        self.label_35 = QtWidgets.QLabel(self.tab_4)
        self.label_35.setGeometry(QtCore.QRect(640, 720, 91, 21))
        self.label_35.setObjectName("label_35")
        self.classroom_course_info_lab = QtWidgets.QLabel(self.tab_4)
        self.classroom_course_info_lab.setGeometry(QtCore.QRect(230, 720, 161, 21))
        self.classroom_course_info_lab.setObjectName("classroom_course_info_lab")
        self.classroom_page_led = QtWidgets.QLineEdit(self.tab_4)
        self.classroom_page_led.setGeometry(QtCore.QRect(800, 720, 51, 21))
        self.classroom_page_led.setObjectName("classroom_page_led")
        self.classroom_determine_btn = QtWidgets.QPushButton(self.tab_4)
        self.classroom_determine_btn.setGeometry(QtCore.QRect(860, 720, 61, 21))
        self.classroom_determine_btn.setObjectName("classroom_determine_btn")
        self.classroom_page_cob = QtWidgets.QComboBox(self.tab_4)
        self.classroom_page_cob.setGeometry(QtCore.QRect(730, 720, 61, 21))
        self.classroom_page_cob.setObjectName("classroom_page_cob")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_page_cob.addItem("")
        self.classroom_view = QtWidgets.QTableView(self.tab_4)
        self.classroom_view.setGeometry(QtCore.QRect(10, 190, 911, 521))
        self.classroom_view.setObjectName("classroom_view")
        self.classroom_view.verticalHeader().setVisible(False)
        self.tabWidget_5.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.teach_page_led = QtWidgets.QLineEdit(self.tab_3)
        self.teach_page_led.setGeometry(QtCore.QRect(800, 720, 51, 21))
        self.teach_page_led.setObjectName("teach_page_led")
        self.teach_firstpage_btn = QtWidgets.QPushButton(self.tab_3)
        self.teach_firstpage_btn.setGeometry(QtCore.QRect(400, 720, 41, 21))
        self.teach_firstpage_btn.setObjectName("teach_firstpage_btn")
        self.teach_endpage_btn = QtWidgets.QPushButton(self.tab_3)
        self.teach_endpage_btn.setGeometry(QtCore.QRect(590, 720, 41, 21))
        self.teach_endpage_btn.setObjectName("teach_endpage_btn")
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        self.label_36.setGeometry(QtCore.QRect(640, 720, 81, 21))
        self.label_36.setObjectName("label_36")
        self.teach_next_btn = QtWidgets.QPushButton(self.tab_3)
        self.teach_next_btn.setGeometry(QtCore.QRect(520, 720, 61, 21))
        self.teach_next_btn.setObjectName("teach_next_btn")
        self.teach_page_cob = QtWidgets.QComboBox(self.tab_3)
        self.teach_page_cob.setGeometry(QtCore.QRect(730, 720, 61, 20))
        self.teach_page_cob.setObjectName("teach_page_cob")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_page_cob.addItem("")
        self.teach_course_info_lab = QtWidgets.QLabel(self.tab_3)
        self.teach_course_info_lab.setGeometry(QtCore.QRect(220, 720, 171, 21))
        self.teach_course_info_lab.setObjectName("teach_course_info_lab")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 2, 911, 111))
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_37 = QtWidgets.QLabel(self.groupBox_13)
        self.label_37.setGeometry(QtCore.QRect(10, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.teach_Academic_term_cob = QtWidgets.QComboBox(self.groupBox_13)
        self.teach_Academic_term_cob.setGeometry(QtCore.QRect(90, 40, 231, 20))
        self.teach_Academic_term_cob.setObjectName("teach_Academic_term_cob")
        self.label_38 = QtWidgets.QLabel(self.groupBox_13)
        self.label_38.setGeometry(QtCore.QRect(320, 30, 61, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.teach_Department_cob = QtWidgets.QComboBox(self.groupBox_13)
        self.teach_Department_cob.setGeometry(QtCore.QRect(380, 40, 161, 20))
        self.teach_Department_cob.setObjectName("teach_Department_cob")
        self.label_40 = QtWidgets.QLabel(self.groupBox_13)
        self.label_40.setGeometry(QtCore.QRect(540, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.teach_name_led = QtWidgets.QLineEdit(self.groupBox_13)
        self.teach_name_led.setGeometry(QtCore.QRect(610, 40, 131, 21))
        self.teach_name_led.setObjectName("teach_name_led")
        self.label_39 = QtWidgets.QLabel(self.groupBox_13)
        self.label_39.setGeometry(QtCore.QRect(740, 40, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(8)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.teach_query_btn = QtWidgets.QPushButton(self.groupBox_13)
        self.teach_query_btn.setGeometry(QtCore.QRect(400, 70, 81, 28))
        self.teach_query_btn.setObjectName("teach_query_btn")
        self.teach_Previous_btn = QtWidgets.QPushButton(self.tab_3)
        self.teach_Previous_btn.setGeometry(QtCore.QRect(450, 720, 61, 21))
        self.teach_Previous_btn.setObjectName("teach_Previous_btn")
        self.teach_determine_btn = QtWidgets.QPushButton(self.tab_3)
        self.teach_determine_btn.setGeometry(QtCore.QRect(860, 720, 61, 21))
        self.teach_determine_btn.setObjectName("teach_determine_btn")
        self.teach_view = QtWidgets.QTableView(self.tab_3)
        self.teach_view.setGeometry(QtCore.QRect(10, 120, 911, 591))
        self.teach_view.setObjectName("teach_view")
        self.teach_view.verticalHeader().setVisible(False)
        self.tabWidget_5.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Class_firstpage_btn = QtWidgets.QPushButton(self.tab)
        self.Class_firstpage_btn.setEnabled(False)
        self.Class_firstpage_btn.setGeometry(QtCore.QRect(400, 720, 41, 21))
        self.Class_firstpage_btn.setObjectName("Class_firstpage_btn")
        self.Class_course_info_lab = QtWidgets.QLabel(self.tab)
        self.Class_course_info_lab.setGeometry(QtCore.QRect(230, 720, 161, 21))
        self.Class_course_info_lab.setObjectName("Class_course_info_lab")
        self.Class_next_btn = QtWidgets.QPushButton(self.tab)
        self.Class_next_btn.setEnabled(False)
        self.Class_next_btn.setGeometry(QtCore.QRect(520, 720, 61, 21))
        self.Class_next_btn.setObjectName("Class_next_btn")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 2, 911, 181))
        self.groupBox_14.setObjectName("groupBox_14")
        self.label_41 = QtWidgets.QLabel(self.groupBox_14)
        self.label_41.setGeometry(QtCore.QRect(10, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.Class_Academic_term_cob = QtWidgets.QComboBox(self.groupBox_14)
        self.Class_Academic_term_cob.setGeometry(QtCore.QRect(100, 40, 261, 20))
        self.Class_Academic_term_cob.setObjectName("Class_Academic_term_cob")
        self.label_42 = QtWidgets.QLabel(self.groupBox_14)
        self.label_42.setGeometry(QtCore.QRect(10, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.Class_Department_cob = QtWidgets.QComboBox(self.groupBox_14)
        self.Class_Department_cob.setGeometry(QtCore.QRect(100, 80, 241, 20))
        self.Class_Department_cob.setObjectName("Class_Department_cob")
        self.label_43 = QtWidgets.QLabel(self.groupBox_14)
        self.label_43.setGeometry(QtCore.QRect(10, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.Class_grade_cob = QtWidgets.QComboBox(self.groupBox_14)
        self.Class_grade_cob.setGeometry(QtCore.QRect(100, 120, 241, 20))
        self.Class_grade_cob.setObjectName("Class_grade_cob")
        self.label_44 = QtWidgets.QLabel(self.groupBox_14)
        self.label_44.setGeometry(QtCore.QRect(390, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.Class_class_cob = QtWidgets.QComboBox(self.groupBox_14)
        self.Class_class_cob.setGeometry(QtCore.QRect(460, 120, 241, 20))
        self.Class_class_cob.setObjectName("Class_class_cob")
        self.Class_class_cob.addItem("")
        self.label_46 = QtWidgets.QLabel(self.groupBox_14)
        self.label_46.setGeometry(QtCore.QRect(390, 70, 61, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.Class_profession_cob = QtWidgets.QComboBox(self.groupBox_14)
        self.Class_profession_cob.setGeometry(QtCore.QRect(460, 80, 241, 20))
        self.Class_profession_cob.setObjectName("Class_profession_cob")
        self.Class_profession_cob.addItem("")
        self.Class_query_btn = QtWidgets.QPushButton(self.groupBox_14)
        self.Class_query_btn.setGeometry(QtCore.QRect(350, 150, 81, 28))
        self.Class_query_btn.setObjectName("Class_query_btn")
        self.Class_Previous_btn = QtWidgets.QPushButton(self.tab)
        self.Class_Previous_btn.setEnabled(False)
        self.Class_Previous_btn.setGeometry(QtCore.QRect(450, 720, 61, 21))
        self.Class_Previous_btn.setObjectName("Class_Previous_btn")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(640, 720, 81, 21))
        self.label_45.setObjectName("label_45")
        self.Class_determine_btn = QtWidgets.QPushButton(self.tab)
        self.Class_determine_btn.setGeometry(QtCore.QRect(860, 720, 61, 21))
        self.Class_determine_btn.setObjectName("Class_determine_btn")
        self.Class_page_cob = QtWidgets.QComboBox(self.tab)
        self.Class_page_cob.setGeometry(QtCore.QRect(730, 720, 61, 21))
        self.Class_page_cob.setObjectName("Class_page_cob")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_page_cob.addItem("")
        self.Class_endpage_btn = QtWidgets.QPushButton(self.tab)
        self.Class_endpage_btn.setEnabled(False)
        self.Class_endpage_btn.setGeometry(QtCore.QRect(590, 720, 41, 21))
        self.Class_endpage_btn.setObjectName("Class_endpage_btn")
        self.Class_page_led = QtWidgets.QLineEdit(self.tab)
        self.Class_page_led.setGeometry(QtCore.QRect(800, 720, 51, 21))
        self.Class_page_led.setObjectName("Class_page_led")
        self.Class_view = QtWidgets.QTableView(self.tab)
        self.Class_view.setGeometry(QtCore.QRect(10, 190, 911, 521))
        self.Class_view.setObjectName("Class_view")
        self.Class_view.verticalHeader().setVisible(False)
        self.tabWidget_5.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.curriculum_page_led = QtWidgets.QLineEdit(self.tab_2)
        self.curriculum_page_led.setGeometry(QtCore.QRect(800, 720, 51, 21))
        self.curriculum_page_led.setObjectName("curriculum_page_led")
        self.curriculum_firstpage_btn = QtWidgets.QPushButton(self.tab_2)
        self.curriculum_firstpage_btn.setGeometry(QtCore.QRect(400, 720, 41, 21))
        self.curriculum_firstpage_btn.setObjectName("curriculum_firstpage_btn")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 2, 911, 181))
        self.groupBox_15.setObjectName("groupBox_15")
        self.label_47 = QtWidgets.QLabel(self.groupBox_15)
        self.label_47.setGeometry(QtCore.QRect(10, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.curriculum_Academic_term_cob = QtWidgets.QComboBox(self.groupBox_15)
        self.curriculum_Academic_term_cob.setGeometry(QtCore.QRect(100, 40, 261, 20))
        self.curriculum_Academic_term_cob.setObjectName("curriculum_Academic_term_cob")
        self.label_48 = QtWidgets.QLabel(self.groupBox_15)
        self.label_48.setGeometry(QtCore.QRect(10, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_15)
        self.label_49.setGeometry(QtCore.QRect(10, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_15)
        self.label_50.setGeometry(QtCore.QRect(380, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_15)
        self.label_51.setGeometry(QtCore.QRect(360, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.curriculum_Department_cob = QtWidgets.QComboBox(self.groupBox_15)
        self.curriculum_Department_cob.setGeometry(QtCore.QRect(460, 80, 241, 20))
        self.curriculum_Department_cob.setObjectName("curriculum_Department_cob")
        self.curriculum_query_btn = QtWidgets.QPushButton(self.groupBox_15)
        self.curriculum_query_btn.setGeometry(QtCore.QRect(330, 150, 81, 28))
        self.curriculum_query_btn.setObjectName("curriculum_query_btn")
        self.curriculum_course_name_led = QtWidgets.QLineEdit(self.groupBox_15)
        self.curriculum_course_name_led.setGeometry(QtCore.QRect(100, 80, 201, 21))
        self.curriculum_course_name_led.setObjectName("curriculum_course_name_led")
        self.curriculum_course_num_led = QtWidgets.QLineEdit(self.groupBox_15)
        self.curriculum_course_num_led.setGeometry(QtCore.QRect(100, 120, 201, 21))
        self.curriculum_course_num_led.setObjectName("curriculum_course_num_led")
        self.curriculum_curse_order_led = QtWidgets.QLineEdit(self.groupBox_15)
        self.curriculum_curse_order_led.setGeometry(QtCore.QRect(460, 120, 201, 21))
        self.curriculum_curse_order_led.setObjectName("curriculum_curse_order_led")
        self.curriculum_endpage_btn = QtWidgets.QPushButton(self.tab_2)
        self.curriculum_endpage_btn.setGeometry(QtCore.QRect(590, 720, 41, 21))
        self.curriculum_endpage_btn.setObjectName("curriculum_endpage_btn")
        self.curriculum_course_info_lab = QtWidgets.QLabel(self.tab_2)
        self.curriculum_course_info_lab.setGeometry(QtCore.QRect(230, 720, 161, 21))
        self.curriculum_course_info_lab.setObjectName("curriculum_course_info_lab")
        self.curriculum_determine_btn = QtWidgets.QPushButton(self.tab_2)
        self.curriculum_determine_btn.setGeometry(QtCore.QRect(860, 720, 61, 21))
        self.curriculum_determine_btn.setObjectName("curriculum_determine_btn")
        self.curriculum_next_btn = QtWidgets.QPushButton(self.tab_2)
        self.curriculum_next_btn.setGeometry(QtCore.QRect(520, 720, 61, 21))
        self.curriculum_next_btn.setObjectName("curriculum_next_btn")
        self.curriculum_page_cob = QtWidgets.QComboBox(self.tab_2)
        self.curriculum_page_cob.setGeometry(QtCore.QRect(730, 720, 61, 20))
        self.curriculum_page_cob.setObjectName("curriculum_page_cob")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_page_cob.addItem("")
        self.curriculum_Previous_btn = QtWidgets.QPushButton(self.tab_2)
        self.curriculum_Previous_btn.setGeometry(QtCore.QRect(450, 720, 61, 21))
        self.curriculum_Previous_btn.setObjectName("curriculum_Previous_btn")
        self.label_52 = QtWidgets.QLabel(self.tab_2)
        self.label_52.setGeometry(QtCore.QRect(640, 720, 81, 21))
        self.label_52.setObjectName("label_52")
        self.curriculum_view = QtWidgets.QTableView(self.tab_2)
        self.curriculum_view.setGeometry(QtCore.QRect(10, 190, 911, 521))
        self.curriculum_view.setObjectName("curriculum_view")
        self.curriculum_view.verticalHeader().setVisible(False)
        self.tabWidget_5.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.Resource, "")
        self.query = QtWidgets.QWidget()
        self.query.setObjectName("query")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.query)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 941, 801))
        self.tabWidget_4.setStyleSheet("\n"
"QTabBar::tab{height:25}\n"
"QTabBar::tab{width:134}")
        self.tabWidget_4.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.all_poss_grade_wid = QtWidgets.QWidget()
        self.all_poss_grade_wid.setObjectName("all_poss_grade_wid")
        self.layoutWidget1 = QtWidgets.QWidget(self.all_poss_grade_wid)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 931, 761))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scool_year_lwid = QtWidgets.QListWidget(self.layoutWidget1)
        self.scool_year_lwid.setMinimumSize(QtCore.QSize(230, 0))
        self.scool_year_lwid.setMaximumSize(QtCore.QSize(230, 16777215))
        self.scool_year_lwid.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.scool_year_lwid.setObjectName("scool_year_lwid")
        item = QtWidgets.QListWidgetItem()
        self.scool_year_lwid.addItem(item)
        self.horizontalLayout.addWidget(self.scool_year_lwid)
        self.stackedWidget = QtWidgets.QStackedWidget(self.layoutWidget1)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.all_passgarade_wid = QtWidgets.QWidget()
        self.all_passgarade_wid.setObjectName("all_passgarade_wid")
        self.garde_timer_lab = QtWidgets.QLabel(self.all_passgarade_wid)
        self.garde_timer_lab.setGeometry(QtCore.QRect(0, 10, 691, 41))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.garde_timer_lab.setFont(font)
        self.garde_timer_lab.setText("")
        self.garde_timer_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.garde_timer_lab.setObjectName("garde_timer_lab")
        self.allgarde_vie = QtWidgets.QTableView(self.all_passgarade_wid)
        self.allgarde_vie.setGeometry(QtCore.QRect(10, 50, 671, 711))
        self.allgarde_vie.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.allgarde_vie.setObjectName("allgarde_vie")
        self.allgarde_vie.verticalHeader().setVisible(False)
        self.stackedWidget.addWidget(self.all_passgarade_wid)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.tabWidget_4.addTab(self.all_poss_grade_wid, "")
        self.property_grade_wid = QtWidgets.QWidget()
        self.property_grade_wid.setObjectName("property_grade_wid")
        self.Compulsory_label = QtWidgets.QLabel(self.property_grade_wid)
        self.Compulsory_label.setGeometry(QtCore.QRect(0, 0, 931, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Compulsory_label.setFont(font)
        self.Compulsory_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Compulsory_label.setObjectName("Compulsory_label")
        self.Compulsory_view = QtWidgets.QTableView(self.property_grade_wid)
        self.Compulsory_view.setGeometry(QtCore.QRect(0, 20, 931, 351))
        self.Compulsory_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}\n"
"gridline-color: rgb(170, 255, 255);")
        self.Compulsory_view.setObjectName("Compulsory_view")
        self.Compulsory_view.verticalHeader().setVisible(False)
        self.Elective_view = QtWidgets.QTableView(self.property_grade_wid)
        self.Elective_view.setGeometry(QtCore.QRect(0, 430, 931, 91))
        self.Elective_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Elective_view.setObjectName("Elective_view")
        self.Elective_view.verticalHeader().setVisible(False)
        self.label_10 = QtWidgets.QLabel(self.property_grade_wid)
        self.label_10.setGeometry(QtCore.QRect(0, 400, 931, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.property_grade_wid)
        self.label_11.setGeometry(QtCore.QRect(0, 550, 931, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.Pick_view = QtWidgets.QTableView(self.property_grade_wid)
        self.Pick_view.setGeometry(QtCore.QRect(0, 580, 931, 151))
        self.Pick_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.Pick_view.setObjectName("Pick_view")
        self.Pick_view.verticalHeader().setVisible(False)
        self.Compulsory_info_lab = QtWidgets.QLabel(self.property_grade_wid)
        self.Compulsory_info_lab.setGeometry(QtCore.QRect(0, 369, 931, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Compulsory_info_lab.setFont(font)
        self.Compulsory_info_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 207, 164);")
        self.Compulsory_info_lab.setText("")
        self.Compulsory_info_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Compulsory_info_lab.setObjectName("Compulsory_info_lab")
        self.Elective_info_lab = QtWidgets.QLabel(self.property_grade_wid)
        self.Elective_info_lab.setGeometry(QtCore.QRect(0, 520, 931, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Elective_info_lab.setFont(font)
        self.Elective_info_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(167, 167, 167);")
        self.Elective_info_lab.setText("")
        self.Elective_info_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Elective_info_lab.setObjectName("Elective_info_lab")
        self.Pick_info_lab = QtWidgets.QLabel(self.property_grade_wid)
        self.Pick_info_lab.setGeometry(QtCore.QRect(0, 735, 931, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Pick_info_lab.setFont(font)
        self.Pick_info_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(167, 167, 167);")
        self.Pick_info_lab.setText("")
        self.Pick_info_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Pick_info_lab.setObjectName("Pick_info_lab")
        self.line_6 = QtWidgets.QFrame(self.property_grade_wid)
        self.line_6.setGeometry(QtCore.QRect(0, 542, 941, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.property_grade_wid)
        self.line_7.setGeometry(QtCore.QRect(0, 390, 941, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.tabWidget_4.addTab(self.property_grade_wid, "")
        self.plan_grade_wid = QtWidgets.QWidget()
        self.plan_grade_wid.setObjectName("plan_grade_wid")
        self.title_label = QtWidgets.QLabel(self.plan_grade_wid)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 921, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(12, 150, 255);")
        self.title_label.setObjectName("title_label")
        self.plan_score_view = QtWidgets.QTableView(self.plan_grade_wid)
        self.plan_score_view.setGeometry(QtCore.QRect(10, 50, 921, 591))
        self.plan_score_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}\n"
"gridline-color: rgb(170, 255, 255);")
        self.plan_score_view.setObjectName("plan_score_view")
        self.plan_score_view.verticalHeader().setVisible(False)
        self.plan_groupBox = QtWidgets.QGroupBox(self.plan_grade_wid)
        self.plan_groupBox.setGeometry(QtCore.QRect(10, 670, 921, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.plan_groupBox.setFont(font)
        self.plan_groupBox.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 170, 127);")
        self.plan_groupBox.setObjectName("plan_groupBox")
        self.plan_info_lab = QtWidgets.QLabel(self.plan_groupBox)
        self.plan_info_lab.setGeometry(QtCore.QRect(10, 30, 901, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.plan_info_lab.setFont(font)
        self.plan_info_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 255, 255);")
        self.plan_info_lab.setObjectName("plan_info_lab")
        self.plan_score_info_lab = QtWidgets.QLabel(self.plan_grade_wid)
        self.plan_score_info_lab.setGeometry(QtCore.QRect(10, 650, 921, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(7)
        self.plan_score_info_lab.setFont(font)
        self.plan_score_info_lab.setObjectName("plan_score_info_lab")
        self.tabWidget_4.addTab(self.plan_grade_wid, "")
        self.noposs_grade_wid = QtWidgets.QWidget()
        self.noposs_grade_wid.setObjectName("noposs_grade_wid")
        self.label_29 = QtWidgets.QLabel(self.noposs_grade_wid)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 911, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 36, 16);")
        self.label_29.setObjectName("label_29")
        self.now_nopass_viw = QtWidgets.QTableView(self.noposs_grade_wid)
        self.now_nopass_viw.setGeometry(QtCore.QRect(10, 50, 911, 231))
        self.now_nopass_viw.setObjectName("now_nopass_viw")
        self.now_nopass_viw.verticalHeader().setVisible(False)
        self.old_nopass_viw = QtWidgets.QTableView(self.noposs_grade_wid)
        self.old_nopass_viw.setGeometry(QtCore.QRect(10, 430, 911, 231))
        self.old_nopass_viw.setObjectName("old_nopass_viw")
        self.old_nopass_viw.verticalHeader().setVisible(False)
        self.label_30 = QtWidgets.QLabel(self.noposs_grade_wid)
        self.label_30.setGeometry(QtCore.QRect(10, 390, 911, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 0, 0);")
        self.label_30.setObjectName("label_30")
        self.now_nopass_lab = QtWidgets.QLabel(self.noposs_grade_wid)
        self.now_nopass_lab.setGeometry(QtCore.QRect(10, 290, 911, 31))
        self.now_nopass_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 225, 216);")
        self.now_nopass_lab.setObjectName("now_nopass_lab")
        self.old_nopass_lab = QtWidgets.QLabel(self.noposs_grade_wid)
        self.old_nopass_lab.setGeometry(QtCore.QRect(10, 670, 911, 31))
        self.old_nopass_lab.setStyleSheet("border-width: 1px;border-style: solid;\n"
"border-color: rgb(255, 225, 216);")
        self.old_nopass_lab.setObjectName("old_nopass_lab")
        self.tabWidget_4.addTab(self.noposs_grade_wid, "")
        self.semester_grade_wid = QtWidgets.QWidget()
        self.semester_grade_wid.setObjectName("semester_grade_wid")
        self.label_9 = QtWidgets.QLabel(self.semester_grade_wid)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 911, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(7, 31, 255);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.this_semester_view = QtWidgets.QTableView(self.semester_grade_wid)
        self.this_semester_view.setGeometry(QtCore.QRect(10, 50, 911, 701))
        self.this_semester_view.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.this_semester_view.setObjectName("this_semester_view")
        self.this_semester_view.verticalHeader().setVisible(False)
        self.tabWidget_4.addTab(self.semester_grade_wid, "")
        self.course_layout_wid = QtWidgets.QWidget()
        self.course_layout_wid.setObjectName("course_layout_wid")
        self.groupBox_11 = QtWidgets.QGroupBox(self.course_layout_wid)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 0, 911, 211))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_16 = QtWidgets.QLabel(self.groupBox_11)
        self.label_16.setGeometry(QtCore.QRect(120, 20, 71, 21))
        self.label_16.setObjectName("label_16")
        self.course_number_led = QtWidgets.QLineEdit(self.groupBox_11)
        self.course_number_led.setGeometry(QtCore.QRect(190, 20, 131, 21))
        self.course_number_led.setObjectName("course_number_led")
        self.course_name2_led = QtWidgets.QLineEdit(self.groupBox_11)
        self.course_name2_led.setGeometry(QtCore.QRect(400, 20, 131, 21))
        self.course_name2_led.setObjectName("course_name2_led")
        self.label_18 = QtWidgets.QLabel(self.groupBox_11)
        self.label_18.setGeometry(QtCore.QRect(330, 20, 71, 21))
        self.label_18.setObjectName("label_18")
        self.teach_led = QtWidgets.QLineEdit(self.groupBox_11)
        self.teach_led.setGeometry(QtCore.QRect(590, 20, 181, 21))
        self.teach_led.setObjectName("teach_led")
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setGeometry(QtCore.QRect(540, 20, 51, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_11)
        self.label_20.setGeometry(QtCore.QRect(120, 50, 72, 21))
        self.label_20.setObjectName("label_20")
        self.Department2_cob = QtWidgets.QComboBox(self.groupBox_11)
        self.Department2_cob.setGeometry(QtCore.QRect(190, 50, 131, 22))
        self.Department2_cob.setObjectName("Department2_cob")
        self.week_cob = QtWidgets.QComboBox(self.groupBox_11)
        self.week_cob.setGeometry(QtCore.QRect(400, 50, 131, 22))
        self.week_cob.setObjectName("week_cob")
        self.label_21 = QtWidgets.QLabel(self.groupBox_11)
        self.label_21.setGeometry(QtCore.QRect(330, 50, 72, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_11)
        self.label_22.setGeometry(QtCore.QRect(541, 50, 81, 21))
        self.label_22.setObjectName("label_22")
        self.class_num_cob = QtWidgets.QComboBox(self.groupBox_11)
        self.class_num_cob.setGeometry(QtCore.QRect(630, 50, 141, 22))
        self.class_num_cob.setObjectName("class_num_cob")
        self.Campus_cob = QtWidgets.QComboBox(self.groupBox_11)
        self.Campus_cob.setGeometry(QtCore.QRect(190, 80, 131, 22))
        self.Campus_cob.setObjectName("Campus_cob")
        self.Campus_cob.addItem("")
        self.Campus_cob.setItemText(0, "")
        self.Campus_cob.addItem("")
        self.Campus_cob.addItem("")
        self.label_23 = QtWidgets.QLabel(self.groupBox_11)
        self.label_23.setGeometry(QtCore.QRect(120, 80, 72, 21))
        self.label_23.setObjectName("label_23")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_11)
        self.comboBox_5.setGeometry(QtCore.QRect(480, 80, 31, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_24 = QtWidgets.QLabel(self.groupBox_11)
        self.label_24.setGeometry(QtCore.QRect(330, 80, 71, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_11)
        self.label_25.setGeometry(QtCore.QRect(440, 80, 41, 21))
        self.label_25.setObjectName("label_25")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_11)
        self.comboBox_6.setGeometry(QtCore.QRect(400, 80, 31, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_26 = QtWidgets.QLabel(self.groupBox_11)
        self.label_26.setGeometry(QtCore.QRect(520, 80, 131, 21))
        self.label_26.setObjectName("label_26")
        self.page_number_cob = QtWidgets.QComboBox(self.groupBox_11)
        self.page_number_cob.setGeometry(QtCore.QRect(650, 80, 121, 22))
        self.page_number_cob.setObjectName("page_number_cob")
        self.page_number_cob.addItem("")
        self.page_number_cob.addItem("")
        self.page_number_cob.addItem("")
        self.page_number_cob.addItem("")
        self.label_27 = QtWidgets.QLabel(self.groupBox_11)
        self.label_27.setGeometry(QtCore.QRect(320, 130, 121, 41))
        self.label_27.setObjectName("label_27")
        self.show_item_list_widget = QtWidgets.QListWidget(self.groupBox_11)
        self.show_item_list_widget.setGeometry(QtCore.QRect(440, 110, 91, 91))
        self.show_item_list_widget.setObjectName("show_item_list_widget")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton.setGeometry(QtCore.QRect(560, 130, 81, 51))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.course_layout_wid)
        self.tableView.setGeometry(QtCore.QRect(10, 220, 911, 501))
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.course_info2_lab = QtWidgets.QLabel(self.course_layout_wid)
        self.course_info2_lab.setGeometry(QtCore.QRect(490, 740, 111, 21))
        self.course_info2_lab.setText("")
        self.course_info2_lab.setObjectName("course_info2_lab")
        self.Previous2_btn = QtWidgets.QPushButton(self.course_layout_wid)
        self.Previous2_btn.setEnabled(False)
        self.Previous2_btn.setGeometry(QtCore.QRect(600, 730, 61, 21))
        self.Previous2_btn.setObjectName("Previous2_btn")
        self.next2_btn = QtWidgets.QPushButton(self.course_layout_wid)
        self.next2_btn.setEnabled(False)
        self.next2_btn.setGeometry(QtCore.QRect(670, 730, 61, 21))
        self.next2_btn.setObjectName("next2_btn")
        self.determine2_btn = QtWidgets.QPushButton(self.course_layout_wid)
        self.determine2_btn.setGeometry(QtCore.QRect(1120, 740, 61, 21))
        self.determine2_btn.setObjectName("determine2_btn")
        self.page2_led = QtWidgets.QLineEdit(self.course_layout_wid)
        self.page2_led.setGeometry(QtCore.QRect(800, 730, 51, 21))
        self.page2_led.setObjectName("page2_led")
        self.determine3_btn = QtWidgets.QPushButton(self.course_layout_wid)
        self.determine3_btn.setGeometry(QtCore.QRect(860, 730, 61, 21))
        self.determine3_btn.setObjectName("determine3_btn")
        self.label_28 = QtWidgets.QLabel(self.course_layout_wid)
        self.label_28.setGeometry(QtCore.QRect(740, 730, 51, 21))
        self.label_28.setObjectName("label_28")
        self.tabWidget_4.addTab(self.course_layout_wid, "")
        self.course_info_wid = QtWidgets.QWidget()
        self.course_info_wid.setObjectName("course_info_wid")
        self.groupBox_10 = QtWidgets.QGroupBox(self.course_info_wid)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 10, 911, 131))
        self.groupBox_10.setObjectName("groupBox_10")
        self.course_query_btn = QtWidgets.QPushButton(self.groupBox_10)
        self.course_query_btn.setGeometry(QtCore.QRect(730, 50, 71, 28))
        self.course_query_btn.setObjectName("course_query_btn")
        self.label_15 = QtWidgets.QLabel(self.groupBox_10)
        self.label_15.setGeometry(QtCore.QRect(420, 70, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.Course_num_led = QtWidgets.QLineEdit(self.groupBox_10)
        self.Course_num_led.setGeometry(QtCore.QRect(190, 70, 181, 21))
        self.Course_num_led.setObjectName("Course_num_led")
        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setGeometry(QtCore.QRect(110, 70, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.course_name_led = QtWidgets.QLineEdit(self.groupBox_10)
        self.course_name_led.setGeometry(QtCore.QRect(500, 70, 181, 21))
        self.course_name_led.setObjectName("course_name_led")
        self.category_cob = QtWidgets.QComboBox(self.groupBox_10)
        self.category_cob.setGeometry(QtCore.QRect(500, 40, 181, 22))
        self.category_cob.setObjectName("category_cob")
        self.label_12 = QtWidgets.QLabel(self.groupBox_10)
        self.label_12.setGeometry(QtCore.QRect(110, 40, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.Department_cob = QtWidgets.QComboBox(self.groupBox_10)
        self.Department_cob.setGeometry(QtCore.QRect(190, 40, 181, 22))
        self.Department_cob.setObjectName("Department_cob")
        self.label_13 = QtWidgets.QLabel(self.groupBox_10)
        self.label_13.setGeometry(QtCore.QRect(420, 40, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.course_info_lab = QtWidgets.QLabel(self.course_info_wid)
        self.course_info_lab.setGeometry(QtCore.QRect(200, 720, 191, 21))
        self.course_info_lab.setObjectName("course_info_lab")
        self.Previous_btn = QtWidgets.QPushButton(self.course_info_wid)
        self.Previous_btn.setGeometry(QtCore.QRect(450, 720, 61, 21))
        self.Previous_btn.setObjectName("Previous_btn")
        self.next_btn = QtWidgets.QPushButton(self.course_info_wid)
        self.next_btn.setGeometry(QtCore.QRect(520, 720, 61, 21))
        self.next_btn.setObjectName("next_btn")
        self.label_17 = QtWidgets.QLabel(self.course_info_wid)
        self.label_17.setGeometry(QtCore.QRect(640, 720, 81, 21))
        self.label_17.setObjectName("label_17")
        self.page_cob = QtWidgets.QComboBox(self.course_info_wid)
        self.page_cob.setGeometry(QtCore.QRect(730, 722, 61, 20))
        self.page_cob.setObjectName("page_cob")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.page_cob.addItem("")
        self.determine_btn = QtWidgets.QPushButton(self.course_info_wid)
        self.determine_btn.setGeometry(QtCore.QRect(860, 720, 61, 21))
        self.determine_btn.setObjectName("determine_btn")
        self.page_led = QtWidgets.QLineEdit(self.course_info_wid)
        self.page_led.setGeometry(QtCore.QRect(800, 720, 51, 21))
        self.page_led.setObjectName("page_led")
        self.firstpage_btn = QtWidgets.QPushButton(self.course_info_wid)
        self.firstpage_btn.setGeometry(QtCore.QRect(400, 720, 41, 21))
        self.firstpage_btn.setObjectName("firstpage_btn")
        self.endpage_btn = QtWidgets.QPushButton(self.course_info_wid)
        self.endpage_btn.setGeometry(QtCore.QRect(590, 720, 41, 21))
        self.endpage_btn.setObjectName("endpage_btn")
        self.select_course_viw = QtWidgets.QTableView(self.course_info_wid)
        self.select_course_viw.setGeometry(QtCore.QRect(10, 150, 911, 561))
        self.select_course_viw.setObjectName("select_course_viw")
        self.select_course_viw.verticalHeader().setVisible(False)
        self.tabWidget_4.addTab(self.course_info_wid, "")
        self.tabWidget.addTab(self.query, "")
        self.Grade_point = QtWidgets.QWidget()
        self.Grade_point.setObjectName("Grade_point")
        self.groupBox_7 = QtWidgets.QGroupBox(self.Grade_point)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 0, 921, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 311, 41))
        self.label_5.setStyleSheet("\n"
"border-color: rgb(5, 92, 255);\n"
"border-width: 1px;border-style: solid;")
        self.label_5.setObjectName("label_5")
        self.grade_point_led = QtWidgets.QLineEdit(self.groupBox_7)
        self.grade_point_led.setGeometry(QtCore.QRect(220, 40, 81, 20))
        self.grade_point_led.setReadOnly(True)
        self.grade_point_led.setObjectName("grade_point_led")
        self.groupBox_8 = QtWidgets.QGroupBox(self.Grade_point)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 80, 921, 631))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.group_point_view = QtWidgets.QTableView(self.groupBox_8)
        self.group_point_view.setGeometry(QtCore.QRect(10, 30, 411, 591))
        self.group_point_view.setObjectName("group_point_view")
        self.group_point_view.verticalHeader().setVisible(False)
        self.loading_lab = QtWidgets.QLabel(self.groupBox_8)
        self.loading_lab.setGeometry(QtCore.QRect(460, 220, 411, 181))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(18)
        self.loading_lab.setFont(font)
        self.loading_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_lab.setObjectName("loading_lab")
        self.groupBox_9 = QtWidgets.QGroupBox(self.Grade_point)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 710, 921, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_6.setObjectName("label_6")
        self.start_cmbox = QtWidgets.QComboBox(self.groupBox_9)
        self.start_cmbox.setGeometry(QtCore.QRect(110, 40, 191, 22))
        self.start_cmbox.setObjectName("start_cmbox")
        self.end_cmbox = QtWidgets.QComboBox(self.groupBox_9)
        self.end_cmbox.setGeometry(QtCore.QRect(410, 40, 181, 22))
        self.end_cmbox.setObjectName("end_cmbox")
        self.label_7 = QtWidgets.QLabel(self.groupBox_9)
        self.label_7.setGeometry(QtCore.QRect(310, 30, 101, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_9)
        self.label_8.setGeometry(QtCore.QRect(600, 30, 111, 41))
        self.label_8.setObjectName("label_8")
        self.group_point_lne = QtWidgets.QLineEdit(self.groupBox_9)
        self.group_point_lne.setGeometry(QtCore.QRect(720, 40, 111, 21))
        self.group_point_lne.setReadOnly(True)
        self.group_point_lne.setObjectName("group_point_lne")
        self.query_group_point_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.query_group_point_btn.setGeometry(QtCore.QRect(840, 30, 71, 41))
        self.query_group_point_btn.setObjectName("query_group_point_btn")
        self.tabWidget.addTab(self.Grade_point, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.group_server = QtWidgets.QGroupBox(self.About)
        self.group_server.setGeometry(QtCore.QRect(510, 20, 411, 761))
        self.group_server.setObjectName("group_server")
        self.pushButton_2 = QtWidgets.QPushButton(self.group_server)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 371, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.group_server)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 180, 371, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.group_server)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 340, 371, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.group_server)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 500, 371, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.group_server)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 650, 371, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_16 = QtWidgets.QGroupBox(self.About)
        self.groupBox_16.setGeometry(QtCore.QRect(20, 20, 411, 761))
        self.groupBox_16.setObjectName("groupBox_16")
        self.label_53 = QtWidgets.QLabel(self.groupBox_16)
        self.label_53.setGeometry(QtCore.QRect(20, 60, 381, 211))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(28)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_16)
        self.label_54.setGeometry(QtCore.QRect(10, 290, 381, 221))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(28)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_16)
        self.label_55.setGeometry(QtCore.QRect(10, 550, 381, 181))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(36)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.tabWidget.addTab(self.About, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_2.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.classroom_page_cob.setCurrentIndex(1)
        self.teach_page_cob.setCurrentIndex(1)
        self.Class_page_cob.setCurrentIndex(1)
        self.curriculum_page_cob.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.scool_year_lwid.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)
        self.page_cob.setCurrentIndex(1)
        self.change_btn.clicked.connect(Form.alter_info)
        self.plan_btn.clicked.connect(Form.Training_program)
        self.query_group_point_btn.clicked.connect(Form.query_fixed_timer_grade_point)
        self.Previous2_btn.clicked.connect(Form.ret_firstpage)
        self.endpage_btn.clicked.connect(Form.return_endpage)
        self.course_query_btn.clicked.connect(Form.course_query)
        self.page_cob.currentIndexChanged['QString'].connect(Form.set_view_page_num)
        self.scool_year_lwid.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.pushButton.clicked.connect(Form.query_course_arrange_info)
        self.firstpage_btn.clicked.connect(Form.return_firstpage)
        self.next2_btn.clicked.connect(Form.ret_endpage)
        self.next_btn.clicked.connect(Form.ret_next_page)
        self.Previous_btn.clicked.connect(Form.ret_front_page)
        self.teach_query_btn.clicked.connect(Form.query_teacher_info)
        self.classroom_Campus_cob.currentIndexChanged['int'].connect(Form.show_teaching_building)
        self.teach_next_btn.clicked.connect(Form.ret_teacher_Next)
        self.classroom_endpage_btn.clicked.connect(Form.ret_classroom_curriculum_end)
        self.curriculum_query_btn.clicked.connect(Form.query_course_curriculum_info)
        self.classroom_firstpage_btn.clicked.connect(Form.ret_classroom_curriculum_first)
        self.teach_Previous_btn.clicked.connect(Form.ret_teacher_Previous)
        self.teach_firstpage_btn.clicked.connect(Form.ret_teacher_first)
        self.classroom_Teaching_building_cob.currentIndexChanged['int'].connect(Form.show_classroom)
        self.classroom_next_btn.clicked.connect(Form.ret_classroom_curriculum_next)
        self.Previous_btn_2.clicked.connect(Form.ret_classroom_curriculum_Previous)
        self.classroom_query_btn.clicked.connect(Form.query_classroom_curriculum)
        self.teach_endpage_btn.clicked.connect(Form.ret_teacher_end)
        self.Class_Department_cob.currentIndexChanged['int'].connect(Form.show_profession_info)
        self.Class_query_btn.clicked.connect(Form.query_class_info)
        self.curriculum_next_btn.clicked.connect(Form.ret_course_Next)
        self.Class_grade_cob.currentIndexChanged['int'].connect(Form.show_class_info)
        self.curriculum_firstpage_btn.clicked.connect(Form.ret_course_first)
        self.Class_Previous_btn.clicked.connect(Form.ret_class_Previous)
        self.Class_next_btn.clicked.connect(Form.ret_class_Next)
        self.curriculum_Previous_btn.clicked.connect(Form.ret_course_Previous)
        self.curriculum_endpage_btn.clicked.connect(Form.ret_course_End)
        self.Class_firstpage_btn.clicked.connect(Form.ret_class_first)
        self.Class_endpage_btn.clicked.connect(Form.ret_class_End)
        self.pushButton_2.clicked.connect(Form.show_School_calendar)
        self.pushButton_3.clicked.connect(Form.show_Suspension_Page)
        self.pushButton_4.clicked.connect(Form.show_return_to_school)
        self.pushButton_5.clicked.connect(Form.show_Drop_out_school)
        self.pushButton_6.clicked.connect(Form.show_Reissue_degree)
        self.Planning_course_btn.clicked.connect(Form.show_planning_course_page)
        self.Program_course_btn.clicked.connect(Form.show_program_course_page)
        self.Elective_course_btn.clicked.connect(Form.show_elective_course_page)
        self.School_elective_course_btn.clicked.connect(Form.show_school_elective_course_page)
        self.free_choice_course_btn.clicked.connect(Form.show_free_choice_course_page)
        self.Rehearsal_course_btn.clicked.connect(Form.show_rehearsal_course_page)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "聊城大学教务系统"))
        self.groupBox.setTitle(_translate("Form", "基本信息"))
        self.groupBox_2.setTitle(_translate("Form", "个人培养方案"))
        self.label_2.setText(_translate("Form", "学籍信息"))
        self.change_btn.setText(_translate("Form", "修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Homepage), _translate("Form", "个人主页"))
        self.groupBox_4.setTitle(_translate("Form", "提示："))
        self.pushButton_7.setText(_translate("Form", "确定"))
        self.pushButton_8.setText(_translate("Form", "取消"))
        self.label_56.setText(_translate("Form", "计划学年学期"))
        self.comboBox.setItemText(1, _translate("Form", "2018-2019学年第一学期(两学期)"))
        self.comboBox.setItemText(2, _translate("Form", "2018-2019学年第二学期(两学期)"))
        self.comboBox.setItemText(3, _translate("Form", "2019-2020学年第一学期(两学期)"))
        self.comboBox.setItemText(4, _translate("Form", "2019-2020学年第二学期(两学期)"))
        self.comboBox.setItemText(5, _translate("Form", "2020-2021学年第一学期(两学期)"))
        self.comboBox.setItemText(6, _translate("Form", "2020-2021学年第二学期(两学期)"))
        self.comboBox.setItemText(7, _translate("Form", "2021-2022学年第一学期(两学期)"))
        self.comboBox.setItemText(8, _translate("Form", "2021-2022学年第二学期(两学期)"))
        self.comboBox_2.setItemText(1, _translate("Form", "限选"))
        self.comboBox_2.setItemText(2, _translate("Form", "必修"))
        self.comboBox_2.setItemText(3, _translate("Form", "选修"))
        self.comboBox_2.setItemText(4, _translate("Form", "任选"))
        self.comboBox_2.setItemText(5, _translate("Form", "辅修"))
        self.label_57.setText(_translate("Form", "课程属性"))
        self.pushButton_9.setText(_translate("Form", "搜索"))
        self.pushButton_10.setText(_translate("Form", "确认"))
        self.pushButton_11.setText(_translate("Form", "取消"))
        self.pushButton_12.setText(_translate("Form", "确认"))
        self.pushButton_13.setText(_translate("Form", "取消"))
        self.pushButton_14.setText(_translate("Form", "确认"))
        self.pushButton_15.setText(_translate("Form", "取消"))
        self.label_58.setText(_translate("Form", "课程号:"))
        self.label_59.setText(_translate("Form", "课序号:"))
        self.label_60.setText(_translate("Form", "课程名:"))
        self.label_61.setText(_translate("Form", "教师:"))
        self.label_62.setText(_translate("Form", "开课系:"))
        self.label_63.setText(_translate("Form", "上课星期:"))
        self.label_64.setText(_translate("Form", "上课节次:"))
        self.pushButton_16.setText(_translate("Form", "确定"))
        self.pushButton_17.setText(_translate("Form", "取消"))
        self.pushButton_18.setText(_translate("Form", "确认"))
        self.pushButton_19.setText(_translate("Form", "取消"))
        self.pushButton_20.setText(_translate("Form", "确认"))
        self.Planning_course_btn.setText(_translate("Form", "计划课程"))
        self.Program_course_btn.setText(_translate("Form", "方案课程"))
        self.Elective_course_btn.setText(_translate("Form", "系任选课"))
        self.School_elective_course_btn.setText(_translate("Form", "校任选课"))
        self.free_choice_course_btn.setText(_translate("Form", "自由选择"))
        self.Rehearsal_course_btn.setText(_translate("Form", "重修课程"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Elective_course), _translate("Form", "网上选课"))
        self.course_res_lab.setText(_translate("Form", "选课结果(已安排时间地点)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Elective_course_res), _translate("Form", "选课结果"))
        self.groupBox_6.setTitle(_translate("Form", "提示："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Withdrawal), _translate("Form", "退课"))
        self.groupBox_5.setTitle(_translate("Form", "提示："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Invalid_Elective), _translate("Form", "无效的选课结果"))
        self.course_res_lab_2.setText(_translate("Form", "选课结果(已安排时间地点)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Class_Schedule), _translate("Form", "本学期课表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Course), _translate("Form", "选课管理"))
        self.post_lab.setText(_translate("Form", "暂时没公告"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.evaluate_post_wid), _translate("Form", "评估公告"))
        self.teaching_lab.setText(_translate("Form", "非教学评估时期，或评估时间已过。"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.teaching_evaluate_wid), _translate("Form", "教学评估"))
        self.graduate_evaluate_lab.setText(_translate("Form", "现在不能进行评估"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.graduate_evaluate_wid), _translate("Form", "毕业生评估"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assess), _translate("Form", "教学评估"))
        self.groupBox_12.setTitle(_translate("Form", "列表"))
        self.label_31.setText(_translate("Form", "学年学期:"))
        self.label_32.setText(_translate("Form", "校区:"))
        self.label_33.setText(_translate("Form", "教学楼:"))
        self.label_34.setText(_translate("Form", "教室:"))
        self.classroom_query_btn.setText(_translate("Form", "查询"))
        self.classroom_firstpage_btn.setText(_translate("Form", "首页"))
        self.classroom_endpage_btn.setText(_translate("Form", "末页"))
        self.Previous_btn_2.setText(_translate("Form", "上一页"))
        self.classroom_next_btn.setText(_translate("Form", "下一页"))
        self.label_35.setText(_translate("Form", "每页记录数:"))
        self.classroom_course_info_lab.setText(_translate("Form", "共0项  第1/0页"))
        self.classroom_determine_btn.setText(_translate("Form", "确定"))
        self.classroom_page_cob.setItemText(0, _translate("Form", "10项"))
        self.classroom_page_cob.setItemText(1, _translate("Form", "20项"))
        self.classroom_page_cob.setItemText(2, _translate("Form", "30项"))
        self.classroom_page_cob.setItemText(3, _translate("Form", "40项"))
        self.classroom_page_cob.setItemText(4, _translate("Form", "50项"))
        self.classroom_page_cob.setItemText(5, _translate("Form", "100项"))
        self.classroom_page_cob.setItemText(6, _translate("Form", "200项"))
        self.classroom_page_cob.setItemText(7, _translate("Form", "300项"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_4), _translate("Form", "教室课表"))
        self.teach_firstpage_btn.setText(_translate("Form", "首页"))
        self.teach_endpage_btn.setText(_translate("Form", "末页"))
        self.label_36.setText(_translate("Form", "每页记录数:"))
        self.teach_next_btn.setText(_translate("Form", "下一页"))
        self.teach_page_cob.setItemText(0, _translate("Form", "10项"))
        self.teach_page_cob.setItemText(1, _translate("Form", "20项"))
        self.teach_page_cob.setItemText(2, _translate("Form", "30项"))
        self.teach_page_cob.setItemText(3, _translate("Form", "40项"))
        self.teach_page_cob.setItemText(4, _translate("Form", "50项"))
        self.teach_page_cob.setItemText(5, _translate("Form", "100项"))
        self.teach_page_cob.setItemText(6, _translate("Form", "200项"))
        self.teach_page_cob.setItemText(7, _translate("Form", "300项"))
        self.teach_course_info_lab.setText(_translate("Form", "共0项  第1/0页"))
        self.groupBox_13.setTitle(_translate("Form", "列表"))
        self.label_37.setText(_translate("Form", "学年学期:"))
        self.label_38.setText(_translate("Form", "院系:"))
        self.label_40.setText(_translate("Form", "教师名:"))
        self.label_39.setText(_translate("Form", "提示：输入框支持模糊查询"))
        self.teach_query_btn.setText(_translate("Form", "查询"))
        self.teach_Previous_btn.setText(_translate("Form", "上一页"))
        self.teach_determine_btn.setText(_translate("Form", "确定"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_3), _translate("Form", "教师课表"))
        self.Class_firstpage_btn.setText(_translate("Form", "首页"))
        self.Class_course_info_lab.setText(_translate("Form", "共0项  第1/0页"))
        self.Class_next_btn.setText(_translate("Form", "下一页"))
        self.groupBox_14.setTitle(_translate("Form", "列表"))
        self.label_41.setText(_translate("Form", "学年学期:"))
        self.label_42.setText(_translate("Form", "院系:"))
        self.label_43.setText(_translate("Form", "年级:"))
        self.label_44.setText(_translate("Form", "班级:"))
        self.Class_class_cob.setItemText(0, _translate("Form", "请选择"))
        self.label_46.setText(_translate("Form", "专业:"))
        self.Class_profession_cob.setItemText(0, _translate("Form", "请选择"))
        self.Class_query_btn.setText(_translate("Form", "查询"))
        self.Class_Previous_btn.setText(_translate("Form", "上一页"))
        self.label_45.setText(_translate("Form", "每页记录数:"))
        self.Class_determine_btn.setText(_translate("Form", "确定"))
        self.Class_page_cob.setItemText(0, _translate("Form", "10项"))
        self.Class_page_cob.setItemText(1, _translate("Form", "20项"))
        self.Class_page_cob.setItemText(2, _translate("Form", "30项"))
        self.Class_page_cob.setItemText(3, _translate("Form", "40项"))
        self.Class_page_cob.setItemText(4, _translate("Form", "50项"))
        self.Class_page_cob.setItemText(5, _translate("Form", "100项"))
        self.Class_page_cob.setItemText(6, _translate("Form", "200项"))
        self.Class_page_cob.setItemText(7, _translate("Form", "300项"))
        self.Class_endpage_btn.setText(_translate("Form", "末页"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab), _translate("Form", "班级课表"))
        self.curriculum_firstpage_btn.setText(_translate("Form", "首页"))
        self.groupBox_15.setTitle(_translate("Form", "列表"))
        self.label_47.setText(_translate("Form", "学年学期:"))
        self.label_48.setText(_translate("Form", "课程名:"))
        self.label_49.setText(_translate("Form", "课程号:"))
        self.label_50.setText(_translate("Form", "课序号:"))
        self.label_51.setText(_translate("Form", "开课系所:"))
        self.curriculum_query_btn.setText(_translate("Form", "查询"))
        self.curriculum_endpage_btn.setText(_translate("Form", "末页"))
        self.curriculum_course_info_lab.setText(_translate("Form", "共0项  第1/0页"))
        self.curriculum_determine_btn.setText(_translate("Form", "确定"))
        self.curriculum_next_btn.setText(_translate("Form", "下一页"))
        self.curriculum_page_cob.setItemText(0, _translate("Form", "10项"))
        self.curriculum_page_cob.setItemText(1, _translate("Form", "20项"))
        self.curriculum_page_cob.setItemText(2, _translate("Form", "30项"))
        self.curriculum_page_cob.setItemText(3, _translate("Form", "40项"))
        self.curriculum_page_cob.setItemText(4, _translate("Form", "50项"))
        self.curriculum_page_cob.setItemText(5, _translate("Form", "100项"))
        self.curriculum_page_cob.setItemText(6, _translate("Form", "200项"))
        self.curriculum_page_cob.setItemText(7, _translate("Form", "300项"))
        self.curriculum_Previous_btn.setText(_translate("Form", "上一页"))
        self.label_52.setText(_translate("Form", "每页记录数:"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_2), _translate("Form", "课程课表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resource), _translate("Form", "教学资源"))
        __sortingEnabled = self.scool_year_lwid.isSortingEnabled()
        self.scool_year_lwid.setSortingEnabled(False)
        item = self.scool_year_lwid.item(0)
        item.setText(_translate("Form", "全部学期的及格成绩"))
        self.scool_year_lwid.setSortingEnabled(__sortingEnabled)
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.all_poss_grade_wid), _translate("Form", "全部及格成绩"))
        self.Compulsory_label.setText(_translate("Form", "必修"))
        self.label_10.setText(_translate("Form", "选修"))
        self.label_11.setText(_translate("Form", "任选"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.property_grade_wid), _translate("Form", "课程属性成绩"))
        self.title_label.setText(_translate("Form", "TextLabel"))
        self.plan_groupBox.setTitle(_translate("Form", "GroupBox"))
        self.plan_info_lab.setText(_translate("Form", "TextLabel"))
        self.plan_score_info_lab.setText(_translate("Form", "TextLabel"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.plan_grade_wid), _translate("Form", "方案成绩"))
        self.label_29.setText(_translate("Form", "尚不及格"))
        self.label_30.setText(_translate("Form", "曾不及格"))
        self.now_nopass_lab.setText(_translate("Form", "TextLabel"))
        self.old_nopass_lab.setText(_translate("Form", "TextLabel"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.noposs_grade_wid), _translate("Form", "不及格成绩"))
        self.label_9.setText(_translate("Form", "本学期成绩查询列表"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.semester_grade_wid), _translate("Form", "本学期成绩"))
        self.groupBox_11.setTitle(_translate("Form", "课程查询"))
        self.label_16.setText(_translate("Form", "课程号:"))
        self.label_18.setText(_translate("Form", "课程名:"))
        self.label_19.setText(_translate("Form", "教师:"))
        self.label_20.setText(_translate("Form", "开课系所:"))
        self.label_21.setText(_translate("Form", "上课星期:"))
        self.label_22.setText(_translate("Form", "上课节次:"))
        self.Campus_cob.setItemText(1, _translate("Form", "东校区"))
        self.Campus_cob.setItemText(2, _translate("Form", "西校区"))
        self.label_23.setText(_translate("Form", "校区:"))
        self.label_24.setText(_translate("Form", "教学楼:"))
        self.label_25.setText(_translate("Form", "教室:"))
        self.label_26.setText(_translate("Form", "每页显示的记录数:"))
        self.page_number_cob.setItemText(0, _translate("Form", "20项"))
        self.page_number_cob.setItemText(1, _translate("Form", "30项"))
        self.page_number_cob.setItemText(2, _translate("Form", "40项"))
        self.page_number_cob.setItemText(3, _translate("Form", "50项"))
        self.label_27.setText(_translate("Form", "选择要显示的列:"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.Previous2_btn.setText(_translate("Form", "上一页"))
        self.next2_btn.setText(_translate("Form", "下一页"))
        self.determine2_btn.setText(_translate("Form", "确定"))
        self.determine3_btn.setText(_translate("Form", "跳转"))
        self.label_28.setText(_translate("Form", "页数："))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.course_layout_wid), _translate("Form", "本学期课程安排"))
        self.groupBox_10.setTitle(_translate("Form", "列表"))
        self.course_query_btn.setText(_translate("Form", "查询"))
        self.label_15.setText(_translate("Form", "课程名:"))
        self.label_14.setText(_translate("Form", "课程号:"))
        self.label_12.setText(_translate("Form", "开课院系:"))
        self.label_13.setText(_translate("Form", "课程类别:"))
        self.course_info_lab.setText(_translate("Form", "TextLabel"))
        self.Previous_btn.setText(_translate("Form", "上一页"))
        self.next_btn.setText(_translate("Form", "下一页"))
        self.label_17.setText(_translate("Form", "每页记录数:"))
        self.page_cob.setItemText(0, _translate("Form", "10项"))
        self.page_cob.setItemText(1, _translate("Form", "20项"))
        self.page_cob.setItemText(2, _translate("Form", "30项"))
        self.page_cob.setItemText(3, _translate("Form", "40项"))
        self.page_cob.setItemText(4, _translate("Form", "50项"))
        self.page_cob.setItemText(5, _translate("Form", "100项"))
        self.page_cob.setItemText(6, _translate("Form", "200项"))
        self.page_cob.setItemText(7, _translate("Form", "300项"))
        self.determine_btn.setText(_translate("Form", "确定"))
        self.firstpage_btn.setText(_translate("Form", "首页"))
        self.endpage_btn.setText(_translate("Form", "末页"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.course_info_wid), _translate("Form", "课程基本信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query), _translate("Form", "综合查询"))
        self.groupBox_7.setTitle(_translate("Form", "学分绩点查询"))
        self.label_5.setText(_translate("Form", "截至现在您获得的学分绩点为:"))
        self.groupBox_8.setTitle(_translate("Form", "学期学分绩点明细"))
        self.loading_lab.setText(_translate("Form", "正在计算绩点中...请稍等....."))
        self.groupBox_9.setTitle(_translate("Form", "期间学分绩点查询"))
        self.label_6.setText(_translate("Form", "开始学年学期:"))
        self.label_7.setText(_translate("Form", "结束学年学期:"))
        self.label_8.setText(_translate("Form", "期间学分绩点值:"))
        self.group_point_lne.setText(_translate("Form", "0"))
        self.query_group_point_btn.setText(_translate("Form", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Grade_point), _translate("Form", "学分绩点"))
        self.group_server.setTitle(_translate("Form", "综合信息服务"))
        self.pushButton_2.setText(_translate("Form", "聊城大学校历"))
        self.pushButton_3.setText(_translate("Form", "学生休学办理流程"))
        self.pushButton_4.setText(_translate("Form", "学生复学办理流程"))
        self.pushButton_5.setText(_translate("Form", "学生退学办理流程"))
        self.pushButton_6.setText(_translate("Form", "补办毕业(学位)证明书流程"))
        self.groupBox_16.setTitle(_translate("Form", "关于"))
        self.label_53.setText(_translate("Form", "BY:…-.-*…"))
        self.label_54.setText(_translate("Form", "QQ:1960622196"))
        self.label_55.setText(_translate("Form", "感谢支持"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("Form", "关于"))

