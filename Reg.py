import Resources
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPropertyAnimation, QSequentialAnimationGroup, QRect, QTimer
from WriterMain import WriterUI
from TDLMain import TDL_UI
import pymysql as sql
from Data_Extractor import DB_Data
import sys

class Welcome_Text(QLabel):
        def __init__(self,parent=None):
                super(Welcome_Text, self).__init__(parent)
                self.setMaximumSize(QtCore.QSize(16777215, 50))
                self.setStyleSheet("color:white;\n"
                                                "")
                self.setObjectName("WelcomeText")
                self.setText("Welcome to Fiesta Content Solution Registeration Form")
                self.i = 0
                self.timer=QTimer()
                self.timer.timeout.connect(self.showTime)
                self.login = [" ","L","o","g","i","n"," ","F","o","r","m"] 
        def showTime(self):
                self.previous_text = self.text()
                if self.previous_text != "Welcome to Fiesta Content Solution":
                        self.previous_text = self.previous_text[:-1]
                        self.setText(self.previous_text)                
                # elif self.previous_text = "Welcome to Fiesta Content Solution":
        def startTimer(self):
                self.timer.start(100)
        def endTimer(self):
                self.timer.stop()
class RegisterationUI(object):
        def __init__(self):
                app = QtWidgets.QApplication(sys.argv)
                self.MainWindow = QtWidgets.QMainWindow()
                self.setupUi(self.MainWindow)
                self.MainWindow.show()
                sys.exit(app.exec_()) 
        def setupUi(self, MainWindow):
                self.i = 0
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(960, 743)
                MainWindow.setMaximumSize(QtCore.QSize(1200, 743))
                MainWindow.setStyleSheet("")
                MainWindow.setWindowFlag(Qt.FramelessWindowHint)
                MainWindow.setAttribute(Qt.WA_TranslucentBackground)
                self.RegisteringAndLogin = QtWidgets.QWidget(MainWindow)
                self.RegisteringAndLogin.setStyleSheet("QLineEdit{\n"
                                                "border-radius:5px;\n"
                                                "border: 2px solid grey;\n"
                                                "background-color:lightgrey;\n"
                                                "padding: 10px;\n"
                                                "}\n"
                                                "QLineEdit:focus{\n"
                                                "border: 2px solid black;\n"
                                                "background-color:white;\n"
                                                "}\n"
                                                "QComboBox{\n"
                                                "border-radius:5px;\n"
                                                "border: 2px solid grey;\n"
                                                "background-color:lightgrey;\n"
                                                "padding: 10px;\n"
                                                "}\n"
                                                "QComboBox:focus{\n"
                                                "border: 2px solid black;\n"
                                                "background-color:white;\n"
                                                "}\n"
                                                "")
                self.RegisteringAndLogin.setObjectName("RegisteringAndLogin")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.RegisteringAndLogin)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.RegWidget = QtWidgets.QWidget(self.RegisteringAndLogin)
                self.RegWidget.setMaximumSize(QtCore.QSize(16777215, 725))
                self.RegWidget.setStyleSheet(
                "background-color: black; border-radius:15px;")
                self.RegWidget.setObjectName("RegWidget")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.RegWidget)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.UpperPanel = QtWidgets.QWidget(self.RegWidget)
                self.UpperPanel.setMaximumSize(QtCore.QSize(16777215, 40))
                self.UpperPanel.setStyleSheet("border: 2px solid black;\n"
                                        "background-color: lightblue;\n"
                                        "")
                self.UpperPanel.setObjectName("UpperPanel")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.UpperPanel)
                self.horizontalLayout.setObjectName("horizontalLayout")
                spacerItem = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem)
                self.UpperPanelMinimizeButton = QtWidgets.QPushButton(self.UpperPanel)
                self.UpperPanelMinimizeButton.setStyleSheet("#UpperPanelMinimizeButton{border:none}\n"
                                                        ":hover{\n"
                                                        "background-color:lightgreen;\n"
                                                        "}\n"
                                                        "")
                self.UpperPanelMinimizeButton.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/minus.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpperPanelMinimizeButton.setIcon(icon)
                self.UpperPanelMinimizeButton.setIconSize(QtCore.QSize(25, 25))
                self.UpperPanelMinimizeButton.setObjectName("UpperPanelMinimizeButton")
                self.horizontalLayout.addWidget(self.UpperPanelMinimizeButton)
                self.UpperPanelCloseButton = QtWidgets.QPushButton(self.UpperPanel)
                self.UpperPanelCloseButton.setStyleSheet("#UpperPanelCloseButton{\n"
                                                        "border: none;\n"
                                                        "}\n"
                                                        ":hover{\n"
                                                        "background-color: red;\n"
                                                        "border-radius:10px;\n"
                                                        "}")
                self.UpperPanelCloseButton.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/x-square.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpperPanelCloseButton.setIcon(icon1)
                self.UpperPanelCloseButton.setIconSize(QtCore.QSize(25, 25))
                self.UpperPanelCloseButton.setObjectName("UpperPanelCloseButton")
                self.horizontalLayout.addWidget(self.UpperPanelCloseButton)
                self.verticalLayout_5.addWidget(self.UpperPanel)
                self.WelcomeContainer = QtWidgets.QWidget(self.RegWidget)
                self.WelcomeContainer.setMaximumSize(QtCore.QSize(16777215, 75))
                self.WelcomeContainer.setStyleSheet("background-color:transparent;")
                self.WelcomeContainer.setObjectName("WelcomeContainer")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.WelcomeContainer)
                self.verticalLayout.setContentsMargins(9, -1, 9, -1)
                self.verticalLayout.setSpacing(9)
                self.verticalLayout.setObjectName("verticalLayout")
                self.WelcomeText = Welcome_Text()
                font = QtGui.QFont()
                font.setFamily("Nirmala UI")
                font.setPointSize(16)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.WelcomeText.setFont(font)
                self.WelcomeText.setStyleSheet("color:white;\n"
                                        "")
                self.verticalLayout.addWidget(
                self.WelcomeText, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_5.addWidget(self.WelcomeContainer)
                self.Validating = QtWidgets.QWidget(self.RegWidget)
                self.Validating.setMaximumSize(QtCore.QSize(0, 0))
                self.Validating.setStyleSheet("border-radius:15px;\n"
                                        "background-color: lightgrey;")
                self.Validating.setObjectName("Validating")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Validating)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                spacerItem1 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_7.addItem(spacerItem1)
                self.LoaderImagetorotate = QtWidgets.QPushButton(self.Validating)
                self.LoaderImagetorotate.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/loader.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.LoaderImagetorotate.setIcon(icon2)
                self.LoaderImagetorotate.setIconSize(QtCore.QSize(50, 50))
                self.LoaderImagetorotate.setObjectName("LoaderImagetorotate")
                self.verticalLayout_7.addWidget(
                self.LoaderImagetorotate, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.label_23 = QtWidgets.QLabel(self.Validating)
                font = QtGui.QFont()
                font.setPointSize(16)
                self.label_23.setFont(font)
                self.label_23.setObjectName("label_23")
                self.verticalLayout_7.addWidget(
                self.label_23, 0, QtCore.Qt.AlignHCenter)
                spacerItem2 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_7.addItem(spacerItem2)
                self.verticalLayout_5.addWidget(self.Validating)
                self.LoginWidget = QtWidgets.QWidget(self.RegWidget)
                self.LoginWidget.setMaximumSize(QtCore.QSize(0, 0))
                self.LoginWidget.setStyleSheet("background-color: black;")
                self.LoginWidget.setObjectName("LoginWidget")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.LoginWidget)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.widget = QtWidgets.QWidget(self.LoginWidget)
                self.widget.setMinimumSize(QtCore.QSize(0, 0))
                self.widget.setMaximumSize(QtCore.QSize(1, 0))
                self.widget.setStyleSheet("background-color:#FF7F7F;\n"
                                        " border-radius:15px;")
                self.widget.setObjectName("widget")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.MessageOnLogin = QtWidgets.QLabel(self.widget)
                self.MessageOnLogin.setMinimumSize(QtCore.QSize(10, 0))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.MessageOnLogin.setFont(font)
                self.MessageOnLogin.setStyleSheet("color:darkred;")
                self.MessageOnLogin.setObjectName("MessageOnLogin")
                self.horizontalLayout_2.addWidget(self.MessageOnLogin)
                self.ButtontoCloseMessageOnLogin = QtWidgets.QPushButton(self.widget)
                self.ButtontoCloseMessageOnLogin.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/x.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ButtontoCloseMessageOnLogin.setIcon(icon3)
                self.ButtontoCloseMessageOnLogin.setObjectName(
                "ButtontoCloseMessageOnLogin")
                self.horizontalLayout_2.addWidget(
                self.ButtontoCloseMessageOnLogin, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_8.addWidget(self.widget)
                self.widget_2 = QtWidgets.QWidget(self.LoginWidget)
                self.widget_2.setStyleSheet("background-color:white;")
                self.widget_2.setObjectName("widget_2")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_2)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.label_24 = QtWidgets.QLabel(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI")
                self.label_24.setFont(font)
                self.label_24.setStyleSheet("")
                self.label_24.setObjectName("label_24")
                self.verticalLayout_9.addWidget(self.label_24)
                self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
                self.lineEdit.setStyleSheet("")
                self.lineEdit.setObjectName("lineEdit")
                self.verticalLayout_9.addWidget(self.lineEdit)
                self.label_25 = QtWidgets.QLabel(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI")
                self.label_25.setFont(font)
                self.label_25.setStyleSheet("")
                self.label_25.setObjectName("label_25")
                self.verticalLayout_9.addWidget(self.label_25)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
                self.lineEdit_2.setStyleSheet("")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.verticalLayout_9.addWidget(self.lineEdit_2)
                self.checkBox_3 = QtWidgets.QCheckBox(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI")
                self.checkBox_3.setFont(font)
                self.checkBox_3.setStyleSheet("")
                self.checkBox_3.setObjectName("checkBox_3")
                self.verticalLayout_9.addWidget(self.checkBox_3)
                self.pushButton = QtWidgets.QPushButton(self.widget_2)
                self.pushButton.setStyleSheet("background-color:pink;\n"
                                        " padding:10px;")
                self.pushButton.setObjectName("pushButton")
                self.verticalLayout_9.addWidget(self.pushButton)
                self.verticalLayout_8.addWidget(self.widget_2)
                spacerItem3 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_8.addItem(spacerItem3)
                self.verticalLayout_5.addWidget(self.LoginWidget)
                self.ContentOnRegisterationPage = QtWidgets.QWidget(self.RegWidget)
                self.ContentOnRegisterationPage.setMaximumSize(
                QtCore.QSize(16777215, 600))
                self.ContentOnRegisterationPage.setStyleSheet(
                "background-color:white;")
                self.ContentOnRegisterationPage.setObjectName(
                "ContentOnRegisterationPage")
                self.gridLayout_6 = QtWidgets.QGridLayout(
                self.ContentOnRegisterationPage)
                self.gridLayout_6.setObjectName("gridLayout_6")
                self.RegisterButtonContainer = QtWidgets.QWidget(
                self.ContentOnRegisterationPage)
                self.RegisterButtonContainer.setMinimumSize(QtCore.QSize(0, 0))
                self.RegisterButtonContainer.setMaximumSize(QtCore.QSize(16777215, 60))
                self.RegisterButtonContainer.setObjectName("RegisterButtonContainer")
                self.gridLayout_11 = QtWidgets.QGridLayout(
                self.RegisterButtonContainer)
                self.gridLayout_11.setObjectName("gridLayout_11")
                self.ButtonToRegister = QtWidgets.QPushButton(
                self.RegisterButtonContainer)
                self.ButtonToRegister.setMinimumSize(QtCore.QSize(150, 0))
                self.ButtonToRegister.setStyleSheet("background-color:pink;\n"
                                                " padding:10px;")
                self.ButtonToRegister.setObjectName("ButtonToRegister")
                self.gridLayout_11.addWidget(self.ButtonToRegister, 0, 1, 1, 1)
                spacerItem4 = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_11.addItem(spacerItem4, 0, 0, 1, 1)
                spacerItem5 = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_11.addItem(spacerItem5, 0, 2, 1, 1)
                self.gridLayout_6.addWidget(self.RegisterButtonContainer, 3, 0, 1, 2)
                self.widget_3 = QtWidgets.QWidget(self.ContentOnRegisterationPage)
                self.widget_3.setObjectName("widget_3")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.label_2 = QtWidgets.QLabel(self.widget_3)
                self.label_2.setMaximumSize(QtCore.QSize(16777215, 10))
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.verticalLayout_3.addWidget(self.label_2)
                self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
                self.pushButton_2.setStyleSheet("background-color:pink;\n"
                                                " padding:10px;")
                self.pushButton_2.setObjectName("pushButton_2")
                self.verticalLayout_3.addWidget(self.pushButton_2)
                self.gridLayout_6.addWidget(self.widget_3, 0, 0, 1, 2)
                spacerItem6 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout_6.addItem(spacerItem6, 4, 0, 1, 1)
                self.MessageHolder = QtWidgets.QWidget(self.ContentOnRegisterationPage)
                self.MessageHolder.setMaximumSize(QtCore.QSize(0, 0))
                self.MessageHolder.setObjectName("MessageHolder")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.MessageHolder)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.label_15 = QtWidgets.QLabel(self.MessageHolder)
                self.label_15.setObjectName("label_15")
                self.verticalLayout_6.addWidget(self.label_15)
                self.gridLayout_6.addWidget(self.MessageHolder, 1, 0, 1, 2)
                self.widget_5 = QtWidgets.QWidget(self.ContentOnRegisterationPage)
                self.widget_5.setObjectName("widget_5")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.NameContainer = QtWidgets.QWidget(self.widget_5)
                self.NameContainer.setMaximumSize(QtCore.QSize(16777215, 100))
                self.NameContainer.setObjectName("NameContainer")
                self.gridLayout_3 = QtWidgets.QGridLayout(self.NameContainer)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.LastNameInput = QtWidgets.QLineEdit(self.NameContainer)
                self.LastNameInput.setMinimumSize(QtCore.QSize(0, 45))
                self.LastNameInput.setObjectName("LastNameInput")
                self.gridLayout_3.addWidget(self.LastNameInput, 2, 2, 1, 1)
                self.label = QtWidgets.QLabel(self.NameContainer)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)
                self.FirstNameInput = QtWidgets.QLineEdit(self.NameContainer)
                self.FirstNameInput.setMinimumSize(QtCore.QSize(0, 45))
                self.FirstNameInput.setObjectName("FirstNameInput")
                self.gridLayout_3.addWidget(self.FirstNameInput, 2, 1, 1, 1)
                self.label_7 = QtWidgets.QLabel(self.NameContainer)
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(8)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color:grey;")
                self.label_7.setObjectName("label_7")
                self.gridLayout_3.addWidget(
                self.label_7, 4, 2, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.label_6 = QtWidgets.QLabel(self.NameContainer)
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(8)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color:grey;")
                self.label_6.setObjectName("label_6")
                self.gridLayout_3.addWidget(self.label_6, 4, 1, 1, 1)
                self.verticalLayout_2.addWidget(self.NameContainer)
                self.widget_4 = QtWidgets.QWidget(self.widget_5)
                self.widget_4.setObjectName("widget_4")
                self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
                self.gridLayout.setObjectName("gridLayout")
                self.ConfirmPasswordInput_2 = QtWidgets.QLineEdit(self.widget_4)
                self.ConfirmPasswordInput_2.setMinimumSize(QtCore.QSize(0, 45))
                self.ConfirmPasswordInput_2.setMaximumSize(
                QtCore.QSize(164654, 16777215))
                self.ConfirmPasswordInput_2.setObjectName("ConfirmPasswordInput_2")
                self.gridLayout.addWidget(self.ConfirmPasswordInput_2, 2, 0, 1, 1)
                self.label_13 = QtWidgets.QLabel(self.widget_4)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_13.setFont(font)
                self.label_13.setObjectName("label_13")
                self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
                self.verticalLayout_2.addWidget(self.widget_4)
                self.PhoneContainer = QtWidgets.QWidget(self.widget_5)
                self.PhoneContainer.setMaximumSize(QtCore.QSize(16777215, 130))
                self.PhoneContainer.setObjectName("PhoneContainer")
                self.gridLayout_8 = QtWidgets.QGridLayout(self.PhoneContainer)
                self.gridLayout_8.setObjectName("gridLayout_8")
                self.CountryCodeInput = QtWidgets.QLineEdit(self.PhoneContainer)
                self.CountryCodeInput.setMinimumSize(QtCore.QSize(0, 45))
                self.CountryCodeInput.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.CountryCodeInput.setObjectName("CountryCodeInput")
                self.gridLayout_8.addWidget(
                self.CountryCodeInput, 1, 1, 1, 1, QtCore.Qt.AlignRight)
                self.ActualNumberInput = QtWidgets.QLineEdit(self.PhoneContainer)
                self.ActualNumberInput.setMinimumSize(QtCore.QSize(0, 45))
                self.ActualNumberInput.setMaximumSize(QtCore.QSize(6546547, 16777215))
                self.ActualNumberInput.setObjectName("ActualNumberInput")
                self.gridLayout_8.addWidget(self.ActualNumberInput, 1, 2, 1, 1)
                self.label_11 = QtWidgets.QLabel(self.PhoneContainer)
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                self.label_11.setFont(font)
                self.label_11.setStyleSheet("color:grey;")
                self.label_11.setObjectName("label_11")
                self.gridLayout_8.addWidget(self.label_11, 3, 2, 1, 1)
                self.label_10 = QtWidgets.QLabel(self.PhoneContainer)
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                self.label_10.setFont(font)
                self.label_10.setStyleSheet("color:grey;")
                self.label_10.setObjectName("label_10")
                self.gridLayout_8.addWidget(
                self.label_10, 3, 1, 1, 1, QtCore.Qt.AlignRight)
                self.label_9 = QtWidgets.QLabel(self.PhoneContainer)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_9.setFont(font)
                self.label_9.setObjectName("label_9")
                self.gridLayout_8.addWidget(self.label_9, 0, 1, 1, 1)
                self.verticalLayout_2.addWidget(self.PhoneContainer)
                self.EmailContainer = QtWidgets.QWidget(self.widget_5)
                self.EmailContainer.setMaximumSize(QtCore.QSize(16777215, 100))
                self.EmailContainer.setObjectName("EmailContainer")
                self.gridLayout_5 = QtWidgets.QGridLayout(self.EmailContainer)
                self.gridLayout_5.setObjectName("gridLayout_5")
                self.label_3 = QtWidgets.QLabel(self.EmailContainer)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
                self.EmailInput = QtWidgets.QLineEdit(self.EmailContainer)
                self.EmailInput.setMinimumSize(QtCore.QSize(0, 45))
                self.EmailInput.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.EmailInput.setObjectName("EmailInput")
                self.gridLayout_5.addWidget(self.EmailInput, 1, 0, 1, 1)
                self.verticalLayout_2.addWidget(self.EmailContainer)
                self.AgreeTermsAndConditionContainer = QtWidgets.QWidget(self.widget_5)
                self.AgreeTermsAndConditionContainer.setMaximumSize(
                QtCore.QSize(16777215, 60))
                self.AgreeTermsAndConditionContainer.setObjectName(
                "AgreeTermsAndConditionContainer")
                self.gridLayout_10 = QtWidgets.QGridLayout(
                self.AgreeTermsAndConditionContainer)
                self.gridLayout_10.setObjectName("gridLayout_10")
                spacerItem7 = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_10.addItem(spacerItem7, 0, 0, 1, 1)
                self.checkBox = QtWidgets.QCheckBox(
                self.AgreeTermsAndConditionContainer)
                self.checkBox.setObjectName("checkBox")
                self.gridLayout_10.addWidget(
                self.checkBox, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
                spacerItem8 = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_10.addItem(spacerItem8, 0, 2, 1, 1)
                self.verticalLayout_2.addWidget(self.AgreeTermsAndConditionContainer)
                self.gridLayout_6.addWidget(self.widget_5, 2, 0, 1, 1)
                self.widget_6 = QtWidgets.QWidget(self.ContentOnRegisterationPage)
                self.widget_6.setObjectName("widget_6")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.NameContainer_2 = QtWidgets.QWidget(self.widget_6)
                self.NameContainer_2.setMaximumSize(QtCore.QSize(16777215, 100))
                self.NameContainer_2.setObjectName("NameContainer_2")
                self.gridLayout_12 = QtWidgets.QGridLayout(self.NameContainer_2)
                self.gridLayout_12.setObjectName("gridLayout_12")
                self.label_5 = QtWidgets.QLabel(self.NameContainer_2)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.gridLayout_12.addWidget(self.label_5, 1, 1, 1, 1)
                self.comboBox = QtWidgets.QComboBox(self.NameContainer_2)
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.gridLayout_12.addWidget(self.comboBox, 2, 1, 1, 1)
                self.verticalLayout_4.addWidget(self.NameContainer_2)
                self.NameContainer_3 = QtWidgets.QWidget(self.widget_6)
                self.NameContainer_3.setMaximumSize(QtCore.QSize(16777215, 100))
                self.NameContainer_3.setObjectName("NameContainer_3")
                self.gridLayout_13 = QtWidgets.QGridLayout(self.NameContainer_3)
                self.gridLayout_13.setObjectName("gridLayout_13")
                self.label_14 = QtWidgets.QLabel(self.NameContainer_3)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_14.setFont(font)
                self.label_14.setObjectName("label_14")
                self.gridLayout_13.addWidget(self.label_14, 1, 1, 1, 1)
                self.comboBox_2 = QtWidgets.QComboBox(self.NameContainer_3)
                self.comboBox_2.setObjectName("comboBox_2")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.gridLayout_13.addWidget(self.comboBox_2, 2, 1, 1, 1)
                self.verticalLayout_4.addWidget(self.NameContainer_3)
                self.GenderContainer = QtWidgets.QWidget(self.widget_6)
                self.GenderContainer.setMaximumSize(QtCore.QSize(16777215, 60))
                self.GenderContainer.setObjectName("GenderContainer")
                self.gridLayout_9 = QtWidgets.QGridLayout(self.GenderContainer)
                self.gridLayout_9.setObjectName("gridLayout_9")
                self.radioButtonforMale = QtWidgets.QRadioButton(self.GenderContainer)
                self.radioButtonforMale.setObjectName("radioButtonforMale")
                self.gridLayout_9.addWidget(
                self.radioButtonforMale, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
                self.radioButtonFemale = QtWidgets.QRadioButton(self.GenderContainer)
                self.radioButtonFemale.setObjectName("radioButtonFemale")
                self.gridLayout_9.addWidget(
                self.radioButtonFemale, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
                self.label_12 = QtWidgets.QLabel(self.GenderContainer)
                self.label_12.setMinimumSize(QtCore.QSize(200, 0))
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_12.setFont(font)
                self.label_12.setObjectName("label_12")
                self.gridLayout_9.addWidget(self.label_12, 1, 0, 1, 1)
                self.verticalLayout_4.addWidget(self.GenderContainer)
                self.PasswordContainer = QtWidgets.QWidget(self.widget_6)
                self.PasswordContainer.setMaximumSize(QtCore.QSize(16777215, 100))
                self.PasswordContainer.setObjectName("PasswordContainer")
                self.gridLayout_4 = QtWidgets.QGridLayout(self.PasswordContainer)
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.PasswordInput = QtWidgets.QLineEdit(self.PasswordContainer)
                self.PasswordInput.setMinimumSize(QtCore.QSize(0, 45))
                self.PasswordInput.setMaximumSize(QtCore.QSize(260, 16777215))
                self.PasswordInput.setObjectName("PasswordInput")
                self.gridLayout_4.addWidget(self.PasswordInput, 1, 0, 2, 1)
                self.label_4 = QtWidgets.QLabel(self.PasswordContainer)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
                self.verticalLayout_4.addWidget(self.PasswordContainer)
                self.ConfirmPasswordContainer = QtWidgets.QWidget(self.widget_6)
                self.ConfirmPasswordContainer.setMaximumSize(
                QtCore.QSize(16777215, 100))
                self.ConfirmPasswordContainer.setSizeIncrement(QtCore.QSize(0, 0))
                self.ConfirmPasswordContainer.setObjectName("ConfirmPasswordContainer")
                self.gridLayout_7 = QtWidgets.QGridLayout(
                self.ConfirmPasswordContainer)
                self.gridLayout_7.setObjectName("gridLayout_7")
                self.label_8 = QtWidgets.QLabel(self.ConfirmPasswordContainer)
                font = QtGui.QFont()
                font.setFamily("Lucida Console")
                font.setPointSize(10)
                self.label_8.setFont(font)
                self.label_8.setObjectName("label_8")
                self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
                self.ConfirmPasswordInput = QtWidgets.QLineEdit(
                self.ConfirmPasswordContainer)
                self.ConfirmPasswordInput.setMinimumSize(QtCore.QSize(0, 45))
                self.ConfirmPasswordInput.setMaximumSize(QtCore.QSize(260, 16777215))
                self.ConfirmPasswordInput.setObjectName("ConfirmPasswordInput")
                self.gridLayout_7.addWidget(self.ConfirmPasswordInput, 1, 0, 1, 1)
                self.verticalLayout_4.addWidget(self.ConfirmPasswordContainer)
                self.gridLayout_6.addWidget(self.widget_6, 2, 1, 1, 1)
                self.verticalLayout_5.addWidget(self.ContentOnRegisterationPage)
                spacerItem9 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_5.addItem(spacerItem9)
                self.gridLayout_2.addWidget(self.RegWidget, 0, 0, 1, 1)
                MainWindow.setCentralWidget(self.RegisteringAndLogin)

                self.ButtonToRegister.clicked.connect(self.Onclickregister)
                self.UpperPanelCloseButton.clicked.connect(self.exitwindow)
                self.UpperPanelMinimizeButton.clicked.connect(self.minimizewindow)
                self.pushButton.clicked.connect(self.OnclickLogin)
                self.ButtontoCloseMessageOnLogin.clicked.connect(self.hidemessage_Login)
                self.pushButton_2.clicked.connect(self.openImage)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.WelcomeText.setText(_translate(
                "MainWindow", "Welcome to Fiesta Content Solution Registeration Form"))
                self.label_23.setText(_translate(
                "MainWindow", "Please wait a minute...."))
                self.MessageOnLogin.setText(_translate(
                "MainWindow", "This is the message"))
                self.label_24.setText(_translate("MainWindow", "Email/Phone No."))
                self.label_25.setText(_translate("MainWindow", "Password:"))
                self.checkBox_3.setText(_translate("MainWindow", "Remember Me"))
                self.pushButton.setText(_translate("MainWindow", "Login"))
                self.ButtonToRegister.setText(_translate("MainWindow", "Register"))
                self.pushButton_2.setText(_translate(
                "MainWindow", "Upload Your Image"))
                self.label_15.setText(_translate("MainWindow", "Text here"))
                self.LastNameInput.setPlaceholderText(_translate("MainWindow", "Doe"))
                self.label.setText(_translate("MainWindow", "Name:"))
                self.FirstNameInput.setPlaceholderText(
                _translate("MainWindow", "John"))
                self.label_7.setText(_translate("MainWindow", "Last Name"))
                self.label_6.setText(_translate("MainWindow", "First Name"))
                self.ConfirmPasswordInput_2.setPlaceholderText(
                _translate("MainWindow", "Type Description"))
                self.label_13.setText(_translate("MainWindow", "Description:"))
                self.label_11.setText(_translate("MainWindow", "Phone Number"))
                self.label_10.setText(_translate("MainWindow", "Area Code"))
                self.label_9.setText(_translate("MainWindow", "Phone:"))
                self.label_3.setText(_translate("MainWindow", "Email:"))
                self.EmailInput.setPlaceholderText(
                _translate("MainWindow", "name@domain.com"))
                self.checkBox.setText(_translate(
                "MainWindow", "I agree to the Terms and Conditions"))
                self.label_5.setText(_translate("MainWindow", "Catogary:"))
                self.comboBox.setItemText(0, _translate("MainWindow", "Home Based"))
                self.comboBox.setItemText(1, _translate("MainWindow", "Office Based"))
                self.comboBox.setItemText(2, _translate(
                "MainWindow", "Assignment Based"))
                self.label_14.setText(_translate("MainWindow", "Team Leader:"))
                self.comboBox_2.setItemText(
                0, _translate("MainWindow", "Abdullah Tariq"))
                self.comboBox_2.setItemText(1, _translate("MainWindow", "Mowaddat"))
                self.comboBox_2.setItemText(2, _translate("MainWindow", "Areeba"))
                self.comboBox_2.setItemText(
                3, _translate("MainWindow", "Huma Javeria"))
                self.comboBox_2.setItemText(
                4, _translate("MainWindow", "Rameen Zahra"))
                self.comboBox_2.setItemText(5, _translate("MainWindow", "Iqra Nadeem"))
                self.comboBox_2.setItemText(
                6, _translate("MainWindow", "Fateen Shahid"))
                self.comboBox_2.setItemText(7, _translate(
                "MainWindow", "Amar Raza Shah Durani"))
                self.radioButtonforMale.setText(_translate("MainWindow", "Male"))
                self.radioButtonFemale.setText(_translate("MainWindow", "Female"))
                self.label_12.setText(_translate("MainWindow", "Gender:"))
                self.PasswordInput.setPlaceholderText(
                _translate("MainWindow", "Passwrod"))
                self.label_4.setText(_translate("MainWindow", "Password:"))
                self.label_8.setText(_translate("MainWindow", "Confirm Password:"))
                self.ConfirmPasswordInput.setPlaceholderText(
                _translate("MainWindow", "Re-type Password"))
        def Onclickregister(self):
                self.Register_to_DB()
                # Closing Content for Registeration by width
                self.step1 = QPropertyAnimation(
                self.ContentOnRegisterationPage, b'maximumWidth')
                self.step1.setDuration(1000)
                self.step1.setStartValue(self.ContentOnRegisterationPage.width())
                self.step1.setEndValue(0)
                self.step1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                # Closing Content for Registeration by height
                self.step2 = QPropertyAnimation(
                self.ContentOnRegisterationPage, b'maximumHeight')
                self.step2.setDuration(1000)
                self.step2.setStartValue(self.ContentOnRegisterationPage.height())
                self.step2.setEndValue(0)
                self.step2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                # Resizing Main Window
                self.step3 = QPropertyAnimation(self.MainWindow, b'maximumHeight')
                self.step3.setDuration(1000)
                self.step3.setStartValue(self.MainWindow.height())
                self.step3.setEndValue(500)
                self.step3.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                # Geometry Setting
                from win32api import GetSystemMetrics
                self.step3 = QPropertyAnimation(self.MainWindow, b'geometry')
                self.step3.setDuration(1000)
                self.step3.setStartValue(
                QRect(self.MainWindow.x(), self.MainWindow.y(), self.MainWindow.width(), self.MainWindow.height()))
                self.step3.setEndValue(QRect(int(GetSystemMetrics(0)/5-100),int(GetSystemMetrics(1)/9),int(GetSystemMetrics(0)/1.5),int(GetSystemMetrics(1)/1.5)))
                self.step3.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step4 = QPropertyAnimation(self.Validating, b'maximumWidth')
                self.step4.setDuration(1000)
                self.step4.setStartValue(800)
                self.step4.setEndValue(900)
                self.step4.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step5 = QPropertyAnimation(self.Validating, b'maximumWidth')
                self.step5.setDuration(1000)
                self.step5.setStartValue(0)
                self.step5.setEndValue(900)
                self.step5.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step6 = QPropertyAnimation(self.Validating, b'maximumHeight')
                self.step6.setDuration(1000)
                self.step6.setStartValue(0)
                self.step6.setEndValue(900)
                self.step6.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step7 = QPropertyAnimation(self.Validating, b'maximumWidth')
                self.step7.setDuration(1000)
                self.step7.setStartValue(900)
                self.step7.setEndValue(0)
                self.step7.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step8 = QPropertyAnimation(self.Validating, b'maximumHeight')
                self.step8.setDuration(1000)
                self.step8.setStartValue(300)
                self.step8.setEndValue(0)
                self.step8.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step9 = QPropertyAnimation(self.MainWindow, b'maximumHeight')
                self.step9.setDuration(1000)
                self.step9.setStartValue(self.MainWindow.height())
                self.step9.setEndValue(300)
                self.step9.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step10 = QPropertyAnimation(self.LoginWidget, b'maximumHeight')
                self.step10.setDuration(1000)
                self.step10.setStartValue(self.LoginWidget.height())
                self.step10.setEndValue(500)
                self.step10.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.step11 = QPropertyAnimation(self.LoginWidget, b'maximumWidth')
                self.step11.setDuration(1000)
                self.step11.setStartValue(self.LoginWidget.width())
                self.step11.setEndValue(900)
                self.step11.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.SequenceAnime = QSequentialAnimationGroup()
                self.SequenceAnime.addAnimation(self.step1)
                self.SequenceAnime.addAnimation(self.step2)
                self.SequenceAnime.addAnimation(self.step3)
                self.SequenceAnime.addAnimation(self.step4)
                self.SequenceAnime.addAnimation(self.step5)
                self.SequenceAnime.addAnimation(self.step6)
                self.SequenceAnime.addAnimation(self.step7)
                self.SequenceAnime.addAnimation(self.step8)
                self.SequenceAnime.addAnimation(self.step9)
                self.SequenceAnime.addAnimation(self.step10)
                self.SequenceAnime.addAnimation(self.step11)
                self.SequenceAnime.start()
                self.WelcomeText.startTimer()
        def exitwindow(self):
                sys.exit()
        def minimizewindow(self):
                import win32gui
                import win32con
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)        
        def Register_to_DB(self):
                if (self.radioButtonforMale.isChecked()):
                        gender = "Male"
                elif (self.radioButtonFemale.isChecked()):
                        gender = "Female"
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("INSERT INTO writer (writer_FName, writer_LName, writer_CompanyName, writer_Email, writer_password, writer_Phone, writer_Description, writer_Gender, writer_Image, writer_Leader, writer_category, writer_JobRole) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (
                str(self.FirstNameInput.text()),
                str(self.LastNameInput.text()),
                "Fiesta Content Solutions",
                str(self.EmailInput.text()),
                str(self.PasswordInput.text()),
                str(self.CountryCodeInput.text()+self.ActualNumberInput.text()),
                str(self.ConfirmPasswordInput_2.text()),
                str(gender),
                self.BinaryData,
                str(self.comboBox_2.currentText()),
                str(self.comboBox.currentText()),
                "Content Writer"
                ))
                con.commit()
                con.close()
        def showmessage_Login(self):
                self.animatemessageview_width = QPropertyAnimation(self.widget, b'maximumWidth')
                self.animatemessageview_width.setDuration(1000)
                self.animatemessageview_width.setStartValue(0)
                self.animatemessageview_width.setEndValue(1000)
                self.animatemessageview_width.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.animatemessageview__height = QPropertyAnimation(self.widget, b'maximumHeight')
                self.animatemessageview__height.setDuration(1000)
                self.animatemessageview__height.setStartValue(0)
                self.animatemessageview__height.setEndValue(100)
                self.animatemessageview__height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.Sequenceformessage = QSequentialAnimationGroup()
                self.Sequenceformessage.addAnimation(self.animatemessageview_width)
                self.Sequenceformessage.addAnimation(self.animatemessageview__height)
                self.Sequenceformessage.start()
        def hidemessage_Login(self):
                self.hidemessageanime_width = QPropertyAnimation(self.widget, b'maximumWidth')
                self.hidemessageanime_width.setDuration(1000)
                self.hidemessageanime_width.setStartValue(1000)
                self.hidemessageanime_width.setEndValue(0)
                self.hidemessageanime_width.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.hidemessageanime_height = QPropertyAnimation(self.widget, b'maximumHeight')
                self.hidemessageanime_height.setDuration(1000)
                self.hidemessageanime_height.setStartValue(100)
                self.hidemessageanime_height.setEndValue(0)
                self.hidemessageanime_height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.sequencetohidemessage  = QSequentialAnimationGroup()
                self.sequencetohidemessage.addAnimation(self.hidemessageanime_width)
                self.sequencetohidemessage.addAnimation(self.hidemessageanime_height)
                self.sequencetohidemessage.start()
        def CloseLogin(self):
                self.CloseLogin1 = QPropertyAnimation(self.widget_2, b'maximumHeight')
                self.CloseLogin1.setDuration(1000)
                self.CloseLogin1.setStartValue(self.widget_2.width())
                self.CloseLogin1.setEndValue(0)
                self.CloseLogin1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                
                self.CloseLogin2 = QPropertyAnimation(self.WelcomeContainer, b'maximumHeight')
                self.CloseLogin2.setDuration(1000)
                self.CloseLogin2.setStartValue(self.WelcomeContainer.width())
                self.CloseLogin2.setEndValue(0)
                self.CloseLogin2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                
                self.CloseLogin3 = QPropertyAnimation(self.MainWindow, b'maximumHeight')
                self.CloseLogin3.setDuration(1000)
                self.CloseLogin3.setStartValue(self.MainWindow.width())
                self.CloseLogin3.setEndValue(0)
                self.CloseLogin3.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.SequenceforCloseLogin = QSequentialAnimationGroup()
                self.SequenceforCloseLogin.addAnimation(self.CloseLogin1)
                self.SequenceforCloseLogin.addAnimation(self.CloseLogin2)
                self.SequenceforCloseLogin.addAnimation(self.CloseLogin3)
                self.SequenceforCloseLogin.start()
                self.SequenceforCloseLogin.finished.connect(self.MWClose)
        def MWClose(self):
                self.MainWindow.close()
        def OnclickLogin(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_Email = %s and writer_password = %s",(self.lineEdit.text(),self.lineEdit_2.text()))
                record = cur.fetchone()
                if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                        self.MessageOnLogin.setText("Fields are empty. Please give some input to work on.")
                        self.MessageOnLogin.setStyleSheet("color: darkred;")
                        self.widget.setStyleSheet("background-color:#FF7F7F;")
                        self.showmessage_Login()
                elif record != None:
                        if record[12] != "Team Leader": 
                                self.MessageOnLogin.setText("Login Succesful")
                                self.MessageOnLogin.setStyleSheet("color: darkgreen;")
                                self.widget.setStyleSheet("background-color: lightgreen;")
                                self.showmessage_Login()
                                self.CloseLogin()
                                self.window = QtWidgets.QMainWindow()
                                GetData = DB_Data(str(self.lineEdit.text()), str(self.lineEdit_2.text()))
                                self.ui = WriterUI(str(GetData.writer_id), False,str(GetData.writer_evaluation_points),str(GetData.writer_fullname),str(GetData.writer_daily_word_count),str(GetData.writer_monthly_word_count),r"./Images/writer_image.png",str(GetData.writer_email),str(GetData.writer_phone),str(GetData.writer_gender),"20",str(GetData.writer_description), str(GetData.writer_jobe_role), str(GetData.writer_team_name),str(GetData.writer_team_leader))
                        else:
                                self.MessageOnLogin.setText("Login Succesful")
                                self.MessageOnLogin.setStyleSheet("color: darkgreen;")
                                self.widget.setStyleSheet("background-color: lightgreen;")
                                self.showmessage_Login()
                                self.CloseLogin()
                                self.window = QtWidgets.QMainWindow()
                                GetData = DB_Data(str(self.lineEdit.text()), str(self.lineEdit_2.text()))
                                self.ui = TDL_UI(False, GetData.writer_team_name,GetData.writer_new_members , GetData.writer_total_assignments, GetData.writer_evaluation_points, GetData.writer_fullname,f"F:\\Visual Code Stuff\\Design_For_FCS_Portal\\Images\\writer_image.png",GetData.writer_email,GetData.writer_phone,GetData.writer_gender,'24',GetData.writer_description,GetData.writer_jobe_role, GetData.writer_team_name)
                else:
                        self.MessageOnLogin.setText("Invalid Credential")
                        self.MessageOnLogin.setStyleSheet("color: darkred;")
                        self.widget.setStyleSheet("background-color:#FF7F7F;")
                        self.showmessage_Login()
                con.commit()
                con.close()
        def openImage(self):
                self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()
                pixmap = QtGui.QPixmap(self.imagePath)
                self.label_2.setPixmap(QtGui.QPixmap.scaled(QtGui.QPixmap(pixmap),300,300,aspectRatioMode= Qt.KeepAspectRatio))
                self.label_2.resize(pixmap.size())
                if self.imagePath == '':
                        pass
                else:
                        with open(self.imagePath, "rb") as File:
                                self.BinaryData = File.read()
if __name__ == "__main__":
    ui = RegisterationUI()