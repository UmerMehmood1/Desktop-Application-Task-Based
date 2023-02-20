import Resources
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as sql
from WriterMain import WriterUI
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup,Qt, QRect
from TDLMain import TDL_UI
from Data_Extractor import DB_Data
import sys
class LoginUI(object):
        def __init__(self):
                app = QtWidgets.QApplication(sys.argv)
                self.MainWindow = QtWidgets.QMainWindow()
                self.setupUi(self.MainWindow)
                self.MainWindow.show()
                sys.exit(app.exec_())
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 372)
                MainWindow.setAttribute(Qt.WA_TranslucentBackground)
                MainWindow.setWindowFlag(Qt.FramelessWindowHint)
                MainWindow.setMaximumSize(QtCore.QSize(800, 372))
                MainWindow.setStyleSheet("")
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
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.RegisteringAndLogin)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.RegWidget = QtWidgets.QWidget(self.RegisteringAndLogin)
                self.RegWidget.setMaximumSize(QtCore.QSize(16777215, 1000))
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
                self.verticalLayout_5.addWidget(self.UpperPanel, 0, QtCore.Qt.AlignTop)
                self.WelcomeContainer = QtWidgets.QWidget(self.RegWidget)
                self.WelcomeContainer.setMaximumSize(QtCore.QSize(16777215, 75))
                self.WelcomeContainer.setStyleSheet("background-color:transparent;")
                self.WelcomeContainer.setObjectName("WelcomeContainer")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.WelcomeContainer)
                self.verticalLayout.setContentsMargins(9, -1, 9, -1)
                self.verticalLayout.setSpacing(9)
                self.verticalLayout.setObjectName("verticalLayout")
                self.WelcomeText = QtWidgets.QLabel(self.WelcomeContainer)
                self.WelcomeText.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setFamily("Nirmala UI")
                font.setPointSize(16)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.WelcomeText.setFont(font)
                self.WelcomeText.setStyleSheet("color:white;\n"
                                        "")
                self.WelcomeText.setObjectName("WelcomeText")
                self.verticalLayout.addWidget(
                self.WelcomeText, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_5.addWidget(
                self.WelcomeContainer, 0, QtCore.Qt.AlignTop)
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
                self.LoginWidget.setMaximumSize(QtCore.QSize(16777215, 860))
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
                self.verticalLayout_6.addWidget(self.RegWidget)
                MainWindow.setCentralWidget(self.RegisteringAndLogin)

                self.UpperPanelCloseButton.clicked.connect(self.exitwindow)
                self.UpperPanelMinimizeButton.clicked.connect(self.minimizewindow)
                self.pushButton.clicked.connect(self.OnclickLogin)
                self.ButtontoCloseMessageOnLogin.clicked.connect(self.hidemessage)

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
        def OnclickLogin(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_Email = %s and writer_password = %s",(
                self.lineEdit.text(),
                self.lineEdit_2.text()
                ))
                record = cur.fetchone()
                if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                        self.MessageOnLogin.setText("Fields are empty. Please give some input to work on.")
                        self.MessageOnLogin.setStyleSheet("color: darkred;")
                        self.widget.setStyleSheet("background-color:#FF7F7F;")
                        self.showmessage()
                elif record != None:
                        if record[12] != "Team Leader": 

                                self.MessageOnLogin.setText("Login Succesful")
                                self.MessageOnLogin.setStyleSheet("color: darkgreen;")
                                self.widget.setStyleSheet("background-color: lightgreen;")
                                self.showmessage()
                                self.CloseLogin()
                                self.window = QtWidgets.QMainWindow()
                                print(self.lineEdit.text())
                                print(self.lineEdit_2.text())
                                GetData = DB_Data(str(self.lineEdit.text()), str(self.lineEdit_2.text()))
                                self.ui = WriterUI(str(GetData.writer_id), False,str(GetData.writer_evaluation_points),str(GetData.writer_fullname),str(GetData.writer_daily_word_count),str(GetData.writer_monthly_word_count),r"./Images/writer_image.png",str(GetData.writer_email),str(GetData.writer_phone),str(GetData.writer_gender),"20",str(GetData.writer_description), str(GetData.writer_jobe_role), str(GetData.writer_team_name),str(GetData.writer_team_leader))
                        else:
                                self.MessageOnLogin.setText("Login Succesful")
                                self.MessageOnLogin.setStyleSheet("color: darkgreen;")
                                self.widget.setStyleSheet("background-color: lightgreen;")
                                self.showmessage()
                                self.CloseLogin()
                                self.window = QtWidgets.QMainWindow()
                                GetData = DB_Data(str(self.lineEdit.text()), str(self.lineEdit_2.text()))
                                self.ui = TDL_UI(False, GetData.writer_team_name,GetData.writer_new_members , GetData.writer_total_assignments, GetData.writer_evaluation_points, GetData.writer_fullname,f".\\Images\\writer_image.png",GetData.writer_email,GetData.writer_phone,GetData.writer_gender,'24',GetData.writer_description,GetData.writer_jobe_role, GetData.writer_team_name)

                else:
                        self.MessageOnLogin.setText("Invalid Credential")
                        self.MessageOnLogin.setStyleSheet("color: darkred;")
                        self.widget.setStyleSheet("background-color:#FF7F7F;")
                        self.showmessage()
                con.commit()
                con.close()
        def showmessage(self):
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
        def hidemessage(self):
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
        def exitwindow(self):
                sys.exit()
        def minimizewindow(self):
                        import win32gui
                        import win32con
                        Minimize = win32gui.GetForegroundWindow()
                        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)        
        def MWClose(self):
                self.MainWindow.close()
if __name__ == "__main__":
        ui = LoginUI()