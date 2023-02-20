import Resources
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QSequentialAnimationGroup
import pymysql as sql
import qdarkstyle
from Data_Extractor import DB_Data
import sys

class TDL_UI(object):
        def __init__(self,maximized, Team_Name, New_Members, Total_Assignments, Evaluation_points, Writer_Name, Writer_Image, Writer_Email, Writer_Contact_No, Writer_Gender, Writer_Age, Writer_Biography, Writer_Role, Writer_Team_leader):
                self.MainWindow = QtWidgets.QMainWindow()
                self.dark_mode = False
                from win32api import GetSystemMetrics
                self.MainWindow.resize(int(GetSystemMetrics(0)/1.5),int(GetSystemMetrics(1)/1.5))
                self.MainWindow.setAttribute(Qt.WA_TranslucentBackground)
                self.MainWindow.setWindowFlag(Qt.FramelessWindowHint)
                self.maximized = maximized
                self.New_Members = New_Members
                self.Total_Assignments = Total_Assignments
                self.Team_Name = Team_Name
                self.Evaluation_points = Evaluation_points
                self.Writer_Name = Writer_Name
                self.Writer_Image = Writer_Image
                self.Writer_Email = Writer_Email
                self.Writer_Contact_No = Writer_Contact_No
                self.Writer_Gender = Writer_Gender
                self.Writer_Age = Writer_Age
                self.Writer_Biography = Writer_Biography
                self.Writer_Role = Writer_Role
                self.Writer_Team_leader = Writer_Team_leader
                self.setupUi()
                self.MainWindow.show()
                self.add_Team_Leader_in_Evaluation_Form(Writer_Team_leader)
                self.function_to_be_called_to_add_data()
        def show_Dashboard(self):
                self.RightForm.setCurrentWidget(self.DashboardAdmin)
        def show_RecievedTask(self):
                self.RightForm.setCurrentWidget(self.RecievedTaskPage)
        def show_MangeTeamLeaves(self):
                self.RightForm.setCurrentWidget(self.ManageTeamLeavesPage)
        def show_TeamReport(self):
                self.RightForm.setCurrentWidget(self.WriterProgressPage)
        def show_PermanencyReport(self):
                self.RightForm.setCurrentWidget(self.PermanencyReport)                
        def show_TaskAvailable(self):
                self.RightForm.setCurrentWidget(self.TaskAvailable)                
        def show_TaskAssinged(self):
                self.RightForm.setCurrentWidget(self.TaskAssignedReport)                
        def show_AssignTask(self):
                self.RightForm.setCurrentWidget(self.AsiggningTask)                
        def show_TDLProductivity(self):
                self.RightForm.setCurrentWidget(self.TDLProductivity)                
        def show_EvaluationForm(self):
                self.RightForm.setCurrentWidget(self.EvaluationPage)                
        def show_UpdateWork(self):
                self.RightForm.setCurrentWidget(self.UpdateWork)
        def show_ManageLeaves(self):
                self.RightForm.setCurrentWidget(self.ManageLeaves)
        def show_UserProfile(self):
                self.RightForm.setCurrentWidget(self.UserProfile)
        def show_ContactUs(self):
                self.RightForm.setCurrentWidget(self.ContactUs)
        def show_FAQs(self):
                self.RightForm.setCurrentWidget(self.FAQs)
        def show_Update_Designation(self):
                self.RightForm.setCurrentWidget(self.page)
        def open_leftmenu(self):
                width = self.LeftMenu.width()
                height = self.LeftMenu.height()

                if width == 0 and height == 0:
                        newWidth = 550
                        newHeight = 1000
                else:
                        newWidth = 0
                        newHeight = 0

                self.leftmenuanimatewidth = QPropertyAnimation(self.LeftMenu, b'maximumWidth')
                self.leftmenuanimatewidth.setDuration(500)
                self.leftmenuanimatewidth.setStartValue(width)
                self.leftmenuanimatewidth.setEndValue(newWidth)
                self.leftmenuanimatewidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.leftmenuanimatewidth.start()

                self.leftmenuanimateheight = QPropertyAnimation(self.LeftMenu, b'maximumHeight')
                self.leftmenuanimateheight.setDuration(1000)
                self.leftmenuanimateheight.setStartValue(height)
                self.leftmenuanimateheight.setEndValue(newHeight)
                self.leftmenuanimateheight.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.leftmenuanimateheight.start()
        def OpenAndHideUserMenu(self,object_here):
                self.object_here = object_here 
                width = object_here.width()
                height = object_here.height()
                if width == 0 and height == 0:
                        newWidth = 550
                        newHeight = 1000
                else:
                        newWidth = 0
                        newHeight = 0

                self.usermenuanimatewidht = QPropertyAnimation(object_here, b'maximumWidth')
                self.usermenuanimatewidht.setDuration(500)
                self.usermenuanimatewidht.setStartValue(width)
                self.usermenuanimatewidht.setEndValue(newWidth)
                self.usermenuanimatewidht.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.usermenuanimatewidht.start()

                self.usermenuanimateheight = QPropertyAnimation(object_here, b'maximumHeight')
                self.usermenuanimateheight.setDuration(700)
                self.usermenuanimateheight.setStartValue(height)
                self.usermenuanimateheight.setEndValue(newHeight)
                self.usermenuanimateheight.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.usermenuanimateheight.start()
        def showUserMenuOnEvaluation(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnDashboard_4)
        def showUserMenuOnTDL(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnTDLProductivity)
        def showUserMenuOnManageLeaves(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnDashboard_3)
        def showUserMenuOnAssingingTask(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnAsiggningTask)
        def showUserMenuOnAssingedTask(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnTaskAssignedReport)
        def showUserMenuOnPermanency(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnPermanencyReport)
        def showUserMenuOnTeamReport(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnDashboard_2)
        def showUserMenuOnDashboard(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnDashboard)
        def showUserMenuOnTaskAvailable(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnTaskAvailable)
        def showUserMenuOnUpdateWork(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnUpdateWork)
        def showUserMenuOnProfile(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnUserProfile)
        def showUserMenuOnContactUs(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnContactUs)
        def showUserMenuOnFAQs(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnFAQs)
        def showUserMenuOnRecievedTask(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnAsiggningTask_2)
        def showUserMenuOnUpdateDesignation(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnUpdateWork_3)
        def showUserMenuOnManageTeamLeaves(self): 
                self.OpenAndHideUserMenu(self.UserMenuOnTDLProductivity_2)
        def closewindow(self):
                import sys
                sys.exit()
        def minimzewindow(self):
                import win32gui
                import win32con
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        def maximizewindow(self):
                from win32api import GetSystemMetrics
                if not self.maximized:
                        self.maximized = True
                        self.animemaximize = QPropertyAnimation(self.MainWindow, b'geometry')
                        self.animemaximize.setDuration(1000)
                        self.animemaximize.setStartValue(QRect(self.MainWindow.x(),self.MainWindow.y(),self.MainWindow.width(),self.MainWindow.height()))
                        self.animemaximize.setEndValue(QRect(0,0,GetSystemMetrics(0),GetSystemMetrics(1)))
                        self.animemaximize.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animemaximize.start()
                elif self.maximized:
                        self.maximized = False
                        self.animeshrink = QPropertyAnimation(self.MainWindow, b'geometry')
                        self.animeshrink.setDuration(1000)
                        self.animeshrink.setStartValue(QRect(self.MainWindow.x(),self.MainWindow.y(),self.MainWindow.width(),self.MainWindow.height()))
                        self.animeshrink.setEndValue(QRect(int(GetSystemMetrics(0)/5),int(GetSystemMetrics(1)/7),int(GetSystemMetrics(0)/1.5),int(GetSystemMetrics(1)/1.5)))
                        self.animeshrink.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animeshrink.start()
        def open_notification_Board(self):
                width = self.widget_9.width()
                height = self.widget_9.height()

                if width == 0 and height == 0:
                        newWidth = 550
                        newHeight = 1000
                else:
                        newWidth = 0
                        newHeight = 0

                self.leftmenuanimatewidth = QPropertyAnimation(self.widget_9, b'maximumWidth')
                self.leftmenuanimatewidth.setDuration(500)
                self.leftmenuanimatewidth.setStartValue(width)
                self.leftmenuanimatewidth.setEndValue(newWidth)
                self.leftmenuanimatewidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.leftmenuanimatewidth.start()

                self.leftmenuanimateheight = QPropertyAnimation(self.widget_9, b'maximumHeight')
                self.leftmenuanimateheight.setDuration(1000)
                self.leftmenuanimateheight.setStartValue(height)
                self.leftmenuanimateheight.setEndValue(newHeight)
                self.leftmenuanimateheight.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.leftmenuanimateheight.start()
        def dark_mode_on(self):
                if not self.dark_mode:
                        self.RightForm.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.ContentOnEvaluatePage.setStyleSheet(
                                "QLineEdit{border:2px solid white; border-radius: 5px;}")
                        self.UpperPartOnPermanencyReport.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnTaskAvailable.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnTaskAssignedReport.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnAsiggningTask.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnUpdateWork.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnUserProfile.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnTDLProductivity.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnTDLProductivity_2.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnContactUs.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnFAQs.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnUpdateWork_3.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UpperPartOnTDLProductivity_3.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        self.UserIconOnAsiggningTask.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/moon.svg"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.pushButton_13.setIcon(icon)
                        self.pushButton_14.setIcon(icon)
                        self.pushButton_15.setIcon(icon)
                        self.pushButton_16.setIcon(icon)
                        self.pushButton_19.setIcon(icon)
                        self.pushButton_20.setIcon(icon)
                        self.pushButton_21.setIcon(icon)
                        self.pushButton_22.setIcon(icon)
                        self.pushButton_24.setIcon(icon)
                        self.pushButton_25.setIcon(icon)
                        self.pushButton_26.setIcon(icon)
                        self.pushButton_27.setIcon(icon)
                        self.pushButton_28.setIcon(icon)
                        self.pushButton_29.setIcon(icon)
                        self.pushButton_31.setIcon(icon)
                        self.pushButton_169.setIcon(icon)
                        self.pushButton_28.setStyleSheet("#pushButton_20 {padding: 0px;} \n #pushButton_20:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_13.setStyleSheet("#pushButton_13 {padding: 0px;} \n #pushButton_13:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_14.setStyleSheet("#pushButton_14 {padding: 0px;} \n #pushButton_14:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_15.setStyleSheet("#pushButton_15 {padding: 0px;} \n #pushButton_15:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_16.setStyleSheet("#pushButton_16 {padding: 0px;} \n #pushButton_16:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_19.setStyleSheet("#pushButton_19 {padding: 0px;} \n #pushButton_19:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_20.setStyleSheet("#pushButton_20 {padding: 0px;} \n #pushButton_20:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_21.setStyleSheet("#pushButton_21 {padding: 0px;} \n #pushButton_21:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_22.setStyleSheet("#pushButton_22 {padding: 0px;} \n #pushButton_22:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_24.setStyleSheet("#pushButton_24 {padding: 0px;} \n #pushButton_24:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_25.setStyleSheet("#pushButton_25 {padding: 0px;} \n #pushButton_25:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_26.setStyleSheet("#pushButton_26 {padding: 0px;} \n #pushButton_26:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_27.setStyleSheet("#pushButton_27 {padding: 0px;} \n #pushButton_27:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_28.setStyleSheet("#pushButton_28 {padding: 0px;} \n #pushButton_28:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_29.setStyleSheet("#pushButton_29 {padding: 0px;} \n #pushButton_29:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_31.setStyleSheet("#pushButton_31 {padding: 0px;} \n #pushButton_31:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_169.setStyleSheet("#pushButton_169 {padding: 0px;} \n #pushButton_169:hover{border-radius:5px; background-color: #2596be;}")
                        self.label_40.setStyleSheet("color:black;")
                        self.label_42.setStyleSheet("color:black;")
                        self.label_10.setStyleSheet("color:black;")
                        self.label_44.setStyleSheet("color:black;")
                        self.label_9.setStyleSheet("color:black;")
                        self.label_43.setStyleSheet("color:black;")
                        self.widget_32.setStyleSheet("color:black;")
                        self.ContentOnFAQs.setStyleSheet("color:black; background-color: grey;")
                        self.widget_31.setStyleSheet("color:black;")
                        self.tableWidget_2.setStyleSheet("color:white;")
                        self.pushButton_23.setStyleSheet("#pushButton_23{\n"
                                                "padding: 10px;\n"
                                                "color:black;"
                                                "background-color: pink;}\n"
                                                "#pushButton_23:hover{\n"
                                                "padding: 5px;\n"
                                                "background-color: lightblue;}")
                        self.pushButton_32.setStyleSheet("#pushButton_32{\n"
                                                "color:black;"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                " }\n"
                                                "#pushButton_32:hover {background-color: lightgreen; \\n padding: 10px; }")
                        self.pushButton_17.setStyleSheet("color:black;"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                        self.pushButton_18.setStyleSheet("color:black;"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                        self.pushButton_34.setStyleSheet("#pushButton_34{\n"
                                                "background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color:black;\n"
                                                "}\n"
                                                "#pushButton_34:hover{\n"
                                                "background-color: lightgreen;\n"
                                                "padding: 10px;\n"
                                                "}\n")
                        self.pushButton_9.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: black;\n")
                        self.pushButton_8.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n")
                        self.pushButton_170.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n")
                        self.pushButton_10.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n")
                        self.widget_4.setStyleSheet("color:black;")
                        self.pushButton_11.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n")
                        self.pushButton_30.setStyleSheet("#pushButton_30{\n"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                "color:black;"
                                                " }\n"
                                                "#pushButton_30:hover {background-color: lightblue; \\n padding: 10px; }")
                        self.pushButton_12.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: black;\n")
                        self.MessageOnEvaluation.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.label_82.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnAssigningTask.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnManageLeaves.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnProfile.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnUpdateDesignation.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnUpdateWork.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnTDL.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnAssigningTask.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.MessageOnRecievedTask.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.label_82.setStyleSheet("color:black; background-color:lightgreen; border-radius:15px; padding: 10px;")
                        self.dark_mode = True
                else:
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/sun.svg"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.pushButton_13.setIcon(icon)
                        self.pushButton_14.setIcon(icon)
                        self.pushButton_15.setIcon(icon)
                        self.pushButton_16.setIcon(icon)
                        self.pushButton_19.setIcon(icon)
                        self.pushButton_20.setIcon(icon)
                        self.pushButton_21.setIcon(icon)
                        self.pushButton_22.setIcon(icon)
                        self.pushButton_24.setIcon(icon)
                        self.pushButton_25.setIcon(icon)
                        self.pushButton_26.setIcon(icon)
                        self.pushButton_27.setIcon(icon)
                        self.pushButton_28.setIcon(icon)
                        self.pushButton_29.setIcon(icon)
                        self.pushButton_31.setIcon(icon)
                        self.pushButton_169.setIcon(icon)
                        self.RightForm.setStyleSheet("background-color:white;\n"
                                        "border-radius:15px;")
                        self.DashboardAdmin.setStyleSheet("#MenuButtonOnDashboard:hover{\n"
                                                "background-color: #2596be;\n"
                                                "}") 
                        self.RightShit.setStyleSheet("#HeaderFrame\n"
                                        "{\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "#Table\n"
                                        "{\n"
                                        "background-color: #2596be;\n"
                                        "}\n"
                                        "\n"
                                        "#BlockforSearch {\n"
                                        "border-radius: 5px;\n"
                                        "border: 2px solid #2596be;\n"
                                        "}\n"
                                        "")
                        self.PageNameOnDashboard.setStyleSheet("color : #2596be;\n"
                                                "font: bold;\n"
                                                "")
                        self.FeildForSearch.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                        self.pushButton_13.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconDashboard.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconDashboard.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                        self.UserMenuOnDashboard.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                        self.pushButton_51.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.CardHolder.setStyleSheet("#Card1{\n"
                                        "}")
                        self.ContentOnWriterDashboard.setStyleSheet(
                                                "background-color: lightblue;")
                        self.label_41.setStyleSheet("color:lightgreen;")
                        self.pushButton_12.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                        self.tableWidget_2.setStyleSheet("background-color:lightblue;")
                        self.PageNameOnDashboard_2.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearch_2.setStyleSheet("#BlockforSearch_2{\n"
                                                "border: 2px solid lightblue;\n"
                                                "border-radius: 5px;\n"
                                                "}")
                        self.FeildForSearch_2.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                        self.pushButton_14.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconDashboard_2.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconDashboard_2.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                        self.UserMenuOnDashboard_2.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_137.setStyleSheet("color: #2596be;")
                        self.pushButton_57.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.UpperPartOnPermanencyReport.setStyleSheet(
                                                "background-color: white;")      
                        self.MenuButtonOnPermanencyReport.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")      
                        self.LabelforMenuOnPermanencyReport.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                        self.BlockforSearchOnPermanencyReport.setStyleSheet("#BlockforSearchOnPermanencyReport{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                        self.FeildForSearchOnPermanencyReport.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;") 
                        self.pushButton_15.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnPermanencyReport.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserIconOnPermanencyReport.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserMenuOnPermanencyReport.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_138.setStyleSheet("color: #2596be;")
                        self.pushButton_60.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.UpperPartOnTaskAvailable.setStyleSheet("background-color: white;")
                        self.MenuButtonOnTaskAvailable.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}\n"
                                                        "")
                        self.LabelforMenuOnTaskAvailable.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearchOnTaskAvailable.setStyleSheet("#BlockforSearchOnTaskAvailable{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                        self.FeildForSearchOnTaskAvailable.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                        self.pushButton_16.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnTaskAvailable.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserIconOnTaskAvailable.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserMenuOnTaskAvailable.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_139.setStyleSheet("color: #2596be;")     
                        self.pushButton_63.setStyleSheet("color:white;\n"
                                                " background-color:white;") 
                        self.UpperPartOnTaskAssignedReport.setStyleSheet(
                                                "background-color: white;")                     
                        self.MenuButtonOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")       
                        self.LabelforMenuOnTaskAssignedReport.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                        self.BlockforSearchOnTaskAssignedReport.setStyleSheet("#BlockforSearchOnTaskAssignedReport{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                        self.FeildForSearchOnTaskAssignedReport.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;") 
                        self.pushButton_19.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")  
                        self.NotificationIconOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                        "border-radius:5px;\n"
                                                                        "background-color: #2596be;\n"
                                                                        "padding:15px;\n"
                                                                        "\n"
                                                                        "}\n"
                                                                        "")
                        self.UserIconOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserMenuOnTaskAssignedReport.setStyleSheet("background-color:white;\n"
                                                                " border-radius:10px;")
                        self.label_141.setStyleSheet("color: #2596be;") 
                        self.pushButton_69.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.UpperPartOnAsiggningTask.setStyleSheet("background-color: white;")
                        self.MenuButtonOnAsiggningTask.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                        self.LabelforMenuOnAsiggningTask.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "") 
                        self.BlockforSearchOnAsiggningTask.setStyleSheet("#BlockforSearchOnAsiggningTask{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "") 
                        self.FeildForSearchOnAsiggningTask.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                        self.pushButton_20.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.pushButtonOnAsiggningTask.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconOnAsiggningTask.setStyleSheet("#UserIconOnAsiggningTask{ border-radius : 5px;\n"
                                                        "background-color: white;}\n"
                                                        "#UserIconOnAsiggningTask:hover{background-color: #2596be;}") 
                        self.UserMenuOnAsiggningTask.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_140.setStyleSheet("color: #2596be;")
                        self.pushButton_66.setStyleSheet("color:white;\n")
                        self.comboBox_2.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.dateTimeEdit.setStyleSheet("border: 2px solid grey; \n"
                                                " border-radius:5px;\n"
                                                " padding:5px")
                        self.lineEdit_17.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px") 
                        self.lineEdit_17.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")                         
                        self.pushButton_7.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                        self.pushButton.setStyleSheet("background-color: pink;\n"
                                        "padding: 10px;\n"
                                        "color: white;\n"
                                        "")                 
                        self.UpperPartOnUpdateWork.setStyleSheet("background-color: white;")
                        self.MenuButtonOnUpdateWork.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")   
                        self.LabelforMenuOnUpdateWork.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearchOnUpdateWork.setStyleSheet("#BlockforSearchOnUpdateWork{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")     
                        self.FeildForSearchOnUpdateWork.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")  
                        self.pushButton_21.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnUpdateWork.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "") 
                        self.UserIconOnUpdateWork.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "") 
                        self.UserMenuOnUpdateWork.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_142.setStyleSheet("color: #2596be;")
                        self.pushButton_72.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.comboBox_3.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.pushButton_11.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                        self.pushButton_10.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                        self.PageNameOnDashboard_3.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearch_3.setStyleSheet("#BlockforSearch_3{\n"
                                                "border: 2px solid lightblue;\n"
                                                "border-radius: 5px;\n"
                                                "}\n"
                                                "")
                        self.FeildForSearch_3.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                        self.pushButton_22.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconDashboard_3.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconDashboard_3.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                        self.UserMenuOnDashboard_3.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_150.setStyleSheet("color: #2596be;")
                        self.pushButton_96.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.spinBox_2.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.comboBox_9.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.pushButton_8.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: white;\n"
                                                "")
                        self.UpperPartOnUserProfile.setStyleSheet("background-color: white;")
                        self.MenuButtonOnUserProfile.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                        self.LabelforMenuOnUserProfile.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearchOnUserProfile.setStyleSheet("#BlockforSearchOnUserProfile{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                        self.FeildForSearchOnUserProfile.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                        self.pushButton_24.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnUserProfile.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserIconOnUserProfile.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserMenuOnUserProfile.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_143.setStyleSheet("color: #2596be;")
                        self.pushButton_75.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.pushButton_9.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                        self.UpperPartOnTDLProductivity.setStyleSheet(
                                                "background-color: white;")
                        self.MenuButtonOnTDLProductivity.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                        self.LabelforMenuOnTDLProductivity.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                        self.BlockforSearchOnTDLProductivity.setStyleSheet("#BlockforSearchOnTDLProductivity{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                        self.FeildForSearchOnTDLProductivity.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                        self.pushButton_25.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnTDLProductivity.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserIconOnTDLProductivity.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserMenuOnTDLProductivity.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                        self.label_145.setStyleSheet("color: #2596be;")
                        self.pushButton_81.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.pushButton_18.setStyleSheet("color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                        self.lineEdit.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.pushButton_17.setStyleSheet("color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                        self.dateEdit_3.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                        self.UpperPartOnTDLProductivity_2.setStyleSheet(
                                        "background-color: white;")
                        self.MenuButtonOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")
                        self.LabelforMenuOnTDLProductivity_2.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                        self.BlockforSearchOnTDLProductivity_2.setStyleSheet("#BlockforSearchOnTDLProductivity{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                        self.FeildForSearchOnTDLProductivity_2.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                        self.pushButton_26.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                        self.UserIconOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.ContentOnEvaluatePage.setStyleSheet(
                                "QLineEdit{border:2px solid black; border-radius: 5px;}")
                        self.label_61.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_62.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_63.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_64.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_58.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_60.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_65.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_66.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_67.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_57.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.label_56.setStyleSheet(
                                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                        self.pushButton_23.setStyleSheet(
                                "#pushButton_23{\n"
                                                "color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;}\n"
                                                "#pushButton_23:hover{\n"
                                                "color: white;\n"
                                                "padding: 5px;\n"
                                                "background-color: lightblue;}")
                        self.UpperPartOnContactUs.setStyleSheet("background-color: white;")
                        self.MenuButtonOnContactUs.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                        self.LabelforMenuOnContactUs.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                        self.BlockforSearchOnContactUs.setStyleSheet("#BlockforSearchOnContactUs{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                        self.FeildForSearchOnContactUs.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                        self.pushButton_27.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnContactUs.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconOnContactUs.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.UserMenuOnContactUs.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                        self.label_148.setStyleSheet("color: #2596be;")
                        self.pushButton_90.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.ContentOnContactUs.setStyleSheet("background-color: lightgrey;\n"
                                                "border-radius: 15px;")
                        self.lineEdit_15.setStyleSheet("border-radius: 5px;\n"
                                        "border: 2px solid grey;")
                        self.lineEdit_16.setStyleSheet("border-radius: 5px;\n"
                                        "border: 2px solid grey;")
                        self.plainTextEdit.setStyleSheet("border-radius: 15px;\n"
                                                "border: 2px solid grey;")
                        self.pushButton_44.setStyleSheet("background-color: lightblue;\n"
                                                "color: white;\n"
                                                "padding: 10px;")
                        self.UpperPartOnFAQs.setStyleSheet("background-color: white;")
                        self.MenuButtonOnFAQs.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "}")
                        self.LabelforMenuOnFAQs.setStyleSheet("color : #2596be;\n"
                                                "font: bold;\n"
                                                "")
                        self.BlockforSearchOnFAQs.setStyleSheet("#BlockforSearchOnFAQs{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                        self.FeildForSearchOnFAQs.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                        self.pushButton_28.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.NotificationIconOnFAQs.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                        self.UserIconOnFAQs.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                        self.UserMenuOnFAQs.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                        self.label_149.setStyleSheet("color: #2596be;")
                        self.pushButton_93.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                        self.pushButton_2.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                        self.label_3.setStyleSheet(
                                                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                        self.pushButton_3.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                        self.label_6.setStyleSheet(
                                                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                        self.pushButton_4.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                        self.label_7.setStyleSheet(
                                                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                        self.pushButton_5.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                        self.label_38.setStyleSheet(
                                                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                        self.pushButton_6.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                        self.label_39.setStyleSheet(
                                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                        self.widget_9.setStyleSheet("background-color:lightgreen;")
                        self.widget_14.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                        self.widget_15.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                        self.widget_17.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                        self.widget_18.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                        self.widget_27.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                        self.widget_28.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                        self.widget_35.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                        self.widget_36.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                        self.label_37.setStyleSheet("padding: 10px; color: lightblue")
                        self.pushButton_13.setStyleSheet("#pushButton_13 {padding: 0px;} \n #pushButton_13:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_14.setStyleSheet("#pushButton_14 {padding: 0px;} \n #pushButton_14:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_15.setStyleSheet("#pushButton_15 {padding: 0px;} \n #pushButton_15:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_16.setStyleSheet("#pushButton_16 {padding: 0px;} \n #pushButton_16:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_19.setStyleSheet("#pushButton_19 {padding: 0px;} \n #pushButton_19:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_20.setStyleSheet("#pushButton_20 {padding: 0px;} \n #pushButton_20:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_21.setStyleSheet("#pushButton_21 {padding: 0px;} \n #pushButton_21:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_22.setStyleSheet("#pushButton_22 {padding: 0px;} \n #pushButton_22:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_24.setStyleSheet("#pushButton_24 {padding: 0px;} \n #pushButton_24:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_25.setStyleSheet("#pushButton_25 {padding: 0px;} \n #pushButton_25:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_26.setStyleSheet("#pushButton_26 {padding: 0px;} \n #pushButton_26:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_27.setStyleSheet("#pushButton_27 {padding: 0px;} \n #pushButton_27:hover{border-radius:5px; background-color: #2596be;}")
                        self.pushButton_28.setStyleSheet("#pushButton_28 {padding: 0px;} \n #pushButton_28:hover{border-radius:5px; background-color: #2596be;}")
                        self.dark_mode = False
        def add_data_in_dashboard(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_JobRole != %s AND writer_Leader = %s ",('Team Leader', self.Writer_Name))
                record = cur.fetchall()
                i = 0
                j = 0
                writer_ids_list = []
                while i< len(record):
                        writer_ID_to_get_data = record[i][j]
                        writer_ids_list.append(writer_ID_to_get_data)
                        i+=1
                i = 0
                while i < len(writer_ids_list): 
                        writer_ID_to_get_data = writer_ids_list[i]
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT * from writer where writer_ID=%s ",(writer_ID_to_get_data))
                        record_but_another_one = cur.fetchall()
                        self.tableWidget_2.setRowCount(1000)
                        self.comboBox_11.addItem(str(record_but_another_one[0][1]+" "+record_but_another_one[0][2]))
                        self.comboBox_2.addItem(str(record_but_another_one[0][1]+" "+record_but_another_one[0][2]))
                        self.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][1]+" "+record_but_another_one[0][2])))
                        self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][12])))
                        self.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][3])))
                        i+=1
                self.label_82.setText("Data has been added at the Table On Dashboard.")
                self.showmessageandhidemessage(self.label_82)
        def showmessageandhidemessage(self, objecthere):
                self.objecthere = objecthere
                self.animatemessageview_width = QPropertyAnimation(self.objecthere, b'maximumWidth')
                self.animatemessageview_width.setDuration(1000)
                self.animatemessageview_width.setStartValue(0)
                self.animatemessageview_width.setEndValue(100000)
                self.animatemessageview_width.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.animatemessageview__height = QPropertyAnimation(self.objecthere, b'maximumHeight')
                self.animatemessageview__height.setDuration(1000)
                self.animatemessageview__height.setStartValue(0)
                self.animatemessageview__height.setEndValue(100)
                self.animatemessageview__height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.delay = QPropertyAnimation(self.objecthere, b'maximumWidth')
                self.delay.setDuration(1000)
                self.delay.setStartValue(100000)
                self.delay.setEndValue(100000)
                self.delay.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.hidemessageanime_width = QPropertyAnimation(self.objecthere, b'maximumWidth')
                self.hidemessageanime_width.setDuration(1000)
                self.hidemessageanime_width.setStartValue(100000)
                self.hidemessageanime_width.setEndValue(0)
                self.hidemessageanime_width.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.hidemessageanime_height = QPropertyAnimation(self.objecthere, b'maximumHeight')
                self.hidemessageanime_height.setDuration(1000)
                self.hidemessageanime_height.setStartValue(100)
                self.hidemessageanime_height.setEndValue(0)
                self.hidemessageanime_height.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                self.Sequenceformessage = QSequentialAnimationGroup()
                self.Sequenceformessage.addAnimation(self.animatemessageview_width)
                self.Sequenceformessage.addAnimation(self.animatemessageview__height)
                self.Sequenceformessage.addAnimation(self.delay)
                self.Sequenceformessage.addAnimation(self.hidemessageanime_height)
                self.Sequenceformessage.addAnimation(self.hidemessageanime_width)
                self.Sequenceformessage.start()
        def add_data_in_team_report(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_JobRole != %s AND writer_Leader = %s ",('Team Leader', self.Writer_Name))
                record = cur.fetchall()
                i = 0
                j = 0
                writer_ids_list = []
                while i< len(record):
                        writer_ID_to_get_data = record[i][j]
                        writer_ids_list.append(writer_ID_to_get_data)
                        i+=1
                i = 0
                while i < len(writer_ids_list): 
                        writer_ID_to_get_data = writer_ids_list[i]
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT * from writer where writer_ID=%s ",(writer_ID_to_get_data))
                        record_but_another_one = cur.fetchall()

                        self.tableWidget.setRowCount(1000)
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][1]+" "+record_but_another_one[0][2])))
                        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][4]+"\n"+"+"+record_but_another_one[0][5])))
                        self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][4])))
                        self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][5])))
                        self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(record_but_another_one[0][3])))
                        i+=1
        def add_data_in_Task_assigning_report(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_JobRole != %s AND writer_Leader = %s ",('Team Leader', self.Writer_Name))
                record = cur.fetchall()
                i = 0
                j = 0
                writer_ids_list = []
                writer_name_list = []
                while i< len(record):
                        writer_ID_to_get_data = record[i][0]
                        writer_name_list.append(record[i][1]+" "+record[i][2])
                        writer_ids_list.append(writer_ID_to_get_data)
                        i+=1
                i = 0
                while i < len(writer_ids_list): 
                        writer_ID_to_get_data = writer_ids_list[i]
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT * from task where writer_ID_fk= %s ",(writer_ID_to_get_data))
                        record_but_another_one = cur.fetchall()
                        cur.execute("SELECT * from writer where writer_ID= %s ",(writer_ID_to_get_data))
                        record_new = cur.fetchall()
                        j = 0
                        while j < len(record_but_another_one):
                                self.ContentOnTaskAssignedReport.setRowCount(1000)
                                self.ContentOnTaskAssignedReport.setItem(j, 0, QtWidgets.QTableWidgetItem(str(str(record_new[0][1])+" "+str(record_new[0][2]))))
                                self.ContentOnTaskAssignedReport.setItem(j, 1, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][0])))
                                self.ContentOnTaskAssignedReport.setItem(j, 2, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][1])))
                                self.ContentOnTaskAssignedReport.setItem(j, 3, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][5])))
                                j+=1
                        i+=1
        def add_data_in_Manage_Team_Leaves(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_JobRole != %s AND writer_Leader = %s ",('Team Leader', self.Writer_Name))
                record = cur.fetchall()
                i = 0
                j = 0
                writer_ids_list = []
                writer_name_list = []
                while i< len(record):
                        writer_ID_to_get_data = record[i][0]
                        writer_name_list.append(record[i][1]+" "+record[i][2])
                        writer_ids_list.append(writer_ID_to_get_data)
                        i+=1
                i = 0
                while i < len(writer_ids_list): 
                        writer_ID_to_get_data = writer_ids_list[i]
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT * from leaves where writer_ID_fk= %s AND leaves_status <> %s ",(writer_ID_to_get_data, "Accepted"))
                        record_but_another_one = cur.fetchall()
                        cur.execute("SELECT * from writer where writer_ID= %s ",(writer_ID_to_get_data))
                        record_new = cur.fetchall()
                        j = 0
                        while j < len(record_but_another_one):
                                self.tableWidget_6.setRowCount(1000)
                                self.tableWidget_6.setItem(j, 0, QtWidgets.QTableWidgetItem(str(str(record_new[0][1])+" "+str(record_new[0][2]))))
                                self.tableWidget_6.setItem(j, 1, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][4])))
                                self.tableWidget_6.setItem(j, 2, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][6])))
                                self.tableWidget_6.setItem(j, 3, QtWidgets.QTableWidgetItem(str(record_but_another_one[j][7])))
                                j+=1
                        i+=1
        def on_click_Add_on_TDL(self):
                if self.widget_8.height() != 0:
                        self.opencustomfeilds = QPropertyAnimation(self.widget_8, b'maximumHeight')
                        self.opencustomfeilds.setDuration(1000)
                        self.opencustomfeilds.setStartValue(self.widget_8.height())
                        self.opencustomfeilds.setEndValue(0)
                        self.opencustomfeilds.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.opencustomfeilds.start()
        def add_data_in_permanency(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from writer where writer_JobRole != %s AND writer_Leader = %s ",('Team Leader', self.Writer_Name))
                record = cur.fetchall()
                i = 0
                self.writer_ids_list = []
                self.writer_name_list = []
                while i< len(record):
                        writer_ID_to_get_data = record[i][0]
                        self.writer_name_list.append(record[i][1]+" "+record[i][2])
                        self.writer_ids_list.append(writer_ID_to_get_data)
                        i+=1
                i = 0
                while i < len(self.writer_ids_list):
                        self.ContentOnPermanencyReport.setRowCount(1000)
                        self.ContentOnPermanencyReport.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.writer_name_list[i])))
                        self.ContentOnPermanencyReport.setItem(i, 1, QtWidgets.QTableWidgetItem(str(record[i][21])))
                        self.ContentOnPermanencyReport.setItem(i, 2, QtWidgets.QTableWidgetItem(str(record[i][22])))
                        i+=1
        def add_data_in_received_task(self):
                i = 0
                while i < len(self.writer_ids_list):
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT * from task where writer_ID_fk = %s",str(self.writer_ids_list[i]))
                        self.Tasks = cur.fetchall()
                        self.tableWidget_3.setRowCount(1000)
                        j = 0
                        row = 0
                        while j < len(self.Tasks):
                                if self.Tasks[j][4] == "Forwarded":
                                        self.tableWidget_3.setItem(row, 0, QtWidgets.QTableWidgetItem(str(self.Tasks[j][0])))
                                        self.tableWidget_3.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.Tasks[j][1])))
                                        self.tableWidget_3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.writer_name_list[i])))
                                        self.tableWidget_3.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.Tasks[j][6])))
                                        self.tableWidget_3.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.Tasks[j][4])))
                                        row+=1
                                j+=1
                        i+=1
                self.MessageOnRecievedTask.setText("Data has been added at the Table On Recieved Task Form.")
                self.showmessageandhidemessage(self.MessageOnRecievedTask)        
        def add_data_in_TDL_Productivity(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * from custom_task_tl where writer_ID_fk = %s",str(self.TL_ID))
                Custom_Tasks = cur.fetchall()
                self.tableWidget_5.setRowCount(1000)
                j = 0
                while j < len(Custom_Tasks):
                        if Custom_Tasks[j][3] != "Confirmed":
                                self.comboBox_3.addItem(str(Custom_Tasks[j][1]))
                                self.tableWidget_5.setItem(j, 0, QtWidgets.QTableWidgetItem(str(Custom_Tasks[j][1])))
                                self.tableWidget_5.setItem(j, 1, QtWidgets.QTableWidgetItem(str(Custom_Tasks[j][2])))
                        j+=1
        def write_file(self, directory, document):
        # Convert binary data to proper format and write it on Hard Disk
                self.directory = directory
                self.document = document
                with open(directory, 'wb') as file:
                        file.write(document)
        def on_selectionChange_table_widget3(self, selected, deselect): 
                try:
                        for ix in selected.indexes():
                                if ix.column() == 0:
                                        self.text_from_column = str(self.tableWidget_3.selectedItems()[ix.column()].text())
                                        self.label_18.setText(self.text_from_column)
                                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                                        cur = con.cursor()
                                        cur.execute("SELECT task_Topic from task where task_ID = %s",str(self.text_from_column))
                                        record = cur.fetchall()
                                        Topic = str(record[0][0])
                                        self.label_68.setText(Topic)
                except:
                        self.label_18.setText("Select a Task")
                        self.label_68.setText("No Task Selected")
        def on_selectionChange_table_widget6(self, selected, deselect):
                try:
                        name_of_writer = self.tableWidget_6.selectedItems()[0].text()
                        Leaves_Reason = self.tableWidget_6.selectedItems()[1].text()
                        Leaves_from = self.tableWidget_6.selectedItems()[2].text()
                        Leaves_to = self.tableWidget_6.selectedItems()[3].text()
                        self.label_75.setText(name_of_writer)
                        self.label_77.setText(Leaves_Reason)
                        self.label_79.setText(Leaves_from+" "+Leaves_to)
                except:
                        self.label_75.setText("Nothing is Selected")
                        self.label_77.setText("Nothing is Selected")
                        self.label_77.setText("Nothing is Selected")
                        self.label_79.setText("Nothing is Selected")
        def On_Clicking_Download_Button_in_Recieved_Task(self):
                try:
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("SELECT task_uploaded_file from task where task_ID = %s",self.text_from_column)
                        file = cur.fetchall()
                        self.write_file(r"./Documents/"+self.text_from_column,file[0][0])
                        self.MessageOnRecievedTask.setText("Your file has been downloaded to ./Documents/"+self.text_from_column)
                        self.showmessageandhidemessage(self.MessageOnRecievedTask)
                except:
                        pass
        def On_Clicking_Update_Button_in_Recieved_Task(self):
                try:
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("update task set task_Palagrism=%s where task_ID = %s",(self.doubleSpinBox.text() , self.text_from_column))
                        if float(self.doubleSpinBox.text()) > float(10.0):
                                cur.execute("update task set task_Status=%s where task_ID = %s",("Declined Due to Palagrism" , self.text_from_column))
                        else:
                                cur.execute("update task set task_Status=%s where task_ID = %s",("Approved" , self.text_from_column))
                        con.commit()
                        cur.close()
                        self.MessageOnRecievedTask.setText("Task with ID: " +str(self.text_from_column)+ " is updated with Palagrism Rate of "+str(self.doubleSpinBox.text()))
                        self.showmessageandhidemessage(self.MessageOnRecievedTask)
                except:
                        self.MessageOnRecievedTask.setText("Connection Error")
                        self.showmessageandhidemessage(self.MessageOnRecievedTask)
        def Insert_data_at_assign_to_db(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("Select * from writer where writer_FName+" "+writer_LName = %s",(self.comboBox_2.currentText()))
                record = cur.fetchall()
                cur.execute("INSERT INTO task (task_Topic, writer_ID_fk, task_Deadline, task_WordCount) values (%s,%s,%s,%s)",(self.lineEdit_14.text() , record[0][0], self.dateTimeEdit.text(), self.lineEdit_17.text()))
                con.commit()
                cur.close()
                self.MessageOnAssigningTask.setText("Task has been Assigned to "+self.comboBox_2.currentText())
                self.showmessageandhidemessage(self.MessageOnAssigningTask)
                self.add_data_in_Task_assigning_report()
        def Create_New_Custom_Task(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("INSERT INTO custom_task_tl (custom_Title, custom_Deadline, writer_ID_fk) values (%s,%s,%s)",(self.lineEdit.text(), self.dateEdit_3.text(), self.TL_ID))
                con.commit()
                cur.close()
                self.add_data_in_TDL_Productivity()
                self.MessageOnTDL.setText("Task was added in your To-do-List")
                self.showmessageandhidemessage(self.MessageOnTDL)
        def on_combobox_changed_by_update_work(self, value):
                self.value = value
                if value == "Confirmed":
                        self.OpenWidget_to_open_on_update_work = QPropertyAnimation(self.widget_23, b'maximumHeight')
                        self.OpenWidget_to_open_on_update_work.setDuration(1000)
                        self.OpenWidget_to_open_on_update_work.setStartValue(self.widget_23.height())
                        self.OpenWidget_to_open_on_update_work.setEndValue(0)
                        self.OpenWidget_to_open_on_update_work.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.OpenWidget_to_open_on_update_work.start()
                else:
                        self.OpenWidget_to_open_on_update_work = QPropertyAnimation(self.widget_23, b'maximumHeight')
                        self.OpenWidget_to_open_on_update_work.setDuration(1000)
                        self.OpenWidget_to_open_on_update_work.setStartValue(0)
                        self.OpenWidget_to_open_on_update_work.setEndValue(200)
                        self.OpenWidget_to_open_on_update_work.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.OpenWidget_to_open_on_update_work.start()
        def on_combobox_changed(self, value):
                self.value = value
                if value == "Custom Designation":
                        self.OpenWidget_to_open_on_update_work = QPropertyAnimation(self.widget_94, b'maximumHeight')
                        self.OpenWidget_to_open_on_update_work.setDuration(1000)
                        self.OpenWidget_to_open_on_update_work.setStartValue(0)
                        self.OpenWidget_to_open_on_update_work.setEndValue(200)
                        self.OpenWidget_to_open_on_update_work.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.OpenWidget_to_open_on_update_work.start()
                else:
                        self.OpenWidget_to_open_on_update_work = QPropertyAnimation(self.widget_94, b'maximumHeight')
                        self.OpenWidget_to_open_on_update_work.setDuration(1000)
                        self.OpenWidget_to_open_on_update_work.setStartValue(self.widget_94.height())
                        self.OpenWidget_to_open_on_update_work.setEndValue(0)
                        self.OpenWidget_to_open_on_update_work.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.OpenWidget_to_open_on_update_work.start()
        def Insert_data_to_db_from_update_task(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("Select custom_ID from custom_task_tl where custom_Title = %s",(self.comboBox_3.currentText()))
                record = cur.fetchall()
                if self.comboBox_4.currentText() == "Delayed":
                        cur.execute("update custom_task_tl set custom_Status = %s,custom_Deadline =%s where custom_ID = %s",(self.comboBox_4.currentText(), self.dateEdit.text() ,record[0][0]))
                        con.commit()
                        cur.close()
                        self.MessageOnUpdateWork.setText("New date for selected task has been updated and has been set to "+self.dateEdit.text())
                        self.showmessageandhidemessage(self.MessageOnUpdateWork)
                elif self.comboBox_4.currentText() == "Confirmed":
                        cur.execute("update custom_task_tl set custom_Status = %s where custom_ID = %s",(self.comboBox_4.currentText(), record[0][0]))
                        con.commit()
                        cur.close()
                        self.MessageOnUpdateWork.setText("Your Task has been status is confirmed")
                        self.showmessageandhidemessage(self.MessageOnUpdateWork)
        def Insert_data_to_db_from_update_designation(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                name = self.comboBox_11.currentText().split(" ")
                if self.comboBox_12.currentText() == "Custom Designation":
                        cur.execute("update writer set writer_JobRole = %s where writer_FName= %s AND writer_LName= %s" ,(self.lineEdit_33.text(), name[0],name[1]))
                        self.MessageOnUpdateDesignation.setText("Update Designation for "+self.comboBox_11.currentText()+" is "+self.lineEdit_33.text())
                        self.showmessageandhidemessage(self.MessageOnUpdateDesignation)
                else:
                        cur.execute("update writer set writer_JobRole =  %s where writer_FName= %s AND writer_LName= %s",(self.comboBox_12.currentText(),  name[0],name[1]))
                        self.MessageOnUpdateDesignation.setText("Update Designation for "+self.comboBox_11.currentText()+" is "+self.comboBox_12.currentText())
                        self.showmessageandhidemessage(self.MessageOnUpdateDesignation)
                con.commit()
                cur.close()
        def add_data_in_manage_leave_table(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("SELECT * FROM `leaves` WHERE `writer_ID_fk` = %s AND `leaves_status` <> %s;",(self.TL_ID, "Accepted"))
                record = cur.fetchall()
                writer_ID_fk = []
                leaves_Amount = []
                leaves_Reason = []
                leaves_Date = []
                leaves_DeductionType = []
                leaves_status = []
                row = 0
                while row < len(record):
                        writer_ID_fk.append(record[row][1])
                        leaves_Amount.append(record[row][2])
                        leaves_Reason.append(record[row][4])
                        leaves_Date.append(record[row][6])
                        leaves_DeductionType.append(record[row][3])
                        leaves_status.append(record[row][7])
                        if str(self.TL_ID) == str(writer_ID_fk[row]) and leaves_status[row] != "Accepted":
                                self.tableWidget_4.setRowCount(1000)
                                self.tableWidget_4.setItem(row, 0, QtWidgets.QTableWidgetItem(str(leaves_Amount[row])))
                                self.tableWidget_4.setItem(row, 1, QtWidgets.QTableWidgetItem(str(leaves_Reason[row])))
                                self.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem(leaves_DeductionType[row]))
                                self.tableWidget_4.setItem(row, 3, QtWidgets.QTableWidgetItem(leaves_Date[row]))
                                self.tableWidget_4.setItem(row, 4, QtWidgets.QTableWidgetItem(leaves_status[row]))
                        row += 1
        def On_click_submit_on_Manage_Leaves(self):
                total_list = 0
                if self.spinBox_2.text() == 0 or self.spinBox_2.text() == "0":
                        # self.MessageOnManageLeaves.setText("Number of leaves cannot contain ""0"" value")
                        # self.showmessageandhidemessage(self.MessageOnManageLeaves)
                        pass
                elif self.textEdit.toPlainText() == '':
                        # self.MessageOnManageLeaves.setText("Reason feild cannot be empty.")
                        # self.showmessageandhidemessage(self.MessageOnManageLeaves)
                        pass
                elif  len(self.textEdit.toPlainText().split(" ")) < 150:
                        total_list = len(self.textEdit.toPlainText().split(" "))
                        # self.MessageOnManageLeaves.setText("Reason feild must contain a valid reason for about 150 words. Total word counts for now is "+str(total_list))
                        # self.showmessageandhidemessage(self.MessageOnManageLeaves)
                else:
                        # self.MessageOnManageLeaves.setText("Your leaves and deduction types are updated.")
                        # self.showmessageandhidemessage(self.MessageOnManageLeaves)
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("insert into leaves (writer_ID_fk, leaves_Amount, leaves_DeductionType, leaves_Reason, leaves_document, leaves_from_date, leaves_status) values (%s,%s,%s,%s,%s,%s,%s)",(
                                self.TL_ID,
                                str(int(self.spinBox_2.text())),
                                self.comboBox_9.currentText(),
                                self.textEdit.toPlainText(),
                                str(self.BinaryData_from_manage_leaves),
                                self.dateEdit_2.text(),
                                "Pending",
                                ))
                        con.commit()
                        con.close()
                        self.add_data_in_manage_leave_table()
        def On_click_change_picture_on_profile(self):
                try:
                        directory, _ = QtWidgets.QFileDialog.getOpenFileName()
                        with open(directory, "rb") as File:
                                self.BinaryData_from_picture = File.read()
                        con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                        cur = con.cursor()
                        cur.execute("update writer set writer_Image = %s where writer_Email = %s ",(self.BinaryData_from_picture, self.Writer_Email))
                        con.commit()
                        con.close()
                        self.MessageOnProfile.setText("Picture Updated")
                        self.showmessageandhidemessage(self.MessageOnProfile)
                except:
                        self.MessageOnProfile.setText("There was an error uploading picture. Please upload maximum of 5 MB file.")
                        self.showmessageandhidemessage(self.MessageOnProfile)
        def On_click_change_picture_on_manage_leaves(self):
                try:
                        directory, _ = QtWidgets.QFileDialog.getOpenFileName()
                        with open(directory, "rb") as File:
                                self.BinaryData_from_manage_leaves = File.read()
                        self.MessageOnManageLeaves.setText("File has been loaded from "+directory)
                        self.showmessageandhidemessage(self.MessageOnManageLeaves)
                except:
                        self.MessageOnManageLeaves.setText("There was an error uploading picture. Please upload maximum of 5 MB file.")
                        self.showmessageandhidemessage(self.MessageOnManageLeaves)
        def Add_data_to_Designation_Combo_Box(self):
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("select designation_Title from designation")
                record = cur.fetchall()
                i = 0
                while i < len(record):
                        self.comboBox_12.addItem(record[i][0])
                        i+=1
                con.commit()
                con.close()
                self.comboBox_12.addItem("Custom Designation")
        def on_click_Upload_file_On_Assign_Task(self):
                directory, _ = QtWidgets.QFileDialog.getOpenFileName()
                if directory != '':
                        with open(directory, "rb") as File:
                                self.BinaryData_from_Assign_Task = File.read()
                                self.MessageOnAssigningTask.setText("File is loaded from: "+directory)
                                self.showmessageandhidemessage(self.MessageOnAssigningTask)
                                self.pushButton_7.setStyleSheet("background-color: lightgreen; padding: 10px; border-radius: 15px;")
        def function_to_be_called_to_add_data(self):
                self.Connect_Functions_With_Button()
                self.add_data_in_dashboard()
                self.add_data_in_team_report()
                self.add_data_in_Task_assigning_report()
                self.add_data_in_permanency()
                self.add_data_in_received_task()
                self.add_data_in_TDL_Productivity()
                self.add_data_in_manage_leave_table()
                self.add_data_in_Manage_Team_Leaves()
                self.Add_data_to_Designation_Combo_Box()
                self.on_combobox_changed_by_update_work("Delayed")
                self.on_combobox_changed("something here burh")
        def last_details(self):
                self.label_46.setPixmap(QtGui.QPixmap.scaled(QtGui.QPixmap(self.Writer_Image),300,300,aspectRatioMode= Qt.KeepAspectRatio))
                self.label_19.setPixmap(QtGui.QPixmap.scaled(QtGui.QPixmap(self.Writer_Image),300,300,aspectRatioMode= Qt.KeepAspectRatio))
        def on_click_accept_button_at_manage_leaves(self):
                Reason = self.label_77.text()
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("UPDATE `leaves` SET `leaves_status`='Accepted' WHERE `leaves_Reason` = %s;",(Reason))
                con.commit()
                cur.close()
                self.MessageOnManageTeamLeaves.setText("Leave with Reason "+Reason+" has been accepted.")
                self.MessageOnManageTeamLeaves.setStyleSheet("background-color: lightgreen; padding: 15px; border-radius: 15px;")
                self.showmessageandhidemessage(self.MessageOnManageTeamLeaves)        
        def on_click_decline_button_at_manage_leaves(self):
                Reason = self.label_77.text()
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("UPDATE `leaves` SET `leaves_status`='Rejected' WHERE `leaves_Reason` = %s;",(Reason))
                con.commit()
                cur.close()
                self.MessageOnManageTeamLeaves.setText("Leave with Reason "+Reason+" has been rejected.")
                self.MessageOnManageTeamLeaves.setStyleSheet("background-color: red; padding: 15px; border-radius: 15px;")
                self.showmessageandhidemessage(self.MessageOnManageTeamLeaves)        
        def Connect_Functions_With_Button(self):
                # Opening Pages
                self.DashboardBtn.clicked.connect(self.show_Dashboard)
                self.UpdateRecievedTaskBtn.clicked.connect(self.show_RecievedTask)
                self.WriterProgressBtn.clicked.connect(self.show_TeamReport)
                self.PermanentReportBtn.clicked.connect(self.show_PermanencyReport)
                self.TaskApprovedBtn.clicked.connect(self.show_TaskAvailable)
                self.TaskAssignedBtn.clicked.connect(self.show_TaskAssinged)
                self.AssignTaskBtn.clicked.connect(self.show_AssignTask)
                self.WordCountReport.clicked.connect(self.show_UpdateWork)
                self.ManageLeavesBtn.clicked.connect(self.show_ManageLeaves)
                self.UpdateDesignationBtn.clicked.connect(self.show_Update_Designation)
                self.ProfileBtn.clicked.connect(self.show_UserProfile)
                self.TDLBtn.clicked.connect(self.show_TDLProductivity)
                self.ManageTeamLeavesBtn.clicked.connect(self.show_MangeTeamLeaves)
                self.ManageExpensesBtn.clicked.connect(self.show_EvaluationForm)
                self.ContactUsBtn.clicked.connect(self.show_ContactUs)
                self.FAQsBtn.clicked.connect(self.show_FAQs)
                self.pushButton_32.clicked.connect(self.on_click_accept_button_at_manage_leaves)
                self.pushButton_33.clicked.connect(self.on_click_decline_button_at_manage_leaves)

                # Opening Menu Function
                self.MenuButtonOnDashboard.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnDashboard_2.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnPermanencyReport.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnTaskAvailable.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnTaskAssignedReport.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnAsiggningTask.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnDashboard_3.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnUpdateWork.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnUserProfile.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnTDLProductivity.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnTDLProductivity_2.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnContactUs.clicked.connect(self.open_leftmenu)
                self.MenuButtonOnFAQs.clicked.connect(self.open_leftmenu)

                # Dark Mode Button Connection
                self.pushButton_13.clicked.connect(self.dark_mode_on)
                self.pushButton_14.clicked.connect(self.dark_mode_on)
                self.pushButton_15.clicked.connect(self.dark_mode_on)
                self.pushButton_16.clicked.connect(self.dark_mode_on)
                self.pushButton_19.clicked.connect(self.dark_mode_on)
                self.pushButton_20.clicked.connect(self.dark_mode_on)
                self.pushButton_21.clicked.connect(self.dark_mode_on)
                self.pushButton_22.clicked.connect(self.dark_mode_on)
                self.pushButton_24.clicked.connect(self.dark_mode_on)
                self.pushButton_25.clicked.connect(self.dark_mode_on)
                self.pushButton_26.clicked.connect(self.dark_mode_on)
                self.pushButton_27.clicked.connect(self.dark_mode_on)
                self.pushButton_28.clicked.connect(self.dark_mode_on)
                self.pushButton_29.clicked.connect(self.dark_mode_on)
                self.pushButton_31.clicked.connect(self.dark_mode_on)
                self.pushButton_169.clicked.connect(self.dark_mode_on)

                #For Opening User Logout Menu
                self.UserIconDashboard.clicked.connect(self.showUserMenuOnDashboard)
                self.UserIconDashboard_2.clicked.connect(self.showUserMenuOnTeamReport)
                self.UserIconOnPermanencyReport.clicked.connect(self.showUserMenuOnPermanency)
                self.UserIconOnTaskAvailable.clicked.connect(self.showUserMenuOnTaskAvailable)
                self.UserIconOnTaskAssignedReport.clicked.connect(self.showUserMenuOnAssingedTask)
                self.UserIconOnAsiggningTask.clicked.connect(self.showUserMenuOnAssingingTask)
                self.UserIconOnUpdateWork.clicked.connect(self.showUserMenuOnUpdateWork)
                self.UserIconDashboard_3.clicked.connect(self.showUserMenuOnManageLeaves)
                self.UserIconOnUserProfile.clicked.connect(self.showUserMenuOnProfile)
                self.UserIconOnTDLProductivity.clicked.connect(self.showUserMenuOnTDL)
                self.UserIconOnTDLProductivity_2.clicked.connect(self.showUserMenuOnEvaluation)
                self.UserIconOnContactUs.clicked.connect(self.showUserMenuOnContactUs)
                self.UserIconOnFAQs.clicked.connect(self.showUserMenuOnFAQs)
                self.UserIconDashboard_4.clicked.connect(self.showUserMenuOnRecievedTask)
                self.UserIconDashboard_4.clicked.connect(self.showUserMenuOnRecievedTask)
                self.UserIconOnUpdateWork_3.clicked.connect(self.showUserMenuOnUpdateDesignation)
                self.UserIconOnTDLProductivity_3.clicked.connect(self.showUserMenuOnManageTeamLeaves)

                # Upper Menu Button Connection
                self.UpperButtonClose.clicked.connect(self.closewindow)
                self.UpperButtonMaximize.clicked.connect(self.maximizewindow)
                self.UpperButtonMinimize.clicked.connect(self.minimzewindow)

                # Open Notification Buttons Connection
                self.NotificationIconDashboard.clicked.connect(self.open_notification_Board)
                self.NotificationIconDashboard_2.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnPermanencyReport.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTaskAvailable.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTaskAssignedReport.clicked.connect(self.open_notification_Board)
                self.pushButtonOnAsiggningTask.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnUpdateWork.clicked.connect(self.open_notification_Board)
                self.NotificationIconDashboard_3.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnUserProfile.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTDLProductivity.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTDLProductivity_2.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnContactUs.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnFAQs.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTaskAvailable.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnUpdateWork.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnUserProfile.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnContactUs.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnFAQs.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnTDLProductivity_3.clicked.connect(self.open_notification_Board)
                self.NotificationIconOnUpdateWork_3.clicked.connect(self.open_notification_Board)
                self.NotificationIconDashboard_4.clicked.connect(self.open_notification_Board)

                self.pushButton_18.clicked.connect(self.on_click_Add_on_TDL) 

                self.label_46.setPixmap(QtGui.QPixmap.scaled(QtGui.QPixmap(self.Writer_Image),300,300,aspectRatioMode= Qt.KeepAspectRatio))
                self.label_19.setPixmap(QtGui.QPixmap.scaled(QtGui.QPixmap(self.Writer_Image),300,300,aspectRatioMode= Qt.KeepAspectRatio))

                self.tableWidget_3.selectionModel().selectionChanged.connect(self.on_selectionChange_table_widget3)
                self.tableWidget_6.selectionModel().selectionChanged.connect(self.on_selectionChange_table_widget6)
                self.pushButton_11.clicked.connect(self.On_Clicking_Download_Button_in_Recieved_Task)
                self.pushButton_30.clicked.connect(self.On_Clicking_Update_Button_in_Recieved_Task)
                self.pushButton.clicked.connect(self.Insert_data_at_assign_to_db)
                self.pushButton_18.clicked.connect(self.Create_New_Custom_Task)
                self.pushButton_10.clicked.connect(self.Insert_data_to_db_from_update_task)
                self.comboBox_4.currentTextChanged.connect(self.on_combobox_changed_by_update_work)
                self.comboBox_12.currentTextChanged.connect(self.on_combobox_changed)
                self.pushButton_8.clicked.connect(self.On_click_submit_on_Manage_Leaves)
                self.pushButton_34.clicked.connect(self.On_click_change_picture_on_profile)
                self.pushButton_170.clicked.connect(self.Insert_data_to_db_from_update_designation)
                self.pushButton_12.clicked.connect(self.on_click_Download_Report_On_Dashboard)                
                self.pushButton_7.clicked.connect(self.on_click_Upload_file_On_Assign_Task)
                self.pushButton_35.clicked.connect(self.On_click_change_picture_on_manage_leaves)

                self.BinaryData_from_manage_leaves = ""

                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("Select writer_ID from writer where writer_email = %s",(self.Writer_Email))
                record = cur.fetchall()
                self.TL_ID = record[0][0]
                con.commit()
                cur.close()
        def on_click_Download_Report_On_Dashboard(self):
                self.label_82.setText("Your file has been downloaded")
                self.showmessageandhidemessage(self.label_82)
        def add_Team_Leader_in_Evaluation_Form(self, Leader):
                self.Leader = Leader
                self.comboBox.addItem(Leader)
        def on_click_evaluate_in_evaluation_form(self):
                self.MessageOnEvaluation.setText(self.Leader+" has been evaluated.")
                self.showmessageandhidemessage(self.MessageOnEvaluation)
                con = sql.connect(host='localhost', user='root', password='', db='fcs_writer')
                cur = con.cursor()
                cur.execute("select writer_ID from writer where writer_JobRole = %s AND writer_Team = %s",('Team Leader', self.Team_Name))
                record = cur.fetchall()
                Leader_ID = record[0][0]
                cur.execute("insert into evaluation (Leader_ID_FK, Writer_ID_FK, P_and_R_Time, Team_Spirit, Instruction, Initiatives, Attitude_and_Behaviour, In_and_out, Coordination_and_FollowUp, Focused_to_new_learning, Planning_and_Management, Team_Management, Honesty_and_Empathy) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        str(Leader_ID),
                        str(self.TL_ID),
                        str(self.lineEdit_3.text()),  
                        str(self.lineEdit_4.text()),  
                        str(self.lineEdit_5.text()),  
                        str(self.lineEdit_6.text()),  
                        str(self.lineEdit_7.text()),  
                        str(self.lineEdit_8.text()),  
                        str(self.lineEdit_9.text()),  
                        str(self.lineEdit_10.text()),  
                        str(self.lineEdit_11.text()),  
                        str(self.lineEdit_12.text()),  
                        str(self.lineEdit_13.text()),  
                        ))
                con.commit()
                con.close()
        def setupUi(self):
                self.MainWindow.setObjectName("self.MainWindow")
                self.MainWindow.resize(859, 828)
                self.MainWindow.setMinimumSize(QtCore.QSize(0, 0))
                self.MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.MainWindow.setStyleSheet(
                "background-color: #2596be; border-radius:15px;")
                self.centralwidget = QtWidgets.QWidget(self.MainWindow)
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.UpperBelt = QtWidgets.QWidget(self.centralwidget)
                self.UpperBelt.setStyleSheet(
                "background-color: #2596be;; border-radius:15px; border: 2px solid rgba(255,255,255,0.6);")
                self.UpperBelt.setObjectName("UpperBelt")
                self.horizontalLayout_107 = QtWidgets.QHBoxLayout(self.UpperBelt)
                self.horizontalLayout_107.setObjectName("horizontalLayout_107")
                spacerItem = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_107.addItem(spacerItem)
                self.UpperButtonMinimize = QtWidgets.QPushButton(self.UpperBelt)
                self.UpperButtonMinimize.setStyleSheet("#UpperButtonMinimize{\n"
                                                "border: none;\n"
                                                "}  \n"
                                                "#UpperButtonMinimize:hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: lightgreen;\n"
                                                " border: none;} ")
                self.UpperButtonMinimize.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/minus.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpperButtonMinimize.setIcon(icon)
                self.UpperButtonMinimize.setObjectName("UpperButtonMinimize")
                self.horizontalLayout_107.addWidget(self.UpperButtonMinimize)
                self.UpperButtonMaximize = QtWidgets.QPushButton(self.UpperBelt)
                self.UpperButtonMaximize.setStyleSheet("#UpperButtonMaximize{\n"
                                                "border: none;\n"
                                                "} \n"
                                                "#UpperButtonMaximize:hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: yellow;\n"
                                                "} ")
                self.UpperButtonMaximize.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/maximize-2.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpperButtonMaximize.setIcon(icon1)
                self.UpperButtonMaximize.setObjectName("UpperButtonMaximize")
                self.horizontalLayout_107.addWidget(self.UpperButtonMaximize)
                self.UpperButtonClose = QtWidgets.QPushButton(self.UpperBelt)
                self.UpperButtonClose.setStyleSheet("#UpperButtonClose{\n"
                                                "border: none;\n"
                                                "}\n"
                                                "#UpperButtonClose:hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: red;\n"
                                                "} ")
                self.UpperButtonClose.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/x.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpperButtonClose.setIcon(icon2)
                self.UpperButtonClose.setObjectName("UpperButtonClose")
                self.horizontalLayout_107.addWidget(self.UpperButtonClose)
                self.verticalLayout.addWidget(self.UpperBelt)
                self.widget_2 = QtWidgets.QWidget(self.centralwidget)
                self.widget_2.setObjectName("widget_2")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.LeftMenu = QtWidgets.QWidget(self.widget_2)
                self.LeftMenu.setMinimumSize(QtCore.QSize(0, 0))
                self.LeftMenu.setMaximumSize(QtCore.QSize(350, 16777215))
                self.LeftMenu.setStyleSheet("#UpdateDesignationBtn:hover, #ManageTeamLeavesBtn:hover, #WriterProgressBtn:hover, #UpdateRecievedTaskBtn:hover, #WriterDashboardBtn:hover, #WordCountReport:hover, #TaskAssignedBtn:hover, #TaskApprovedBtn:hover, #TDLBtn:hover, #RegisterClientBtn:hover,    #ProfileBtn:hover, #PermanentReportBtn:hover, #PaymentBtn:hover, #ManageWordCountBtn:hover,    #ManageLeavesBtn:hover, #ManageExpensesBtn:hover, #InProgressBtn:hover,    #FAQsBtn:hover,   #DashboardBtn:hover,#ContactUsBtn:hover,#AssignTaskBtn:hover,#ClientDetailsBtn:hover{\n"
                                        "    background-color: white;\n"
                                        "    text-align:center;\n"
                                        "    margin-right: 5%;\n"
                                        "    }\n"
                                        "#UpdateDesignationBtn, #ManageTeamLeavesBtn, #WriterProgressBtn, #UpdateRecievedTaskBtn, #WriterDashboardBtn, #WordCountReport, #TaskAssignedBtn, #TaskApprovedBtn, #TDLBtn, #RegisterClientBtn, #ProfileBtn, #PermanentReportBtn, #PaymentBtn,    #ManageWordCountBtn, #ManageLeavesBtn, #InProgressBtn, #FAQsBtn, #DashboardBtn,    #ContactUsBtn,    #ManageExpensesBtn, #ClientDetailsBtn,    #AssignTaskBtn{\n"
                                        "    border-radius:5px;\n"
                                        "    background-color:transparent;padding:5px;text-align:left;\n"
                                        "    }\n"
                                        "#UpdateDesignationBtn:focus, #ManageTeamLeavesBtn:focus, #WriterProgressBtn:focus, #WriterDashboardBtn:focus, #UpdateRecievedTaskBtn:focus , #WordCountReport:focus, #TaskAssignedBtn:focus, #TaskApprovedBtn:focus, #TDLBtn:focus, #RegisterClientBtn:focus, #ProfileBtn:focus, #PermanentReportBtn:focus, #PaymentBtn:focus,    #ManageWordCountBtn:focus, #ManageLeavesBtn:focus, #InProgressBtn:focus, #FAQsBtn:focus, #DashboardBtn:focus,    #ContactUsBtn:focus,    #ManageExpensesBtn:focus, #ClientDetailsBtn:focus,    #AssignTaskBtn:focus{\n"
                                        "    border-top-left-radius:15px;\n"
                                        "    border-top-right-radius:0px;\n"
                                        "    border-bottom-left-radius: 0px;\n"
                                        "    border-bottom-right-radius: 0px;\n"
                                        "    background-color:white;\n"
                                        "    padding:5px;\n"
                                        "    text-align:right;\n"
                                        "    }")
                self.LeftMenu.setObjectName("LeftMenu")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftMenu)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.LabelForMenu = QtWidgets.QLabel(self.LeftMenu)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                self.LabelForMenu.setFont(font)
                self.LabelForMenu.setStyleSheet("color:#2596be;\n"
                                                " background-color: black;\n"
                                                " border-radius:5px")
                self.LabelForMenu.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelForMenu.setObjectName("LabelForMenu")
                self.verticalLayout_2.addWidget(self.LabelForMenu)
                spacerItem1 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem1)
                self.DashboardBtn = QtWidgets.QPushButton(self.LeftMenu)
                self.DashboardBtn.setMaximumSize(QtCore.QSize(16777213, 16777215))
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.DashboardBtn.setFont(font)
                self.DashboardBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.DashboardBtn.setStyleSheet("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/airplay.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.DashboardBtn.setIcon(icon3)
                self.DashboardBtn.setObjectName("DashboardBtn")
                self.verticalLayout_2.addWidget(self.DashboardBtn)
                self.UpdateRecievedTaskBtn = QtWidgets.QPushButton(self.LeftMenu)
                self.UpdateRecievedTaskBtn.setMaximumSize(
                QtCore.QSize(16777213, 16777215))
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.UpdateRecievedTaskBtn.setFont(font)
                self.UpdateRecievedTaskBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UpdateRecievedTaskBtn.setStyleSheet("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/check.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.UpdateRecievedTaskBtn.setIcon(icon4)
                self.UpdateRecievedTaskBtn.setObjectName("UpdateRecievedTaskBtn")
                self.verticalLayout_2.addWidget(self.UpdateRecievedTaskBtn)
                self.WriterProgressBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.WriterProgressBtn.setFont(font)
                self.WriterProgressBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.WriterProgressBtn.setStyleSheet("")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons/cpu.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.WriterProgressBtn.setIcon(icon5)
                self.WriterProgressBtn.setObjectName("WriterProgressBtn")
                self.verticalLayout_2.addWidget(self.WriterProgressBtn)
                self.PermanentReportBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.PermanentReportBtn.setFont(font)
                self.PermanentReportBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.PermanentReportBtn.setStyleSheet("")
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(
                ":/Icons/Icons/check-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.PermanentReportBtn.setIcon(icon6)
                self.PermanentReportBtn.setObjectName("PermanentReportBtn")
                self.verticalLayout_2.addWidget(self.PermanentReportBtn)
                self.TaskApprovedBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.TaskApprovedBtn.setFont(font)
                self.TaskApprovedBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.TaskApprovedBtn.setStyleSheet("")
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap(
                ":/Icons/Icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.TaskApprovedBtn.setIcon(icon7)
                self.TaskApprovedBtn.setObjectName("TaskApprovedBtn")
                self.verticalLayout_2.addWidget(self.TaskApprovedBtn)
                self.TaskAssignedBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.TaskAssignedBtn.setFont(font)
                self.TaskAssignedBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.TaskAssignedBtn.setStyleSheet("")
                icon8 = QtGui.QIcon()
                icon8.addPixmap(QtGui.QPixmap(":/Icons/Icons/bar-chart-2.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.TaskAssignedBtn.setIcon(icon8)
                self.TaskAssignedBtn.setObjectName("TaskAssignedBtn")
                self.verticalLayout_2.addWidget(self.TaskAssignedBtn)
                self.AssignTaskBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.AssignTaskBtn.setFont(font)
                self.AssignTaskBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.AssignTaskBtn.setStyleSheet("")
                icon9 = QtGui.QIcon()
                icon9.addPixmap(QtGui.QPixmap(":/Icons/Icons/at-sign.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.AssignTaskBtn.setIcon(icon9)
                self.AssignTaskBtn.setObjectName("AssignTaskBtn")
                self.verticalLayout_2.addWidget(self.AssignTaskBtn)
                self.WordCountReport = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.WordCountReport.setFont(font)
                self.WordCountReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.WordCountReport.setStyleSheet("")
                self.WordCountReport.setIcon(icon4)
                self.WordCountReport.setObjectName("WordCountReport")
                self.verticalLayout_2.addWidget(self.WordCountReport)
                self.UpdateDesignationBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.UpdateDesignationBtn.setFont(font)
                self.UpdateDesignationBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UpdateDesignationBtn.setStyleSheet("")
                self.UpdateDesignationBtn.setIcon(icon6)
                self.UpdateDesignationBtn.setObjectName("UpdateDesignationBtn")
                self.verticalLayout_2.addWidget(self.UpdateDesignationBtn)
                self.ManageLeavesBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.ManageLeavesBtn.setFont(font)
                self.ManageLeavesBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.ManageLeavesBtn.setStyleSheet("")
                icon10 = QtGui.QIcon()
                icon10.addPixmap(QtGui.QPixmap(":/Icons/Icons/activity.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ManageLeavesBtn.setIcon(icon10)
                self.ManageLeavesBtn.setObjectName("ManageLeavesBtn")
                self.verticalLayout_2.addWidget(self.ManageLeavesBtn)
                self.ProfileBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.ProfileBtn.setFont(font)
                self.ProfileBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.ProfileBtn.setStyleSheet("")
                icon11 = QtGui.QIcon()
                icon11.addPixmap(QtGui.QPixmap(":/Icons/Icons/user.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ProfileBtn.setIcon(icon11)
                self.ProfileBtn.setObjectName("ProfileBtn")
                self.verticalLayout_2.addWidget(self.ProfileBtn)
                self.TDLBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.TDLBtn.setFont(font)
                self.TDLBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.TDLBtn.setStyleSheet("")
                icon12 = QtGui.QIcon()
                icon12.addPixmap(QtGui.QPixmap(
                ":/Icons/Icons/bar-chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.TDLBtn.setIcon(icon12)
                self.TDLBtn.setObjectName("TDLBtn")
                self.verticalLayout_2.addWidget(self.TDLBtn)
                self.ManageTeamLeavesBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.ManageTeamLeavesBtn.setFont(font)
                self.ManageTeamLeavesBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.ManageTeamLeavesBtn.setStyleSheet("")
                icon13 = QtGui.QIcon()
                icon13.addPixmap(QtGui.QPixmap(":/Icons/Icons/phone.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ManageTeamLeavesBtn.setIcon(icon13)
                self.ManageTeamLeavesBtn.setObjectName("ManageTeamLeavesBtn")
                self.verticalLayout_2.addWidget(self.ManageTeamLeavesBtn)
                self.ManageExpensesBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.ManageExpensesBtn.setFont(font)
                self.ManageExpensesBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.ManageExpensesBtn.setStyleSheet("")
                icon14 = QtGui.QIcon()
                icon14.addPixmap(QtGui.QPixmap(":/Icons/Icons/sliders.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ManageExpensesBtn.setIcon(icon14)
                self.ManageExpensesBtn.setObjectName("ManageExpensesBtn")
                self.verticalLayout_2.addWidget(self.ManageExpensesBtn)
                self.ContactUsBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.ContactUsBtn.setFont(font)
                self.ContactUsBtn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.ContactUsBtn.setStyleSheet("")
                self.ContactUsBtn.setIcon(icon13)
                self.ContactUsBtn.setObjectName("ContactUsBtn")
                self.verticalLayout_2.addWidget(self.ContactUsBtn)
                self.FAQsBtn = QtWidgets.QPushButton(self.LeftMenu)
                font = QtGui.QFont()
                font.setFamily("Malgun Gothic")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.FAQsBtn.setFont(font)
                self.FAQsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.FAQsBtn.setStyleSheet("")
                icon15 = QtGui.QIcon()
                icon15.addPixmap(QtGui.QPixmap(":/Icons/Icons/codepen.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.FAQsBtn.setIcon(icon15)
                self.FAQsBtn.setObjectName("FAQsBtn")
                self.verticalLayout_2.addWidget(self.FAQsBtn)
                spacerItem2 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem2)
                self.horizontalLayout.addWidget(self.LeftMenu)
                self.RightForm = QtWidgets.QStackedWidget(self.widget_2)
                self.RightForm.setMinimumSize(QtCore.QSize(500, 0))
                self.RightForm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.RightForm.setStyleSheet("background-color:white;\n"
                                        "border-radius:15px;")
                self.RightForm.setObjectName("RightForm")
                self.DashboardAdmin = QtWidgets.QWidget()
                self.DashboardAdmin.setStyleSheet("#MenuButtonOnDashboard:hover{\n"
                                                "background-color: #2596be;\n"
                                                "}")
                self.DashboardAdmin.setObjectName("DashboardAdmin")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DashboardAdmin)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.RightShit = QtWidgets.QWidget(self.DashboardAdmin)
                self.RightShit.setStyleSheet("#HeaderFrame\n"
                                        "{\n"
                                        "background-color: white;\n"
                                        "}\n"
                                        "#Table\n"
                                        "{\n"
                                        "background-color: #2596be;\n"
                                        "}\n"
                                        "\n"
                                        "#BlockforSearch {\n"
                                        "border-radius: 5px;\n"
                                        "border: 2px solid #2596be;\n"
                                        "}\n"
                                        "")
                self.RightShit.setObjectName("RightShit")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.RightShit)
                self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.UpperPartDashboard = QtWidgets.QWidget(self.RightShit)
                self.UpperPartDashboard.setObjectName("UpperPartDashboard")
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
                self.UpperPartDashboard)
                self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_8.setSpacing(0)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.MenuMiscContainerDashboard = QtWidgets.QWidget(
                self.UpperPartDashboard)
                self.MenuMiscContainerDashboard.setObjectName(
                "MenuMiscContainerDashboard")
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout(
                self.MenuMiscContainerDashboard)
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                self.MenuButtonOnDashboard = QtWidgets.QPushButton(
                self.MenuMiscContainerDashboard)
                self.MenuButtonOnDashboard.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnDashboard.setText("")
                icon16 = QtGui.QIcon()
                icon16.addPixmap(QtGui.QPixmap(":/Icons/Icons/menu.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.MenuButtonOnDashboard.setIcon(icon16)
                self.MenuButtonOnDashboard.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnDashboard.setFlat(True)
                self.MenuButtonOnDashboard.setObjectName("MenuButtonOnDashboard")
                self.horizontalLayout_9.addWidget(self.MenuButtonOnDashboard)
                self.PageNameOnDashboard = QtWidgets.QLabel(
                self.MenuMiscContainerDashboard)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.PageNameOnDashboard.setFont(font)
                self.PageNameOnDashboard.setStyleSheet("color : #2596be;\n"
                                                "font: bold;\n"
                                                "")
                self.PageNameOnDashboard.setAlignment(QtCore.Qt.AlignCenter)
                self.PageNameOnDashboard.setObjectName("PageNameOnDashboard")
                self.horizontalLayout_9.addWidget(self.PageNameOnDashboard)
                self.horizontalLayout_8.addWidget(
                self.MenuMiscContainerDashboard, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.SearchMiscContainerDashboard = QtWidgets.QWidget(
                self.UpperPartDashboard)
                self.SearchMiscContainerDashboard.setObjectName(
                "SearchMiscContainerDashboard")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(
                self.SearchMiscContainerDashboard)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.BlockforSearch = QtWidgets.QFrame(
                self.SearchMiscContainerDashboard)
                self.BlockforSearch.setStyleSheet("")
                self.BlockforSearch.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BlockforSearch.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearch.setObjectName("BlockforSearch")
                self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.BlockforSearch)
                self.horizontalLayout_11.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_11.setSpacing(0)
                self.horizontalLayout_11.setObjectName("horizontalLayout_11")
                self.SearchIcon = QtWidgets.QLabel(self.BlockforSearch)
                self.SearchIcon.setText("")
                self.SearchIcon.setPixmap(QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIcon.setObjectName("SearchIcon")
                self.horizontalLayout_11.addWidget(
                self.SearchIcon, 0, QtCore.Qt.AlignRight)
                self.FeildForSearch = QtWidgets.QLineEdit(self.BlockforSearch)
                self.FeildForSearch.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                self.FeildForSearch.setObjectName("FeildForSearch")
                self.horizontalLayout_11.addWidget(
                self.FeildForSearch, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_10.addWidget(
                self.BlockforSearch, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_8.addWidget(self.SearchMiscContainerDashboard)
                self.RightIconMiscContainer = QtWidgets.QWidget(
                self.UpperPartDashboard)
                self.RightIconMiscContainer.setObjectName("RightIconMiscContainer")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
                self.RightIconMiscContainer)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.pushButton_13 = QtWidgets.QPushButton(self.RightIconMiscContainer)
                self.pushButton_13.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_13.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_13.setText("")
                icon17 = QtGui.QIcon()
                icon17.addPixmap(QtGui.QPixmap(":/Icons/Icons/sun.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_13.setIcon(icon17)
                self.pushButton_13.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_13.setObjectName("pushButton_13")
                self.horizontalLayout_5.addWidget(self.pushButton_13)
                self.NotificationIconDashboard = QtWidgets.QPushButton(
                self.RightIconMiscContainer)
                self.NotificationIconDashboard.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconDashboard.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconDashboard.setText("")
                icon18 = QtGui.QIcon()
                icon18.addPixmap(QtGui.QPixmap(":/Icons/Icons/bell.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.NotificationIconDashboard.setIcon(icon18)
                self.NotificationIconDashboard.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconDashboard.setObjectName(
                "NotificationIconDashboard")
                self.horizontalLayout_5.addWidget(self.NotificationIconDashboard)
                self.UserIconDashboard = QtWidgets.QPushButton(
                self.RightIconMiscContainer)
                self.UserIconDashboard.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconDashboard.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                self.UserIconDashboard.setText("")
                self.UserIconDashboard.setIcon(icon11)
                self.UserIconDashboard.setIconSize(QtCore.QSize(32, 32))
                self.UserIconDashboard.setObjectName("UserIconDashboard")
                self.horizontalLayout_5.addWidget(self.UserIconDashboard)
                self.horizontalLayout_8.addWidget(
                self.RightIconMiscContainer, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_3.addWidget(
                self.UpperPartDashboard, 0, QtCore.Qt.AlignTop)
                self.widget_29 = QtWidgets.QWidget(self.RightShit)
                self.widget_29.setMinimumSize(QtCore.QSize(0, 0))
                self.widget_29.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_29.setObjectName("widget_29")
                self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.widget_29)
                self.verticalLayout_66.setObjectName("verticalLayout_66")
                self.label_82 = QtWidgets.QLabel(self.widget_29)
                self.label_82.setMinimumSize(QtCore.QSize(0, 0))
                self.label_82.setMaximumSize(QtCore.QSize(16777215, 0))
                self.label_82.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.label_82.setObjectName("label_82")
                self.verticalLayout_66.addWidget(self.label_82)
                self.verticalLayout_3.addWidget(self.widget_29)
                self.frameforUserMenu_2 = QtWidgets.QWidget(self.RightShit)
                self.frameforUserMenu_2.setObjectName("frameforUserMenu_2")
                self.horizontalLayout_92 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_2)
                self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_92.setSpacing(0)
                self.horizontalLayout_92.setObjectName("horizontalLayout_92")
                self.UserMenuOnDashboard = QtWidgets.QWidget(self.frameforUserMenu_2)
                self.UserMenuOnDashboard.setEnabled(False)
                self.UserMenuOnDashboard.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnDashboard.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnDashboard.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                self.UserMenuOnDashboard.setObjectName("UserMenuOnDashboard")
                self.verticalLayout_44 = QtWidgets.QVBoxLayout(
                self.UserMenuOnDashboard)
                self.verticalLayout_44.setObjectName("verticalLayout_44")
                self.label_135 = QtWidgets.QLabel(self.UserMenuOnDashboard)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_135.setFont(font)
                self.label_135.setStyleSheet("color: #2596be;")
                self.label_135.setObjectName("label_135")
                self.verticalLayout_44.addWidget(
                self.label_135, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_51 = QtWidgets.QPushButton(self.UserMenuOnDashboard)
                self.pushButton_51.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_51.setText("")
                icon19 = QtGui.QIcon()
                icon19.addPixmap(QtGui.QPixmap(
                ":/Icons/Icons/instagram.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_51.setIcon(icon19)
                self.pushButton_51.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_51.setObjectName("pushButton_51")
                self.verticalLayout_44.addWidget(
                self.pushButton_51, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_52 = QtWidgets.QPushButton(self.UserMenuOnDashboard)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_52.setFont(font)
                self.pushButton_52.setIcon(icon11)
                self.pushButton_52.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_52.setObjectName("pushButton_52")
                self.verticalLayout_44.addWidget(
                self.pushButton_52, 0, QtCore.Qt.AlignLeft)
                self.pushButton_53 = QtWidgets.QPushButton(self.UserMenuOnDashboard)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_53.setFont(font)
                icon20 = QtGui.QIcon()
                icon20.addPixmap(QtGui.QPixmap(":/Icons/Icons/log-out.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_53.setIcon(icon20)
                self.pushButton_53.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_53.setObjectName("pushButton_53")
                self.verticalLayout_44.addWidget(
                self.pushButton_53, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_92.addWidget(self.UserMenuOnDashboard)
                self.verticalLayout_3.addWidget(
                self.frameforUserMenu_2, 0, QtCore.Qt.AlignRight)
                self.CardHolder = QtWidgets.QWidget(self.RightShit)
                self.CardHolder.setObjectName("CardHolder")
                self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.CardHolder)
                self.horizontalLayout_13.setObjectName("horizontalLayout_13")
                self.Card1 = QtWidgets.QWidget(self.CardHolder)
                self.Card1.setObjectName("Card1")
                self.gridLayout_6 = QtWidgets.QGridLayout(self.Card1)
                self.gridLayout_6.setObjectName("gridLayout_6")
                self.Card1ValueString = QtWidgets.QLabel(self.Card1)
                font = QtGui.QFont()
                font.setFamily("MS Serif")
                font.setPointSize(10)
                self.Card1ValueString.setFont(font)
                self.Card1ValueString.setObjectName("Card1ValueString")
                self.gridLayout_6.addWidget(
                self.Card1ValueString, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
                self.Card1Value = QtWidgets.QLabel(self.Card1)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.Card1Value.setFont(font)
                self.Card1Value.setObjectName("Card1Value")
                self.gridLayout_6.addWidget(self.Card1Value, 0, 1, 1, 1)
                self.Card1Icon = QtWidgets.QLabel(self.Card1)
                self.Card1Icon.setText("")
                self.Card1Icon.setPixmap(QtGui.QPixmap(":/Icons/Icons/users.svg"))
                self.Card1Icon.setObjectName("Card1Icon")
                self.gridLayout_6.addWidget(
                self.Card1Icon, 0, 0, 2, 1, QtCore.Qt.AlignRight)
                self.horizontalLayout_13.addWidget(self.Card1)
                self.Card2 = QtWidgets.QWidget(self.CardHolder)
                self.Card2.setObjectName("Card2")
                self.gridLayout_7 = QtWidgets.QGridLayout(self.Card2)
                self.gridLayout_7.setObjectName("gridLayout_7")
                self.CardV2Value = QtWidgets.QLabel(self.Card2)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.CardV2Value.setFont(font)
                self.CardV2Value.setObjectName("CardV2Value")
                self.gridLayout_7.addWidget(
                self.CardV2Value, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
                self.Card2ValueString = QtWidgets.QLabel(self.Card2)
                font = QtGui.QFont()
                font.setFamily("MS Serif")
                font.setPointSize(10)
                self.Card2ValueString.setFont(font)
                self.Card2ValueString.setObjectName("Card2ValueString")
                self.gridLayout_7.addWidget(
                self.Card2ValueString, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
                self.Card2Icon = QtWidgets.QLabel(self.Card2)
                self.Card2Icon.setText("")
                self.Card2Icon.setPixmap(QtGui.QPixmap(
                ":/Icons/Icons/shopping-cart.svg"))
                self.Card2Icon.setObjectName("Card2Icon")
                self.gridLayout_7.addWidget(
                self.Card2Icon, 0, 0, 2, 1, QtCore.Qt.AlignRight)
                self.horizontalLayout_13.addWidget(self.Card2)
                self.verticalLayout_3.addWidget(self.CardHolder)
                self.widget_3 = QtWidgets.QWidget(self.RightShit)
                self.widget_3.setObjectName("widget_3")
                self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.widget_3)
                self.verticalLayout_63.setObjectName("verticalLayout_63")
                self.ContentOnWriterDashboard = QtWidgets.QWidget(self.widget_3)
                self.ContentOnWriterDashboard.setStyleSheet(
                "background-color: lightblue;")
                self.ContentOnWriterDashboard.setObjectName("ContentOnWriterDashboard")
                self.verticalLayout_64 = QtWidgets.QVBoxLayout(
                self.ContentOnWriterDashboard)
                self.verticalLayout_64.setObjectName("verticalLayout_64")
                self.widget_10 = QtWidgets.QWidget(self.ContentOnWriterDashboard)
                self.widget_10.setObjectName("widget_10")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_10)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.widget_12 = QtWidgets.QWidget(self.widget_10)
                self.widget_12.setObjectName("widget_12")
                self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.widget_12)
                self.verticalLayout_62.setObjectName("verticalLayout_62")
                self.label_40 = QtWidgets.QLabel(self.widget_12)
                font = QtGui.QFont()
                font.setFamily("MS PGothic")
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)
                self.label_40.setFont(font)
                self.label_40.setStyleSheet("")
                self.label_40.setObjectName("label_40")
                self.verticalLayout_62.addWidget(self.label_40)
                self.widget_13 = QtWidgets.QWidget(self.widget_12)
                self.widget_13.setObjectName("widget_13")
                self.horizontalLayout_114 = QtWidgets.QHBoxLayout(self.widget_13)
                self.horizontalLayout_114.setObjectName("horizontalLayout_114")
                self.label_41 = QtWidgets.QLabel(self.widget_13)
                font = QtGui.QFont()
                font.setFamily("MS PGothic")
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)
                self.label_41.setFont(font)
                self.label_41.setStyleSheet("color:lightgreen;")
                self.label_41.setObjectName("label_41")
                self.horizontalLayout_114.addWidget(
                self.label_41, 0, QtCore.Qt.AlignRight)
                self.label_42 = QtWidgets.QLabel(self.widget_13)
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)
                self.label_42.setFont(font)
                self.label_42.setObjectName("label_42")
                self.horizontalLayout_114.addWidget(
                self.label_42, 0, QtCore.Qt.AlignLeft)
                self.verticalLayout_62.addWidget(self.widget_13)
                self.widget_16 = QtWidgets.QWidget(self.widget_12)
                self.widget_16.setObjectName("widget_16")
                self.gridLayout = QtWidgets.QGridLayout(self.widget_16)
                self.gridLayout.setObjectName("gridLayout")
                self.label_44 = QtWidgets.QLabel(self.widget_16)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_44.setFont(font)
                self.label_44.setObjectName("label_44")
                self.gridLayout.addWidget(self.label_44, 0, 0, 1, 1)
                spacerItem3 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
                self.pushButton_12 = QtWidgets.QPushButton(self.widget_16)
                self.pushButton_12.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                self.pushButton_12.setObjectName("pushButton_12")
                self.gridLayout.addWidget(self.pushButton_12, 3, 0, 1, 2)
                self.label_10 = QtWidgets.QLabel(self.widget_16)
                self.label_10.setObjectName("label_10")
                self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
                self.label_9 = QtWidgets.QLabel(self.widget_16)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setObjectName("label_9")
                self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
                self.label_43 = QtWidgets.QLabel(self.widget_16)
                self.label_43.setObjectName("label_43")
                self.gridLayout.addWidget(self.label_43, 1, 1, 1, 1)
                self.verticalLayout_62.addWidget(self.widget_16)
                self.horizontalLayout_2.addWidget(self.widget_12)
                self.label_46 = QtWidgets.QLabel(self.widget_10)
                self.label_46.setText("")
                self.label_46.setPixmap(QtGui.QPixmap("../Icons/Template Image.png"))
                self.label_46.setObjectName("label_46")
                self.horizontalLayout_2.addWidget(
                self.label_46, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_64.addWidget(self.widget_10)
                self.verticalLayout_63.addWidget(self.ContentOnWriterDashboard)
                self.verticalLayout_3.addWidget(self.widget_3)
                self.label_8 = QtWidgets.QLabel(self.RightShit)
                font = QtGui.QFont()
                font.setFamily("MS PGothic")
                font.setPointSize(24)
                self.label_8.setFont(font)
                self.label_8.setAlignment(QtCore.Qt.AlignCenter)
                self.label_8.setObjectName("label_8")
                self.verticalLayout_3.addWidget(self.label_8)
                self.tableWidget_2 = QtWidgets.QTableWidget(self.RightShit)
                self.tableWidget_2.setStyleSheet("background-color:lightblue;")
                self.tableWidget_2.setObjectName("tableWidget_2")
                self.tableWidget_2.setColumnCount(4)
                self.tableWidget_2.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(3, item)
                self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
                self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
                self.tableWidget_2.verticalHeader().setSortIndicatorShown(True)
                self.tableWidget_2.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_3.addWidget(self.tableWidget_2)
                spacerItem4 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_3.addItem(spacerItem4)
                self.verticalLayout_4.addWidget(self.RightShit)
                self.RightForm.addWidget(self.DashboardAdmin)
                self.WriterProgressPage = QtWidgets.QWidget()
                self.WriterProgressPage.setObjectName("WriterProgressPage")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.WriterProgressPage)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.UpperPartDashboard_2 = QtWidgets.QWidget(self.WriterProgressPage)
                self.UpperPartDashboard_2.setObjectName("UpperPartDashboard_2")
                self.horizontalLayout_14 = QtWidgets.QHBoxLayout(
                self.UpperPartDashboard_2)
                self.horizontalLayout_14.setContentsMargins(6, 6, 6, 6)
                self.horizontalLayout_14.setSpacing(6)
                self.horizontalLayout_14.setObjectName("horizontalLayout_14")
                self.MenuMiscContainerDashboard_2 = QtWidgets.QWidget(
                self.UpperPartDashboard_2)
                self.MenuMiscContainerDashboard_2.setObjectName(
                "MenuMiscContainerDashboard_2")
                self.horizontalLayout_15 = QtWidgets.QHBoxLayout(
                self.MenuMiscContainerDashboard_2)
                self.horizontalLayout_15.setObjectName("horizontalLayout_15")
                self.MenuButtonOnDashboard_2 = QtWidgets.QPushButton(
                self.MenuMiscContainerDashboard_2)
                self.MenuButtonOnDashboard_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnDashboard_2.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.MenuButtonOnDashboard_2.setText("")
                self.MenuButtonOnDashboard_2.setIcon(icon16)
                self.MenuButtonOnDashboard_2.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnDashboard_2.setFlat(True)
                self.MenuButtonOnDashboard_2.setObjectName("MenuButtonOnDashboard_2")
                self.horizontalLayout_15.addWidget(self.MenuButtonOnDashboard_2)
                self.PageNameOnDashboard_2 = QtWidgets.QLabel(
                self.MenuMiscContainerDashboard_2)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.PageNameOnDashboard_2.setFont(font)
                self.PageNameOnDashboard_2.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.PageNameOnDashboard_2.setAlignment(QtCore.Qt.AlignCenter)
                self.PageNameOnDashboard_2.setObjectName("PageNameOnDashboard_2")
                self.horizontalLayout_15.addWidget(self.PageNameOnDashboard_2)
                self.horizontalLayout_14.addWidget(
                self.MenuMiscContainerDashboard_2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.SearchMiscContainerDashboard_2 = QtWidgets.QWidget(
                self.UpperPartDashboard_2)
                self.SearchMiscContainerDashboard_2.setObjectName(
                "SearchMiscContainerDashboard_2")
                self.horizontalLayout_16 = QtWidgets.QHBoxLayout(
                self.SearchMiscContainerDashboard_2)
                self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                self.BlockforSearch_2 = QtWidgets.QFrame(
                self.SearchMiscContainerDashboard_2)
                self.BlockforSearch_2.setStyleSheet("#BlockforSearch_2{\n"
                                                "border: 2px solid lightblue;\n"
                                                "border-radius: 5px;\n"
                                                "}")
                self.BlockforSearch_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BlockforSearch_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearch_2.setObjectName("BlockforSearch_2")
                self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.BlockforSearch_2)
                self.horizontalLayout_17.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_17.setSpacing(0)
                self.horizontalLayout_17.setObjectName("horizontalLayout_17")
                self.SearchIcon_2 = QtWidgets.QLabel(self.BlockforSearch_2)
                self.SearchIcon_2.setText("")
                self.SearchIcon_2.setPixmap(QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIcon_2.setObjectName("SearchIcon_2")
                self.horizontalLayout_17.addWidget(
                self.SearchIcon_2, 0, QtCore.Qt.AlignRight)
                self.FeildForSearch_2 = QtWidgets.QLineEdit(self.BlockforSearch_2)
                self.FeildForSearch_2.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                self.FeildForSearch_2.setObjectName("FeildForSearch_2")
                self.horizontalLayout_17.addWidget(
                self.FeildForSearch_2, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_16.addWidget(
                self.BlockforSearch_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_14.addWidget(self.SearchMiscContainerDashboard_2)
                self.RightIconMiscContainer_2 = QtWidgets.QWidget(
                self.UpperPartDashboard_2)
                self.RightIconMiscContainer_2.setObjectName("RightIconMiscContainer_2")
                self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
                self.RightIconMiscContainer_2)
                self.horizontalLayout_12.setObjectName("horizontalLayout_12")
                self.pushButton_14 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_2)
                self.pushButton_14.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_14.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_14.setText("")
                self.pushButton_14.setIcon(icon17)
                self.pushButton_14.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_14.setObjectName("pushButton_14")
                self.horizontalLayout_12.addWidget(self.pushButton_14)
                self.NotificationIconDashboard_2 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_2)
                self.NotificationIconDashboard_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconDashboard_2.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconDashboard_2.setText("")
                self.NotificationIconDashboard_2.setIcon(icon18)
                self.NotificationIconDashboard_2.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconDashboard_2.setObjectName(
                "NotificationIconDashboard_2")
                self.horizontalLayout_12.addWidget(self.NotificationIconDashboard_2)
                self.UserIconDashboard_2 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_2)
                self.UserIconDashboard_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconDashboard_2.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                self.UserIconDashboard_2.setText("")
                self.UserIconDashboard_2.setIcon(icon11)
                self.UserIconDashboard_2.setIconSize(QtCore.QSize(32, 32))
                self.UserIconDashboard_2.setObjectName("UserIconDashboard_2")
                self.horizontalLayout_12.addWidget(self.UserIconDashboard_2)
                self.horizontalLayout_14.addWidget(
                self.RightIconMiscContainer_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_5.addWidget(self.UpperPartDashboard_2)
                self.widget_30 = QtWidgets.QWidget(self.WriterProgressPage)
                self.widget_30.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_30.setStyleSheet("")
                self.widget_30.setObjectName("widget_30")
                self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.widget_30)
                self.verticalLayout_67.setObjectName("verticalLayout_67")
                self.label_83 = QtWidgets.QLabel(self.widget_30)
                self.label_83.setMaximumSize(QtCore.QSize(16777215, 0))
                self.label_83.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.label_83.setObjectName("label_83")
                self.verticalLayout_67.addWidget(self.label_83)
                self.verticalLayout_5.addWidget(self.widget_30)
                self.frameforUserMenu_4 = QtWidgets.QWidget(self.WriterProgressPage)
                self.frameforUserMenu_4.setObjectName("frameforUserMenu_4")
                self.horizontalLayout_94 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_4)
                self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_94.setSpacing(0)
                self.horizontalLayout_94.setObjectName("horizontalLayout_94")
                self.UserMenuOnDashboard_2 = QtWidgets.QWidget(self.frameforUserMenu_4)
                self.UserMenuOnDashboard_2.setEnabled(False)
                self.UserMenuOnDashboard_2.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnDashboard_2.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnDashboard_2.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnDashboard_2.setObjectName("UserMenuOnDashboard_2")
                self.verticalLayout_46 = QtWidgets.QVBoxLayout(
                self.UserMenuOnDashboard_2)
                self.verticalLayout_46.setObjectName("verticalLayout_46")
                self.label_137 = QtWidgets.QLabel(self.UserMenuOnDashboard_2)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_137.setFont(font)
                self.label_137.setStyleSheet("color: #2596be;")
                self.label_137.setObjectName("label_137")
                self.verticalLayout_46.addWidget(
                self.label_137, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_57 = QtWidgets.QPushButton(self.UserMenuOnDashboard_2)
                self.pushButton_57.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_57.setText("")
                self.pushButton_57.setIcon(icon19)
                self.pushButton_57.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_57.setObjectName("pushButton_57")
                self.verticalLayout_46.addWidget(
                self.pushButton_57, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_58 = QtWidgets.QPushButton(self.UserMenuOnDashboard_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_58.setFont(font)
                self.pushButton_58.setIcon(icon11)
                self.pushButton_58.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_58.setObjectName("pushButton_58")
                self.verticalLayout_46.addWidget(
                self.pushButton_58, 0, QtCore.Qt.AlignLeft)
                self.pushButton_59 = QtWidgets.QPushButton(self.UserMenuOnDashboard_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_59.setFont(font)
                self.pushButton_59.setIcon(icon20)
                self.pushButton_59.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_59.setObjectName("pushButton_59")
                self.verticalLayout_46.addWidget(
                self.pushButton_59, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_94.addWidget(self.UserMenuOnDashboard_2)
                self.verticalLayout_5.addWidget(
                self.frameforUserMenu_4, 0, QtCore.Qt.AlignRight)
                self.tableWidget = QtWidgets.QTableWidget(self.WriterProgressPage)
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(4, item)
                self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget.horizontalHeader().setDefaultSectionSize(138)
                self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
                self.tableWidget.verticalHeader().setSortIndicatorShown(True)
                self.tableWidget.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_5.addWidget(self.tableWidget)
                self.RightForm.addWidget(self.WriterProgressPage)
                self.PermanencyReport = QtWidgets.QWidget()
                self.PermanencyReport.setObjectName("PermanencyReport")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.PermanencyReport)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.UpperPartOnPermanencyReport = QtWidgets.QWidget(
                self.PermanencyReport)
                self.UpperPartOnPermanencyReport.setStyleSheet(
                "background-color: white;")
                self.UpperPartOnPermanencyReport.setObjectName(
                "UpperPartOnPermanencyReport")
                self.horizontalLayout_19 = QtWidgets.QHBoxLayout(
                self.UpperPartOnPermanencyReport)
                self.horizontalLayout_19.setObjectName("horizontalLayout_19")
                self.MenuButtonMiscOnPermanencyReport = QtWidgets.QWidget(
                self.UpperPartOnPermanencyReport)
                self.MenuButtonMiscOnPermanencyReport.setObjectName(
                "MenuButtonMiscOnPermanencyReport")
                self.horizontalLayout_20 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnPermanencyReport)
                self.horizontalLayout_20.setObjectName("horizontalLayout_20")
                self.MenuButtonOnPermanencyReport = QtWidgets.QPushButton(
                self.MenuButtonMiscOnPermanencyReport)
                self.MenuButtonOnPermanencyReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnPermanencyReport.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")
                self.MenuButtonOnPermanencyReport.setText("")
                self.MenuButtonOnPermanencyReport.setIcon(icon16)
                self.MenuButtonOnPermanencyReport.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnPermanencyReport.setFlat(True)
                self.MenuButtonOnPermanencyReport.setObjectName(
                "MenuButtonOnPermanencyReport")
                self.horizontalLayout_20.addWidget(self.MenuButtonOnPermanencyReport)
                self.LabelforMenuOnPermanencyReport = QtWidgets.QLabel(
                self.MenuButtonMiscOnPermanencyReport)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnPermanencyReport.setFont(font)
                self.LabelforMenuOnPermanencyReport.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                self.LabelforMenuOnPermanencyReport.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnPermanencyReport.setObjectName(
                "LabelforMenuOnPermanencyReport")
                self.horizontalLayout_20.addWidget(self.LabelforMenuOnPermanencyReport)
                self.horizontalLayout_19.addWidget(
                self.MenuButtonMiscOnPermanencyReport, 0, QtCore.Qt.AlignLeft)
                self.SearchBarOnPermanencyReport = QtWidgets.QWidget(
                self.UpperPartOnPermanencyReport)
                self.SearchBarOnPermanencyReport.setObjectName(
                "SearchBarOnPermanencyReport")
                self.horizontalLayout_21 = QtWidgets.QHBoxLayout(
                self.SearchBarOnPermanencyReport)
                self.horizontalLayout_21.setObjectName("horizontalLayout_21")
                self.BlockforSearchOnPermanencyReport = QtWidgets.QFrame(
                self.SearchBarOnPermanencyReport)
                self.BlockforSearchOnPermanencyReport.setStyleSheet("#BlockforSearchOnPermanencyReport{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnPermanencyReport.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnPermanencyReport.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnPermanencyReport.setObjectName(
                "BlockforSearchOnPermanencyReport")
                self.horizontalLayout_22 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnPermanencyReport)
                self.horizontalLayout_22.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_22.setSpacing(0)
                self.horizontalLayout_22.setObjectName("horizontalLayout_22")
                self.SearchIconOnPermanencyReport = QtWidgets.QLabel(
                self.BlockforSearchOnPermanencyReport)
                self.SearchIconOnPermanencyReport.setText("")
                self.SearchIconOnPermanencyReport.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnPermanencyReport.setObjectName(
                "SearchIconOnPermanencyReport")
                self.horizontalLayout_22.addWidget(self.SearchIconOnPermanencyReport)
                self.FeildForSearchOnPermanencyReport = QtWidgets.QLineEdit(
                self.BlockforSearchOnPermanencyReport)
                self.FeildForSearchOnPermanencyReport.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnPermanencyReport.setObjectName(
                "FeildForSearchOnPermanencyReport")
                self.horizontalLayout_22.addWidget(
                self.FeildForSearchOnPermanencyReport)
                self.horizontalLayout_21.addWidget(
                self.BlockforSearchOnPermanencyReport, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_19.addWidget(
                self.SearchBarOnPermanencyReport, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.UserButtonOnPermanencyReport = QtWidgets.QWidget(
                self.UpperPartOnPermanencyReport)
                self.UserButtonOnPermanencyReport.setObjectName(
                "UserButtonOnPermanencyReport")
                self.horizontalLayout_18 = QtWidgets.QHBoxLayout(
                self.UserButtonOnPermanencyReport)
                self.horizontalLayout_18.setObjectName("horizontalLayout_18")
                self.pushButton_15 = QtWidgets.QPushButton(
                self.UserButtonOnPermanencyReport)
                self.pushButton_15.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_15.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_15.setText("")
                self.pushButton_15.setIcon(icon17)
                self.pushButton_15.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_15.setObjectName("pushButton_15")
                self.horizontalLayout_18.addWidget(self.pushButton_15)
                self.NotificationIconOnPermanencyReport = QtWidgets.QPushButton(
                self.UserButtonOnPermanencyReport)
                self.NotificationIconOnPermanencyReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnPermanencyReport.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnPermanencyReport.setText("")
                self.NotificationIconOnPermanencyReport.setIcon(icon18)
                self.NotificationIconOnPermanencyReport.setIconSize(
                QtCore.QSize(30, 30))
                self.NotificationIconOnPermanencyReport.setObjectName(
                "NotificationIconOnPermanencyReport")
                self.horizontalLayout_18.addWidget(
                self.NotificationIconOnPermanencyReport)
                self.UserIconOnPermanencyReport = QtWidgets.QPushButton(
                self.UserButtonOnPermanencyReport)
                self.UserIconOnPermanencyReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnPermanencyReport.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnPermanencyReport.setText("")
                self.UserIconOnPermanencyReport.setIcon(icon11)
                self.UserIconOnPermanencyReport.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnPermanencyReport.setObjectName(
                "UserIconOnPermanencyReport")
                self.horizontalLayout_18.addWidget(self.UserIconOnPermanencyReport)
                self.horizontalLayout_19.addWidget(
                self.UserButtonOnPermanencyReport, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_6.addWidget(self.UpperPartOnPermanencyReport)
                self.widget_37 = QtWidgets.QWidget(self.PermanencyReport)
                self.widget_37.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_37.setObjectName("widget_37")
                self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.widget_37)
                self.verticalLayout_68.setObjectName("verticalLayout_68")
                self.label_84 = QtWidgets.QLabel(self.widget_37)
                self.label_84.setMaximumSize(QtCore.QSize(16777215, 0))
                self.label_84.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.label_84.setObjectName("label_84")
                self.verticalLayout_68.addWidget(self.label_84)
                self.verticalLayout_6.addWidget(self.widget_37)
                self.frameforUserMenu_5 = QtWidgets.QWidget(self.PermanencyReport)
                self.frameforUserMenu_5.setObjectName("frameforUserMenu_5")
                self.horizontalLayout_95 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_5)
                self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_95.setSpacing(0)
                self.horizontalLayout_95.setObjectName("horizontalLayout_95")
                self.UserMenuOnPermanencyReport = QtWidgets.QWidget(
                self.frameforUserMenu_5)
                self.UserMenuOnPermanencyReport.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnPermanencyReport.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnPermanencyReport.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnPermanencyReport.setObjectName(
                "UserMenuOnPermanencyReport")
                self.verticalLayout_47 = QtWidgets.QVBoxLayout(
                self.UserMenuOnPermanencyReport)
                self.verticalLayout_47.setObjectName("verticalLayout_47")
                self.label_138 = QtWidgets.QLabel(self.UserMenuOnPermanencyReport)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_138.setFont(font)
                self.label_138.setStyleSheet("color: #2596be;")
                self.label_138.setObjectName("label_138")
                self.verticalLayout_47.addWidget(
                self.label_138, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_60 = QtWidgets.QPushButton(
                self.UserMenuOnPermanencyReport)
                self.pushButton_60.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_60.setText("")
                self.pushButton_60.setIcon(icon19)
                self.pushButton_60.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_60.setObjectName("pushButton_60")
                self.verticalLayout_47.addWidget(
                self.pushButton_60, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_61 = QtWidgets.QPushButton(
                self.UserMenuOnPermanencyReport)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_61.setFont(font)
                self.pushButton_61.setIcon(icon11)
                self.pushButton_61.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_61.setObjectName("pushButton_61")
                self.verticalLayout_47.addWidget(
                self.pushButton_61, 0, QtCore.Qt.AlignLeft)
                self.pushButton_62 = QtWidgets.QPushButton(
                self.UserMenuOnPermanencyReport)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_62.setFont(font)
                self.pushButton_62.setIcon(icon20)
                self.pushButton_62.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_62.setObjectName("pushButton_62")
                self.verticalLayout_47.addWidget(
                self.pushButton_62, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_95.addWidget(self.UserMenuOnPermanencyReport)
                self.verticalLayout_6.addWidget(
                self.frameforUserMenu_5, 0, QtCore.Qt.AlignRight)
                self.ContentOnPermanencyReport = QtWidgets.QTableWidget(
                self.PermanencyReport)
                self.ContentOnPermanencyReport.setObjectName(
                "ContentOnPermanencyReport")
                self.ContentOnPermanencyReport.setColumnCount(3)
                self.ContentOnPermanencyReport.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnPermanencyReport.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnPermanencyReport.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnPermanencyReport.setHorizontalHeaderItem(2, item)
                self.ContentOnPermanencyReport.horizontalHeader().setCascadingSectionResizes(True)
                self.ContentOnPermanencyReport.horizontalHeader().setDefaultSectionSize(150)
                self.ContentOnPermanencyReport.horizontalHeader().setStretchLastSection(True)
                self.ContentOnPermanencyReport.verticalHeader().setCascadingSectionResizes(True)
                self.ContentOnPermanencyReport.verticalHeader().setSortIndicatorShown(True)
                self.ContentOnPermanencyReport.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_6.addWidget(self.ContentOnPermanencyReport)
                self.RightForm.addWidget(self.PermanencyReport)
                self.TaskAvailable = QtWidgets.QWidget()
                self.TaskAvailable.setObjectName("TaskAvailable")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.TaskAvailable)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.UpperPartOnTaskAvailable = QtWidgets.QWidget(self.TaskAvailable)
                self.UpperPartOnTaskAvailable.setStyleSheet("background-color: white;")
                self.UpperPartOnTaskAvailable.setObjectName("UpperPartOnTaskAvailable")
                self.horizontalLayout_24 = QtWidgets.QHBoxLayout(
                self.UpperPartOnTaskAvailable)
                self.horizontalLayout_24.setObjectName("horizontalLayout_24")
                self.MenuButtonMiscOnTaskAvailable = QtWidgets.QWidget(
                self.UpperPartOnTaskAvailable)
                self.MenuButtonMiscOnTaskAvailable.setObjectName(
                "MenuButtonMiscOnTaskAvailable")
                self.horizontalLayout_25 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnTaskAvailable)
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                self.MenuButtonOnTaskAvailable = QtWidgets.QPushButton(
                self.MenuButtonMiscOnTaskAvailable)
                self.MenuButtonOnTaskAvailable.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnTaskAvailable.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}\n"
                                                        "")
                self.MenuButtonOnTaskAvailable.setText("")
                self.MenuButtonOnTaskAvailable.setIcon(icon16)
                self.MenuButtonOnTaskAvailable.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnTaskAvailable.setFlat(True)
                self.MenuButtonOnTaskAvailable.setObjectName(
                "MenuButtonOnTaskAvailable")
                self.horizontalLayout_25.addWidget(self.MenuButtonOnTaskAvailable)
                self.LabelforMenuOnTaskAvailable = QtWidgets.QLabel(
                self.MenuButtonMiscOnTaskAvailable)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnTaskAvailable.setFont(font)
                self.LabelforMenuOnTaskAvailable.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnTaskAvailable.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnTaskAvailable.setObjectName(
                "LabelforMenuOnTaskAvailable")
                self.horizontalLayout_25.addWidget(self.LabelforMenuOnTaskAvailable)
                self.horizontalLayout_24.addWidget(
                self.MenuButtonMiscOnTaskAvailable, 0, QtCore.Qt.AlignLeft)
                self.SearchBarOnTaskAvailable = QtWidgets.QWidget(
                self.UpperPartOnTaskAvailable)
                self.SearchBarOnTaskAvailable.setObjectName("SearchBarOnTaskAvailable")
                self.horizontalLayout_26 = QtWidgets.QHBoxLayout(
                self.SearchBarOnTaskAvailable)
                self.horizontalLayout_26.setObjectName("horizontalLayout_26")
                self.BlockforSearchOnTaskAvailable = QtWidgets.QFrame(
                self.SearchBarOnTaskAvailable)
                self.BlockforSearchOnTaskAvailable.setStyleSheet("#BlockforSearchOnTaskAvailable{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnTaskAvailable.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnTaskAvailable.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnTaskAvailable.setObjectName(
                "BlockforSearchOnTaskAvailable")
                self.horizontalLayout_27 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnTaskAvailable)
                self.horizontalLayout_27.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_27.setSpacing(0)
                self.horizontalLayout_27.setObjectName("horizontalLayout_27")
                self.SearchIconOnTaskAvailable = QtWidgets.QLabel(
                self.BlockforSearchOnTaskAvailable)
                self.SearchIconOnTaskAvailable.setText("")
                self.SearchIconOnTaskAvailable.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnTaskAvailable.setObjectName(
                "SearchIconOnTaskAvailable")
                self.horizontalLayout_27.addWidget(self.SearchIconOnTaskAvailable)
                self.FeildForSearchOnTaskAvailable = QtWidgets.QLineEdit(
                self.BlockforSearchOnTaskAvailable)
                self.FeildForSearchOnTaskAvailable.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnTaskAvailable.setObjectName(
                "FeildForSearchOnTaskAvailable")
                self.horizontalLayout_27.addWidget(self.FeildForSearchOnTaskAvailable)
                self.horizontalLayout_26.addWidget(
                self.BlockforSearchOnTaskAvailable, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_24.addWidget(
                self.SearchBarOnTaskAvailable, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonOnTaskAvailable = QtWidgets.QWidget(
                self.UpperPartOnTaskAvailable)
                self.UserButtonOnTaskAvailable.setObjectName(
                "UserButtonOnTaskAvailable")
                self.horizontalLayout_23 = QtWidgets.QHBoxLayout(
                self.UserButtonOnTaskAvailable)
                self.horizontalLayout_23.setObjectName("horizontalLayout_23")
                self.pushButton_16 = QtWidgets.QPushButton(
                self.UserButtonOnTaskAvailable)
                self.pushButton_16.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_16.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_16.setText("")
                self.pushButton_16.setIcon(icon17)
                self.pushButton_16.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_16.setObjectName("pushButton_16")
                self.horizontalLayout_23.addWidget(self.pushButton_16)
                self.NotificationIconOnTaskAvailable = QtWidgets.QPushButton(
                self.UserButtonOnTaskAvailable)
                self.NotificationIconOnTaskAvailable.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnTaskAvailable.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnTaskAvailable.setText("")
                self.NotificationIconOnTaskAvailable.setIcon(icon18)
                self.NotificationIconOnTaskAvailable.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnTaskAvailable.setObjectName(
                "NotificationIconOnTaskAvailable")
                self.horizontalLayout_23.addWidget(
                self.NotificationIconOnTaskAvailable)
                self.UserIconOnTaskAvailable = QtWidgets.QPushButton(
                self.UserButtonOnTaskAvailable)
                self.UserIconOnTaskAvailable.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnTaskAvailable.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnTaskAvailable.setText("")
                self.UserIconOnTaskAvailable.setIcon(icon11)
                self.UserIconOnTaskAvailable.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnTaskAvailable.setObjectName("UserIconOnTaskAvailable")
                self.horizontalLayout_23.addWidget(self.UserIconOnTaskAvailable)
                self.horizontalLayout_24.addWidget(
                self.UserButtonOnTaskAvailable, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_7.addWidget(self.UpperPartOnTaskAvailable)
                self.widget_38 = QtWidgets.QWidget(self.TaskAvailable)
                self.widget_38.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_38.setObjectName("widget_38")
                self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.widget_38)
                self.verticalLayout_69.setObjectName("verticalLayout_69")
                self.label_85 = QtWidgets.QLabel(self.widget_38)
                self.label_85.setMaximumSize(QtCore.QSize(16777215, 0))
                self.label_85.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.label_85.setObjectName("label_85")
                self.verticalLayout_69.addWidget(self.label_85)
                self.verticalLayout_7.addWidget(self.widget_38)
                self.frameforUserMenu_6 = QtWidgets.QWidget(self.TaskAvailable)
                self.frameforUserMenu_6.setObjectName("frameforUserMenu_6")
                self.horizontalLayout_96 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_6)
                self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_96.setSpacing(0)
                self.horizontalLayout_96.setObjectName("horizontalLayout_96")
                self.UserMenuOnTaskAvailable = QtWidgets.QWidget(
                self.frameforUserMenu_6)
                self.UserMenuOnTaskAvailable.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnTaskAvailable.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnTaskAvailable.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnTaskAvailable.setObjectName("UserMenuOnTaskAvailable")
                self.verticalLayout_48 = QtWidgets.QVBoxLayout(
                self.UserMenuOnTaskAvailable)
                self.verticalLayout_48.setObjectName("verticalLayout_48")
                self.label_139 = QtWidgets.QLabel(self.UserMenuOnTaskAvailable)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_139.setFont(font)
                self.label_139.setStyleSheet("color: #2596be;")
                self.label_139.setObjectName("label_139")
                self.verticalLayout_48.addWidget(
                self.label_139, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_63 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAvailable)
                self.pushButton_63.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_63.setText("")
                self.pushButton_63.setIcon(icon19)
                self.pushButton_63.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_63.setObjectName("pushButton_63")
                self.verticalLayout_48.addWidget(self.pushButton_63)
                self.pushButton_64 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAvailable)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_64.setFont(font)
                self.pushButton_64.setIcon(icon11)
                self.pushButton_64.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_64.setObjectName("pushButton_64")
                self.verticalLayout_48.addWidget(
                self.pushButton_64, 0, QtCore.Qt.AlignLeft)
                self.pushButton_65 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAvailable)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_65.setFont(font)
                self.pushButton_65.setIcon(icon20)
                self.pushButton_65.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_65.setObjectName("pushButton_65")
                self.verticalLayout_48.addWidget(
                self.pushButton_65, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_96.addWidget(self.UserMenuOnTaskAvailable)
                self.verticalLayout_7.addWidget(
                self.frameforUserMenu_6, 0, QtCore.Qt.AlignRight)
                self.ContentOnTaskAvailable = QtWidgets.QTableWidget(
                self.TaskAvailable)
                self.ContentOnTaskAvailable.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.ContentOnTaskAvailable.setAutoScrollMargin(16)
                self.ContentOnTaskAvailable.setObjectName("ContentOnTaskAvailable")
                self.ContentOnTaskAvailable.setColumnCount(6)
                self.ContentOnTaskAvailable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAvailable.setHorizontalHeaderItem(5, item)
                self.ContentOnTaskAvailable.horizontalHeader().setCascadingSectionResizes(True)
                self.ContentOnTaskAvailable.horizontalHeader().setDefaultSectionSize(80)
                self.ContentOnTaskAvailable.horizontalHeader().setSortIndicatorShown(True)
                self.ContentOnTaskAvailable.horizontalHeader().setStretchLastSection(True)
                self.ContentOnTaskAvailable.verticalHeader().setCascadingSectionResizes(True)
                self.ContentOnTaskAvailable.verticalHeader().setMinimumSectionSize(50)
                self.ContentOnTaskAvailable.verticalHeader().setSortIndicatorShown(True)
                self.ContentOnTaskAvailable.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_7.addWidget(self.ContentOnTaskAvailable)
                self.RightForm.addWidget(self.TaskAvailable)
                self.TaskAssignedReport = QtWidgets.QWidget()
                self.TaskAssignedReport.setObjectName("TaskAssignedReport")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.TaskAssignedReport)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.UpperPartOnTaskAssignedReport = QtWidgets.QWidget(
                self.TaskAssignedReport)
                self.UpperPartOnTaskAssignedReport.setStyleSheet(
                "background-color: white;")
                self.UpperPartOnTaskAssignedReport.setObjectName(
                "UpperPartOnTaskAssignedReport")
                self.horizontalLayout_34 = QtWidgets.QHBoxLayout(
                self.UpperPartOnTaskAssignedReport)
                self.horizontalLayout_34.setObjectName("horizontalLayout_34")
                self.MenuButtonMiscOnTaskAssignedReport = QtWidgets.QWidget(
                self.UpperPartOnTaskAssignedReport)
                self.MenuButtonMiscOnTaskAssignedReport.setObjectName(
                "MenuButtonMiscOnTaskAssignedReport")
                self.horizontalLayout_35 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnTaskAssignedReport)
                self.horizontalLayout_35.setObjectName("horizontalLayout_35")
                self.MenuButtonOnTaskAssignedReport = QtWidgets.QPushButton(
                self.MenuButtonMiscOnTaskAssignedReport)
                self.MenuButtonOnTaskAssignedReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")
                self.MenuButtonOnTaskAssignedReport.setText("")
                self.MenuButtonOnTaskAssignedReport.setIcon(icon16)
                self.MenuButtonOnTaskAssignedReport.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnTaskAssignedReport.setFlat(True)
                self.MenuButtonOnTaskAssignedReport.setObjectName(
                "MenuButtonOnTaskAssignedReport")
                self.horizontalLayout_35.addWidget(self.MenuButtonOnTaskAssignedReport)
                self.LabelforMenuOnTaskAssignedReport = QtWidgets.QLabel(
                self.MenuButtonMiscOnTaskAssignedReport)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnTaskAssignedReport.setFont(font)
                self.LabelforMenuOnTaskAssignedReport.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                self.LabelforMenuOnTaskAssignedReport.setAlignment(
                QtCore.Qt.AlignCenter)
                self.LabelforMenuOnTaskAssignedReport.setObjectName(
                "LabelforMenuOnTaskAssignedReport")
                self.horizontalLayout_35.addWidget(
                self.LabelforMenuOnTaskAssignedReport)
                self.horizontalLayout_34.addWidget(
                self.MenuButtonMiscOnTaskAssignedReport, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnTaskAssignedReport = QtWidgets.QWidget(
                self.UpperPartOnTaskAssignedReport)
                self.SearchBarMiscOnTaskAssignedReport.setObjectName(
                "SearchBarMiscOnTaskAssignedReport")
                self.horizontalLayout_36 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnTaskAssignedReport)
                self.horizontalLayout_36.setObjectName("horizontalLayout_36")
                self.BlockforSearchOnTaskAssignedReport = QtWidgets.QFrame(
                self.SearchBarMiscOnTaskAssignedReport)
                self.BlockforSearchOnTaskAssignedReport.setStyleSheet("#BlockforSearchOnTaskAssignedReport{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnTaskAssignedReport.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnTaskAssignedReport.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnTaskAssignedReport.setObjectName(
                "BlockforSearchOnTaskAssignedReport")
                self.horizontalLayout_37 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnTaskAssignedReport)
                self.horizontalLayout_37.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_37.setSpacing(0)
                self.horizontalLayout_37.setObjectName("horizontalLayout_37")
                self.SearchIconOnTaskAssignedReport = QtWidgets.QLabel(
                self.BlockforSearchOnTaskAssignedReport)
                self.SearchIconOnTaskAssignedReport.setText("")
                self.SearchIconOnTaskAssignedReport.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnTaskAssignedReport.setObjectName(
                "SearchIconOnTaskAssignedReport")
                self.horizontalLayout_37.addWidget(self.SearchIconOnTaskAssignedReport)
                self.FeildForSearchOnTaskAssignedReport = QtWidgets.QLineEdit(
                self.BlockforSearchOnTaskAssignedReport)
                self.FeildForSearchOnTaskAssignedReport.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnTaskAssignedReport.setObjectName(
                "FeildForSearchOnTaskAssignedReport")
                self.horizontalLayout_37.addWidget(
                self.FeildForSearchOnTaskAssignedReport)
                self.horizontalLayout_36.addWidget(
                self.BlockforSearchOnTaskAssignedReport, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_34.addWidget(
                self.SearchBarMiscOnTaskAssignedReport, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnTaskAssignedReport = QtWidgets.QWidget(
                self.UpperPartOnTaskAssignedReport)
                self.UserButtonMiscOnTaskAssignedReport.setObjectName(
                "UserButtonMiscOnTaskAssignedReport")
                self.horizontalLayout_28 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnTaskAssignedReport)
                self.horizontalLayout_28.setObjectName("horizontalLayout_28")
                self.pushButton_19 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTaskAssignedReport)
                self.pushButton_19.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_19.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_19.setText("")
                self.pushButton_19.setIcon(icon17)
                self.pushButton_19.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_19.setObjectName("pushButton_19")
                self.horizontalLayout_28.addWidget(self.pushButton_19)
                self.NotificationIconOnTaskAssignedReport = QtWidgets.QPushButton(
                self.UserButtonMiscOnTaskAssignedReport)
                self.NotificationIconOnTaskAssignedReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                        "border-radius:5px;\n"
                                                                        "background-color: #2596be;\n"
                                                                        "padding:15px;\n"
                                                                        "\n"
                                                                        "}\n"
                                                                        "")
                self.NotificationIconOnTaskAssignedReport.setText("")
                self.NotificationIconOnTaskAssignedReport.setIcon(icon18)
                self.NotificationIconOnTaskAssignedReport.setIconSize(
                QtCore.QSize(30, 30))
                self.NotificationIconOnTaskAssignedReport.setObjectName(
                "NotificationIconOnTaskAssignedReport")
                self.horizontalLayout_28.addWidget(
                self.NotificationIconOnTaskAssignedReport)
                self.UserIconOnTaskAssignedReport = QtWidgets.QPushButton(
                self.UserButtonMiscOnTaskAssignedReport)
                self.UserIconOnTaskAssignedReport.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnTaskAssignedReport.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.UserIconOnTaskAssignedReport.setText("")
                self.UserIconOnTaskAssignedReport.setIcon(icon11)
                self.UserIconOnTaskAssignedReport.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnTaskAssignedReport.setObjectName(
                "UserIconOnTaskAssignedReport")
                self.horizontalLayout_28.addWidget(self.UserIconOnTaskAssignedReport)
                self.horizontalLayout_34.addWidget(
                self.UserButtonMiscOnTaskAssignedReport, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_10.addWidget(self.UpperPartOnTaskAssignedReport)
                self.widget_39 = QtWidgets.QWidget(self.TaskAssignedReport)
                self.widget_39.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_39.setObjectName("widget_39")
                self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.widget_39)
                self.verticalLayout_70.setObjectName("verticalLayout_70")
                self.label_86 = QtWidgets.QLabel(self.widget_39)
                self.label_86.setMaximumSize(QtCore.QSize(16777215, 0))
                self.label_86.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.label_86.setObjectName("label_86")
                self.verticalLayout_70.addWidget(self.label_86)
                self.verticalLayout_10.addWidget(self.widget_39)
                self.frameforUserMenu_8 = QtWidgets.QWidget(self.TaskAssignedReport)
                self.frameforUserMenu_8.setObjectName("frameforUserMenu_8")
                self.horizontalLayout_98 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_8)
                self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_98.setSpacing(0)
                self.horizontalLayout_98.setObjectName("horizontalLayout_98")
                self.UserMenuOnTaskAssignedReport = QtWidgets.QWidget(
                self.frameforUserMenu_8)
                self.UserMenuOnTaskAssignedReport.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnTaskAssignedReport.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnTaskAssignedReport.setStyleSheet("background-color:white;\n"
                                                                " border-radius:10px;")
                self.UserMenuOnTaskAssignedReport.setObjectName(
                "UserMenuOnTaskAssignedReport")
                self.verticalLayout_50 = QtWidgets.QVBoxLayout(
                self.UserMenuOnTaskAssignedReport)
                self.verticalLayout_50.setObjectName("verticalLayout_50")
                self.label_141 = QtWidgets.QLabel(self.UserMenuOnTaskAssignedReport)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_141.setFont(font)
                self.label_141.setStyleSheet("color: #2596be;")
                self.label_141.setObjectName("label_141")
                self.verticalLayout_50.addWidget(
                self.label_141, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_69 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAssignedReport)
                self.pushButton_69.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_69.setText("")
                self.pushButton_69.setIcon(icon19)
                self.pushButton_69.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_69.setObjectName("pushButton_69")
                self.verticalLayout_50.addWidget(self.pushButton_69)
                self.pushButton_70 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAssignedReport)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_70.setFont(font)
                self.pushButton_70.setIcon(icon11)
                self.pushButton_70.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_70.setObjectName("pushButton_70")
                self.verticalLayout_50.addWidget(
                self.pushButton_70, 0, QtCore.Qt.AlignLeft)
                self.pushButton_71 = QtWidgets.QPushButton(
                self.UserMenuOnTaskAssignedReport)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_71.setFont(font)
                self.pushButton_71.setIcon(icon20)
                self.pushButton_71.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_71.setObjectName("pushButton_71")
                self.verticalLayout_50.addWidget(
                self.pushButton_71, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_98.addWidget(self.UserMenuOnTaskAssignedReport)
                self.verticalLayout_10.addWidget(
                self.frameforUserMenu_8, 0, QtCore.Qt.AlignRight)
                self.ContentOnTaskAssignedReport = QtWidgets.QTableWidget(
                self.TaskAssignedReport)
                self.ContentOnTaskAssignedReport.setObjectName(
                "ContentOnTaskAssignedReport")
                self.ContentOnTaskAssignedReport.setColumnCount(4)
                self.ContentOnTaskAssignedReport.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAssignedReport.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAssignedReport.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAssignedReport.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.ContentOnTaskAssignedReport.setHorizontalHeaderItem(3, item)
                self.ContentOnTaskAssignedReport.horizontalHeader().setCascadingSectionResizes(True)
                self.ContentOnTaskAssignedReport.horizontalHeader().setDefaultSectionSize(130)
                self.ContentOnTaskAssignedReport.horizontalHeader().setSortIndicatorShown(True)
                self.ContentOnTaskAssignedReport.horizontalHeader().setStretchLastSection(True)
                self.ContentOnTaskAssignedReport.verticalHeader().setCascadingSectionResizes(True)
                self.ContentOnTaskAssignedReport.verticalHeader().setSortIndicatorShown(True)
                self.ContentOnTaskAssignedReport.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_10.addWidget(self.ContentOnTaskAssignedReport)
                self.RightForm.addWidget(self.TaskAssignedReport)
                self.AsiggningTask = QtWidgets.QWidget()
                self.AsiggningTask.setObjectName("AsiggningTask")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.AsiggningTask)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.UpperPartOnAsiggningTask = QtWidgets.QWidget(self.AsiggningTask)
                self.UpperPartOnAsiggningTask.setStyleSheet("background-color: white;")
                self.UpperPartOnAsiggningTask.setObjectName("UpperPartOnAsiggningTask")
                self.horizontalLayout_29 = QtWidgets.QHBoxLayout(
                self.UpperPartOnAsiggningTask)
                self.horizontalLayout_29.setObjectName("horizontalLayout_29")
                self.MenuButtonMiscOnAsiggningTask = QtWidgets.QWidget(
                self.UpperPartOnAsiggningTask)
                self.MenuButtonMiscOnAsiggningTask.setObjectName(
                "MenuButtonMiscOnAsiggningTask")
                self.horizontalLayout_30 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnAsiggningTask)
                self.horizontalLayout_30.setObjectName("horizontalLayout_30")
                self.MenuButtonOnAsiggningTask = QtWidgets.QPushButton(
                self.MenuButtonMiscOnAsiggningTask)
                self.MenuButtonOnAsiggningTask.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnAsiggningTask.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnAsiggningTask.setText("")
                self.MenuButtonOnAsiggningTask.setIcon(icon16)
                self.MenuButtonOnAsiggningTask.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnAsiggningTask.setFlat(True)
                self.MenuButtonOnAsiggningTask.setObjectName(
                "MenuButtonOnAsiggningTask")
                self.horizontalLayout_30.addWidget(self.MenuButtonOnAsiggningTask)
                self.LabelforMenuOnAsiggningTask = QtWidgets.QLabel(
                self.MenuButtonMiscOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnAsiggningTask.setFont(font)
                self.LabelforMenuOnAsiggningTask.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnAsiggningTask.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnAsiggningTask.setObjectName(
                "LabelforMenuOnAsiggningTask")
                self.horizontalLayout_30.addWidget(self.LabelforMenuOnAsiggningTask)
                self.horizontalLayout_29.addWidget(
                self.MenuButtonMiscOnAsiggningTask, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnAsiggningTask = QtWidgets.QWidget(
                self.UpperPartOnAsiggningTask)
                self.SearchBarMiscOnAsiggningTask.setObjectName(
                "SearchBarMiscOnAsiggningTask")
                self.horizontalLayout_31 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnAsiggningTask)
                self.horizontalLayout_31.setObjectName("horizontalLayout_31")
                self.BlockforSearchOnAsiggningTask = QtWidgets.QFrame(
                self.SearchBarMiscOnAsiggningTask)
                self.BlockforSearchOnAsiggningTask.setStyleSheet("#BlockforSearchOnAsiggningTask{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnAsiggningTask.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnAsiggningTask.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnAsiggningTask.setObjectName(
                "BlockforSearchOnAsiggningTask")
                self.horizontalLayout_32 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnAsiggningTask)
                self.horizontalLayout_32.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_32.setSpacing(0)
                self.horizontalLayout_32.setObjectName("horizontalLayout_32")
                self.SearchIconOnAsiggningTask = QtWidgets.QLabel(
                self.BlockforSearchOnAsiggningTask)
                self.SearchIconOnAsiggningTask.setText("")
                self.SearchIconOnAsiggningTask.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnAsiggningTask.setObjectName(
                "SearchIconOnAsiggningTask")
                self.horizontalLayout_32.addWidget(self.SearchIconOnAsiggningTask)
                self.FeildForSearchOnAsiggningTask = QtWidgets.QLineEdit(
                self.BlockforSearchOnAsiggningTask)
                self.FeildForSearchOnAsiggningTask.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnAsiggningTask.setObjectName(
                "FeildForSearchOnAsiggningTask")
                self.horizontalLayout_32.addWidget(self.FeildForSearchOnAsiggningTask)
                self.horizontalLayout_31.addWidget(
                self.BlockforSearchOnAsiggningTask, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_29.addWidget(
                self.SearchBarMiscOnAsiggningTask, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnAsiggningTask = QtWidgets.QWidget(
                self.UpperPartOnAsiggningTask)
                self.UserButtonMiscOnAsiggningTask.setObjectName(
                "UserButtonMiscOnAsiggningTask")
                self.horizontalLayout_33 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnAsiggningTask)
                self.horizontalLayout_33.setObjectName("horizontalLayout_33")
                self.pushButton_20 = QtWidgets.QPushButton(
                self.UserButtonMiscOnAsiggningTask)
                self.pushButton_20.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_20.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_20.setText("")
                self.pushButton_20.setIcon(icon17)
                self.pushButton_20.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_20.setObjectName("pushButton_20")
                self.horizontalLayout_33.addWidget(self.pushButton_20)
                self.pushButtonOnAsiggningTask = QtWidgets.QPushButton(
                self.UserButtonMiscOnAsiggningTask)
                self.pushButtonOnAsiggningTask.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButtonOnAsiggningTask.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.pushButtonOnAsiggningTask.setText("")
                self.pushButtonOnAsiggningTask.setIcon(icon18)
                self.pushButtonOnAsiggningTask.setIconSize(QtCore.QSize(30, 30))
                self.pushButtonOnAsiggningTask.setObjectName(
                "pushButtonOnAsiggningTask")
                self.horizontalLayout_33.addWidget(self.pushButtonOnAsiggningTask)
                self.UserIconOnAsiggningTask = QtWidgets.QPushButton(
                self.UserButtonMiscOnAsiggningTask)
                self.UserIconOnAsiggningTask.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnAsiggningTask.setStyleSheet("border-radius : 5px;\n"
                                                        "background-color: white;\n"
                                                        "color: #2596be;")
                self.UserIconOnAsiggningTask.setText("")
                self.UserIconOnAsiggningTask.setIcon(icon11)
                self.UserIconOnAsiggningTask.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnAsiggningTask.setObjectName("UserIconOnAsiggningTask")
                self.horizontalLayout_33.addWidget(self.UserIconOnAsiggningTask)
                self.horizontalLayout_29.addWidget(
                self.UserButtonMiscOnAsiggningTask, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_8.addWidget(self.UpperPartOnAsiggningTask)
                self.widget_40 = QtWidgets.QWidget(self.AsiggningTask)
                self.widget_40.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_40.setObjectName("widget_40")
                self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.widget_40)
                self.verticalLayout_71.setObjectName("verticalLayout_71")
                self.MessageOnAssigningTask = QtWidgets.QLabel(self.widget_40)
                self.MessageOnAssigningTask.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnAssigningTask.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnAssigningTask.setObjectName("MessageOnAssigningTask")
                self.verticalLayout_71.addWidget(self.MessageOnAssigningTask)
                self.verticalLayout_8.addWidget(self.widget_40)
                self.frameforUserMenu_7 = QtWidgets.QWidget(self.AsiggningTask)
                self.frameforUserMenu_7.setObjectName("frameforUserMenu_7")
                self.horizontalLayout_97 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_7)
                self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_97.setSpacing(0)
                self.horizontalLayout_97.setObjectName("horizontalLayout_97")
                self.UserMenuOnAsiggningTask = QtWidgets.QWidget(
                self.frameforUserMenu_7)
                self.UserMenuOnAsiggningTask.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnAsiggningTask.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnAsiggningTask.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnAsiggningTask.setObjectName("UserMenuOnAsiggningTask")
                self.verticalLayout_49 = QtWidgets.QVBoxLayout(
                self.UserMenuOnAsiggningTask)
                self.verticalLayout_49.setObjectName("verticalLayout_49")
                self.label_140 = QtWidgets.QLabel(self.UserMenuOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_140.setFont(font)
                self.label_140.setStyleSheet("color: #2596be;")
                self.label_140.setObjectName("label_140")
                self.verticalLayout_49.addWidget(
                self.label_140, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_66 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask)
                self.pushButton_66.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_66.setText("")
                self.pushButton_66.setIcon(icon19)
                self.pushButton_66.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_66.setObjectName("pushButton_66")
                self.verticalLayout_49.addWidget(self.pushButton_66)
                self.pushButton_67 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_67.setFont(font)
                self.pushButton_67.setIcon(icon11)
                self.pushButton_67.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_67.setObjectName("pushButton_67")
                self.verticalLayout_49.addWidget(
                self.pushButton_67, 0, QtCore.Qt.AlignLeft)
                self.pushButton_68 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_68.setFont(font)
                self.pushButton_68.setIcon(icon20)
                self.pushButton_68.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_68.setObjectName("pushButton_68")
                self.verticalLayout_49.addWidget(
                self.pushButton_68, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_97.addWidget(self.UserMenuOnAsiggningTask)
                self.verticalLayout_8.addWidget(
                self.frameforUserMenu_7, 0, QtCore.Qt.AlignRight)
                self.ContentOnAsiggningTask = QtWidgets.QWidget(self.AsiggningTask)
                self.ContentOnAsiggningTask.setObjectName("ContentOnAsiggningTask")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(
                self.ContentOnAsiggningTask)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                spacerItem5 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_9.addItem(spacerItem5)
                self.label_11 = QtWidgets.QLabel(self.ContentOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setAlignment(QtCore.Qt.AlignCenter)
                self.label_11.setObjectName("label_11")
                self.verticalLayout_9.addWidget(
                self.label_11, 0, QtCore.Qt.AlignHCenter)
                self.lineEdit_14 = QtWidgets.QLineEdit(self.ContentOnAsiggningTask)
                self.lineEdit_14.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.lineEdit_14.setObjectName("lineEdit_14")
                self.verticalLayout_9.addWidget(self.lineEdit_14)
                self.label_12 = QtWidgets.QLabel(self.ContentOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.label_12.setFont(font)
                self.label_12.setAlignment(QtCore.Qt.AlignCenter)
                self.label_12.setObjectName("label_12")
                self.verticalLayout_9.addWidget(
                self.label_12, 0, QtCore.Qt.AlignHCenter)
                self.comboBox_2 = QtWidgets.QComboBox(self.ContentOnAsiggningTask)
                self.comboBox_2.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_2.setObjectName("comboBox_2")
                self.comboBox_2.addItem("")
                self.verticalLayout_9.addWidget(self.comboBox_2)
                self.label_13 = QtWidgets.QLabel(self.ContentOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.label_13.setFont(font)
                self.label_13.setAlignment(QtCore.Qt.AlignCenter)
                self.label_13.setObjectName("label_13")
                self.verticalLayout_9.addWidget(
                self.label_13, 0, QtCore.Qt.AlignHCenter)
                self.dateTimeEdit = QtWidgets.QDateTimeEdit(
                self.ContentOnAsiggningTask)
                self.dateTimeEdit.setStyleSheet("border: 2px solid grey; \n"
                                                " border-radius:5px;\n"
                                                " padding:5px")
                self.dateTimeEdit.setObjectName("dateTimeEdit")
                self.verticalLayout_9.addWidget(self.dateTimeEdit)
                self.label = QtWidgets.QLabel(self.ContentOnAsiggningTask)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.verticalLayout_9.addWidget(self.label)
                self.lineEdit_17 = QtWidgets.QLineEdit(self.ContentOnAsiggningTask)
                self.lineEdit_17.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.lineEdit_17.setObjectName("lineEdit_17")
                self.verticalLayout_9.addWidget(self.lineEdit_17)
                spacerItem6 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_9.addItem(spacerItem6)
                self.widget_4 = QtWidgets.QWidget(self.ContentOnAsiggningTask)
                self.widget_4.setObjectName("widget_4")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
                self.pushButton_7.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                self.pushButton_7.setObjectName("pushButton_7")
                self.horizontalLayout_3.addWidget(self.pushButton_7)
                self.pushButton = QtWidgets.QPushButton(self.widget_4)
                self.pushButton.setStyleSheet("background-color: pink;\n"
                                        "padding: 10px;\n"
                                        "color: white;\n"
                                        "")
                self.pushButton.setObjectName("pushButton")
                self.horizontalLayout_3.addWidget(self.pushButton)
                self.verticalLayout_9.addWidget(
                self.widget_4, 0, QtCore.Qt.AlignHCenter)
                spacerItem7 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_9.addItem(spacerItem7)
                self.verticalLayout_8.addWidget(self.ContentOnAsiggningTask)
                self.RightForm.addWidget(self.AsiggningTask)
                self.RecievedTaskPage = QtWidgets.QWidget()
                self.RecievedTaskPage.setObjectName("RecievedTaskPage")
                self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.RecievedTaskPage)
                self.verticalLayout_28.setObjectName("verticalLayout_28")
                self.UpperPartDashboard_4 = QtWidgets.QWidget(self.RecievedTaskPage)
                self.UpperPartDashboard_4.setObjectName("UpperPartDashboard_4")
                self.horizontalLayout_53 = QtWidgets.QHBoxLayout(
                self.UpperPartDashboard_4)
                self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_53.setSpacing(0)
                self.horizontalLayout_53.setObjectName("horizontalLayout_53")
                self.MenuMiscContainerDashboard_4 = QtWidgets.QWidget(
                self.UpperPartDashboard_4)
                self.MenuMiscContainerDashboard_4.setObjectName(
                "MenuMiscContainerDashboard_4")
                self.horizontalLayout_62 = QtWidgets.QHBoxLayout(
                self.MenuMiscContainerDashboard_4)
                self.horizontalLayout_62.setObjectName("horizontalLayout_62")
                self.MenuButtonOnDashboard_4 = QtWidgets.QPushButton(
                self.MenuMiscContainerDashboard_4)
                self.MenuButtonOnDashboard_4.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnDashboard_4.setText("")
                self.MenuButtonOnDashboard_4.setIcon(icon16)
                self.MenuButtonOnDashboard_4.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnDashboard_4.setFlat(True)
                self.MenuButtonOnDashboard_4.setObjectName("MenuButtonOnDashboard_4")
                self.horizontalLayout_62.addWidget(self.MenuButtonOnDashboard_4)
                self.PageNameOnDashboard_4 = QtWidgets.QLabel(
                self.MenuMiscContainerDashboard_4)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.PageNameOnDashboard_4.setFont(font)
                self.PageNameOnDashboard_4.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.PageNameOnDashboard_4.setAlignment(QtCore.Qt.AlignCenter)
                self.PageNameOnDashboard_4.setObjectName("PageNameOnDashboard_4")
                self.horizontalLayout_62.addWidget(self.PageNameOnDashboard_4)
                self.horizontalLayout_53.addWidget(
                self.MenuMiscContainerDashboard_4, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.SearchMiscContainerDashboard_4 = QtWidgets.QWidget(
                self.UpperPartDashboard_4)
                self.SearchMiscContainerDashboard_4.setObjectName(
                "SearchMiscContainerDashboard_4")
                self.horizontalLayout_63 = QtWidgets.QHBoxLayout(
                self.SearchMiscContainerDashboard_4)
                self.horizontalLayout_63.setObjectName("horizontalLayout_63")
                self.BlockforSearch_4 = QtWidgets.QFrame(
                self.SearchMiscContainerDashboard_4)
                self.BlockforSearch_4.setStyleSheet("")
                self.BlockforSearch_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BlockforSearch_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearch_4.setObjectName("BlockforSearch_4")
                self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.BlockforSearch_4)
                self.horizontalLayout_64.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_64.setSpacing(0)
                self.horizontalLayout_64.setObjectName("horizontalLayout_64")
                self.SearchIcon_4 = QtWidgets.QLabel(self.BlockforSearch_4)
                self.SearchIcon_4.setText("")
                self.SearchIcon_4.setPixmap(QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIcon_4.setObjectName("SearchIcon_4")
                self.horizontalLayout_64.addWidget(
                self.SearchIcon_4, 0, QtCore.Qt.AlignRight)
                self.FeildForSearch_4 = QtWidgets.QLineEdit(self.BlockforSearch_4)
                self.FeildForSearch_4.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                self.FeildForSearch_4.setObjectName("FeildForSearch_4")
                self.horizontalLayout_64.addWidget(
                self.FeildForSearch_4, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_63.addWidget(
                self.BlockforSearch_4, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_53.addWidget(self.SearchMiscContainerDashboard_4)
                self.RightIconMiscContainer_4 = QtWidgets.QWidget(
                self.UpperPartDashboard_4)
                self.RightIconMiscContainer_4.setObjectName("RightIconMiscContainer_4")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(
                self.RightIconMiscContainer_4)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.pushButton_29 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_4)
                self.pushButton_29.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_29.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_29.setText("")
                self.pushButton_29.setIcon(icon17)
                self.pushButton_29.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_29.setObjectName("pushButton_29")
                self.horizontalLayout_6.addWidget(self.pushButton_29)
                self.NotificationIconDashboard_4 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_4)
                self.NotificationIconDashboard_4.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconDashboard_4.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconDashboard_4.setText("")
                self.NotificationIconDashboard_4.setIcon(icon18)
                self.NotificationIconDashboard_4.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconDashboard_4.setObjectName(
                "NotificationIconDashboard_4")
                self.horizontalLayout_6.addWidget(self.NotificationIconDashboard_4)
                self.UserIconDashboard_4 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_4)
                self.UserIconDashboard_4.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconDashboard_4.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                self.UserIconDashboard_4.setText("")
                self.UserIconDashboard_4.setIcon(icon11)
                self.UserIconDashboard_4.setIconSize(QtCore.QSize(32, 32))
                self.UserIconDashboard_4.setObjectName("UserIconDashboard_4")
                self.horizontalLayout_6.addWidget(self.UserIconDashboard_4)
                self.horizontalLayout_53.addWidget(
                self.RightIconMiscContainer_4, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_28.addWidget(self.UpperPartDashboard_4)
                self.widget_41 = QtWidgets.QWidget(self.RecievedTaskPage)
                self.widget_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_41.setObjectName("widget_41")
                self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.widget_41)
                self.verticalLayout_72.setObjectName("verticalLayout_72")
                self.MessageOnRecievedTask = QtWidgets.QLabel(self.widget_41)
                self.MessageOnRecievedTask.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnRecievedTask.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnRecievedTask.setObjectName("MessageOnRecievedTask")
                self.verticalLayout_72.addWidget(self.MessageOnRecievedTask)
                self.verticalLayout_28.addWidget(self.widget_41)
                self.widget_19 = QtWidgets.QWidget(self.RecievedTaskPage)
                self.widget_19.setObjectName("widget_19")
                self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.widget_19)
                self.verticalLayout_29.setObjectName("verticalLayout_29")
                self.frameforUserMenu_11 = QtWidgets.QWidget(self.widget_19)
                self.frameforUserMenu_11.setObjectName("frameforUserMenu_11")
                self.horizontalLayout_101 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_11)
                self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_101.setSpacing(0)
                self.horizontalLayout_101.setObjectName("horizontalLayout_101")
                self.UserMenuOnAsiggningTask_2 = QtWidgets.QWidget(
                self.frameforUserMenu_11)
                self.UserMenuOnAsiggningTask_2.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnAsiggningTask_2.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnAsiggningTask_2.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnAsiggningTask_2.setObjectName(
                "UserMenuOnAsiggningTask_2")
                self.verticalLayout_53 = QtWidgets.QVBoxLayout(
                self.UserMenuOnAsiggningTask_2)
                self.verticalLayout_53.setObjectName("verticalLayout_53")
                self.label_144 = QtWidgets.QLabel(self.UserMenuOnAsiggningTask_2)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_144.setFont(font)
                self.label_144.setStyleSheet("color: #2596be;")
                self.label_144.setObjectName("label_144")
                self.verticalLayout_53.addWidget(
                self.label_144, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_78 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask_2)
                self.pushButton_78.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_78.setText("")
                self.pushButton_78.setIcon(icon19)
                self.pushButton_78.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_78.setObjectName("pushButton_78")
                self.verticalLayout_53.addWidget(self.pushButton_78)
                self.pushButton_79 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_79.setFont(font)
                self.pushButton_79.setIcon(icon11)
                self.pushButton_79.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_79.setObjectName("pushButton_79")
                self.verticalLayout_53.addWidget(
                self.pushButton_79, 0, QtCore.Qt.AlignLeft)
                self.pushButton_80 = QtWidgets.QPushButton(
                self.UserMenuOnAsiggningTask_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_80.setFont(font)
                self.pushButton_80.setIcon(icon20)
                self.pushButton_80.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_80.setObjectName("pushButton_80")
                self.verticalLayout_53.addWidget(
                self.pushButton_80, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_101.addWidget(self.UserMenuOnAsiggningTask_2)
                self.verticalLayout_29.addWidget(
                self.frameforUserMenu_11, 0, QtCore.Qt.AlignRight)
                self.tableWidget_3 = QtWidgets.QTableWidget(self.widget_19)
                self.tableWidget_3.setObjectName("tableWidget_3")
                self.tableWidget_3.setColumnCount(5)
                self.tableWidget_3.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setHorizontalHeaderItem(4, item)
                self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)
                self.tableWidget_3.horizontalHeader().setMinimumSectionSize(50)
                self.tableWidget_3.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
                self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
                self.tableWidget_3.verticalHeader().setMinimumSectionSize(50)
                self.tableWidget_3.verticalHeader().setSortIndicatorShown(True)
                self.tableWidget_3.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_29.addWidget(self.tableWidget_3)
                self.widget_20 = QtWidgets.QWidget(self.widget_19)
                self.widget_20.setObjectName("widget_20")
                self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.widget_20)
                self.verticalLayout_33.setObjectName("verticalLayout_33")
                self.label_72 = QtWidgets.QLabel(self.widget_20)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_72.setFont(font)
                self.label_72.setAlignment(QtCore.Qt.AlignCenter)
                self.label_72.setObjectName("label_72")
                self.verticalLayout_33.addWidget(self.label_72)
                self.label_17 = QtWidgets.QLabel(self.widget_20)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_17.setFont(font)
                self.label_17.setObjectName("label_17")
                self.verticalLayout_33.addWidget(self.label_17)
                self.label_18 = QtWidgets.QLabel(self.widget_20)
                self.label_18.setObjectName("label_18")
                self.verticalLayout_33.addWidget(self.label_18)
                self.label_70 = QtWidgets.QLabel(self.widget_20)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_70.setFont(font)
                self.label_70.setObjectName("label_70")
                self.verticalLayout_33.addWidget(self.label_70)
                self.label_68 = QtWidgets.QLabel(self.widget_20)
                self.label_68.setObjectName("label_68")
                self.verticalLayout_33.addWidget(self.label_68)
                self.widget_22 = QtWidgets.QWidget(self.widget_20)
                self.widget_22.setObjectName("widget_22")
                self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.widget_22)
                self.verticalLayout_32.setObjectName("verticalLayout_32")
                self.label_71 = QtWidgets.QLabel(self.widget_22)
                self.label_71.setObjectName("label_71")
                self.verticalLayout_32.addWidget(self.label_71)
                self.pushButton_11 = QtWidgets.QPushButton(self.widget_22)
                self.pushButton_11.setStyleSheet("#pushButton_11{\n"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                " }\n"
                                                "#pushButton_11:hover {background-color: lightblue; \\n padding: 10px; }")
                self.pushButton_11.setObjectName("pushButton_11")
                self.verticalLayout_32.addWidget(self.pushButton_11)
                self.verticalLayout_33.addWidget(self.widget_22)
                self.verticalLayout_29.addWidget(self.widget_20)
                self.widget_21 = QtWidgets.QWidget(self.widget_19)
                self.widget_21.setObjectName("widget_21")
                self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.widget_21)
                self.verticalLayout_30.setObjectName("verticalLayout_30")
                self.label_69 = QtWidgets.QLabel(self.widget_21)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_69.setFont(font)
                self.label_69.setAlignment(QtCore.Qt.AlignCenter)
                self.label_69.setObjectName("label_69")
                self.verticalLayout_30.addWidget(self.label_69)
                self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_21)
                self.doubleSpinBox.setStyleSheet("border: 2px solid grey; \n"
                                                " border-radius:5px;\n"
                                                " padding:5px")
                self.doubleSpinBox.setObjectName("doubleSpinBox")
                self.verticalLayout_30.addWidget(self.doubleSpinBox)
                self.pushButton_30 = QtWidgets.QPushButton(self.widget_21)
                self.pushButton_30.setStyleSheet("#pushButton_30{\n"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                " }\n"
                                                "#pushButton_30:hover {background-color: lightblue; \\n padding: 10px; }")
                self.pushButton_30.setObjectName("pushButton_30")
                self.verticalLayout_30.addWidget(self.pushButton_30)
                self.verticalLayout_29.addWidget(self.widget_21)
                self.verticalLayout_28.addWidget(self.widget_19)
                self.RightForm.addWidget(self.RecievedTaskPage)
                self.UpdateWork = QtWidgets.QWidget()
                self.UpdateWork.setObjectName("UpdateWork")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.UpdateWork)
                self.verticalLayout_11.setObjectName("verticalLayout_11")
                self.UpperPartOnUpdateWork = QtWidgets.QWidget(self.UpdateWork)
                self.UpperPartOnUpdateWork.setStyleSheet("background-color: white;")
                self.UpperPartOnUpdateWork.setObjectName("UpperPartOnUpdateWork")
                self.horizontalLayout_39 = QtWidgets.QHBoxLayout(
                self.UpperPartOnUpdateWork)
                self.horizontalLayout_39.setObjectName("horizontalLayout_39")
                self.MenuButtonMiscOnUpdateWork = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork)
                self.MenuButtonMiscOnUpdateWork.setObjectName(
                "MenuButtonMiscOnUpdateWork")
                self.horizontalLayout_40 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnUpdateWork)
                self.horizontalLayout_40.setObjectName("horizontalLayout_40")
                self.MenuButtonOnUpdateWork = QtWidgets.QPushButton(
                self.MenuButtonMiscOnUpdateWork)
                self.MenuButtonOnUpdateWork.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnUpdateWork.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnUpdateWork.setText("")
                self.MenuButtonOnUpdateWork.setIcon(icon16)
                self.MenuButtonOnUpdateWork.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnUpdateWork.setFlat(True)
                self.MenuButtonOnUpdateWork.setObjectName("MenuButtonOnUpdateWork")
                self.horizontalLayout_40.addWidget(self.MenuButtonOnUpdateWork)
                self.LabelforMenuOnUpdateWork = QtWidgets.QLabel(
                self.MenuButtonMiscOnUpdateWork)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnUpdateWork.setFont(font)
                self.LabelforMenuOnUpdateWork.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnUpdateWork.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnUpdateWork.setObjectName("LabelforMenuOnUpdateWork")
                self.horizontalLayout_40.addWidget(self.LabelforMenuOnUpdateWork)
                self.horizontalLayout_39.addWidget(
                self.MenuButtonMiscOnUpdateWork, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnUpdateWork = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork)
                self.SearchBarMiscOnUpdateWork.setObjectName(
                "SearchBarMiscOnUpdateWork")
                self.horizontalLayout_41 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnUpdateWork)
                self.horizontalLayout_41.setObjectName("horizontalLayout_41")
                self.BlockforSearchOnUpdateWork = QtWidgets.QFrame(
                self.SearchBarMiscOnUpdateWork)
                self.BlockforSearchOnUpdateWork.setStyleSheet("#BlockforSearchOnUpdateWork{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                self.BlockforSearchOnUpdateWork.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnUpdateWork.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearchOnUpdateWork.setObjectName(
                "BlockforSearchOnUpdateWork")
                self.horizontalLayout_42 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnUpdateWork)
                self.horizontalLayout_42.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_42.setSpacing(0)
                self.horizontalLayout_42.setObjectName("horizontalLayout_42")
                self.SearchIconOnUpdateWork = QtWidgets.QLabel(
                self.BlockforSearchOnUpdateWork)
                self.SearchIconOnUpdateWork.setText("")
                self.SearchIconOnUpdateWork.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnUpdateWork.setObjectName("SearchIconOnUpdateWork")
                self.horizontalLayout_42.addWidget(self.SearchIconOnUpdateWork)
                self.FeildForSearchOnUpdateWork = QtWidgets.QLineEdit(
                self.BlockforSearchOnUpdateWork)
                self.FeildForSearchOnUpdateWork.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                self.FeildForSearchOnUpdateWork.setObjectName(
                "FeildForSearchOnUpdateWork")
                self.horizontalLayout_42.addWidget(self.FeildForSearchOnUpdateWork)
                self.horizontalLayout_41.addWidget(
                self.BlockforSearchOnUpdateWork, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_39.addWidget(
                self.SearchBarMiscOnUpdateWork, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnUpdateWork = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork)
                self.UserButtonMiscOnUpdateWork.setObjectName(
                "UserButtonMiscOnUpdateWork")
                self.horizontalLayout_38 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnUpdateWork)
                self.horizontalLayout_38.setObjectName("horizontalLayout_38")
                self.pushButton_21 = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork)
                self.pushButton_21.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_21.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_21.setText("")
                self.pushButton_21.setIcon(icon17)
                self.pushButton_21.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_21.setObjectName("pushButton_21")
                self.horizontalLayout_38.addWidget(self.pushButton_21)
                self.NotificationIconOnUpdateWork = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork)
                self.NotificationIconOnUpdateWork.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnUpdateWork.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnUpdateWork.setText("")
                self.NotificationIconOnUpdateWork.setIcon(icon18)
                self.NotificationIconOnUpdateWork.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnUpdateWork.setObjectName(
                "NotificationIconOnUpdateWork")
                self.horizontalLayout_38.addWidget(self.NotificationIconOnUpdateWork)
                self.UserIconOnUpdateWork = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork)
                self.UserIconOnUpdateWork.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnUpdateWork.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnUpdateWork.setText("")
                self.UserIconOnUpdateWork.setIcon(icon11)
                self.UserIconOnUpdateWork.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnUpdateWork.setObjectName("UserIconOnUpdateWork")
                self.horizontalLayout_38.addWidget(self.UserIconOnUpdateWork)
                self.horizontalLayout_39.addWidget(
                self.UserButtonMiscOnUpdateWork, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_11.addWidget(self.UpperPartOnUpdateWork)
                self.widget_42 = QtWidgets.QWidget(self.UpdateWork)
                self.widget_42.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_42.setObjectName("widget_42")
                self.verticalLayout_73 = QtWidgets.QVBoxLayout(self.widget_42)
                self.verticalLayout_73.setObjectName("verticalLayout_73")
                self.MessageOnUpdateWork = QtWidgets.QLabel(self.widget_42)
                self.MessageOnUpdateWork.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnUpdateWork.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnUpdateWork.setObjectName("MessageOnUpdateWork")
                self.verticalLayout_73.addWidget(self.MessageOnUpdateWork)
                self.verticalLayout_11.addWidget(self.widget_42)
                self.frameforUserMenu_9 = QtWidgets.QWidget(self.UpdateWork)
                self.frameforUserMenu_9.setObjectName("frameforUserMenu_9")
                self.horizontalLayout_99 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_9)
                self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_99.setSpacing(0)
                self.horizontalLayout_99.setObjectName("horizontalLayout_99")
                self.UserMenuOnUpdateWork = QtWidgets.QWidget(self.frameforUserMenu_9)
                self.UserMenuOnUpdateWork.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnUpdateWork.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnUpdateWork.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnUpdateWork.setObjectName("UserMenuOnUpdateWork")
                self.verticalLayout_51 = QtWidgets.QVBoxLayout(
                self.UserMenuOnUpdateWork)
                self.verticalLayout_51.setObjectName("verticalLayout_51")
                self.label_142 = QtWidgets.QLabel(self.UserMenuOnUpdateWork)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_142.setFont(font)
                self.label_142.setStyleSheet("color: #2596be;")
                self.label_142.setObjectName("label_142")
                self.verticalLayout_51.addWidget(
                self.label_142, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_72 = QtWidgets.QPushButton(self.UserMenuOnUpdateWork)
                self.pushButton_72.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_72.setText("")
                self.pushButton_72.setIcon(icon19)
                self.pushButton_72.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_72.setObjectName("pushButton_72")
                self.verticalLayout_51.addWidget(self.pushButton_72)
                self.pushButton_73 = QtWidgets.QPushButton(self.UserMenuOnUpdateWork)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_73.setFont(font)
                self.pushButton_73.setIcon(icon11)
                self.pushButton_73.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_73.setObjectName("pushButton_73")
                self.verticalLayout_51.addWidget(
                self.pushButton_73, 0, QtCore.Qt.AlignLeft)
                self.pushButton_74 = QtWidgets.QPushButton(self.UserMenuOnUpdateWork)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_74.setFont(font)
                self.pushButton_74.setIcon(icon20)
                self.pushButton_74.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_74.setObjectName("pushButton_74")
                self.verticalLayout_51.addWidget(
                self.pushButton_74, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_99.addWidget(self.UserMenuOnUpdateWork)
                self.verticalLayout_11.addWidget(
                self.frameforUserMenu_9, 0, QtCore.Qt.AlignRight)
                self.ContentOnUpdateWork = QtWidgets.QWidget(self.UpdateWork)
                self.ContentOnUpdateWork.setObjectName("ContentOnUpdateWork")
                self.verticalLayout_12 = QtWidgets.QVBoxLayout(
                self.ContentOnUpdateWork)
                self.verticalLayout_12.setObjectName("verticalLayout_12")
                spacerItem8 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_12.addItem(spacerItem8)
                self.label_14 = QtWidgets.QLabel(self.ContentOnUpdateWork)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_14.setFont(font)
                self.label_14.setObjectName("label_14")
                self.verticalLayout_12.addWidget(self.label_14)
                self.comboBox_3 = QtWidgets.QComboBox(self.ContentOnUpdateWork)
                self.comboBox_3.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_3.setObjectName("comboBox_3")
                self.verticalLayout_12.addWidget(self.comboBox_3)
                self.label_16 = QtWidgets.QLabel(self.ContentOnUpdateWork)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_16.setFont(font)
                self.label_16.setObjectName("label_16")
                self.verticalLayout_12.addWidget(self.label_16)
                self.comboBox_4 = QtWidgets.QComboBox(self.ContentOnUpdateWork)
                self.comboBox_4.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_4.setObjectName("comboBox_4")
                self.comboBox_4.addItem("")
                self.comboBox_4.addItem("")
                self.verticalLayout_12.addWidget(self.comboBox_4)
                self.widget_23 = QtWidgets.QWidget(self.ContentOnUpdateWork)
                self.widget_23.setObjectName("widget_23")
                self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.widget_23)
                self.verticalLayout_34.setObjectName("verticalLayout_34")
                self.label_33 = QtWidgets.QLabel(self.widget_23)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_33.setFont(font)
                self.label_33.setObjectName("label_33")
                self.verticalLayout_34.addWidget(self.label_33)
                self.dateEdit = QtWidgets.QDateEdit(self.widget_23)
                self.dateEdit.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.dateEdit.setObjectName("dateEdit")
                self.verticalLayout_34.addWidget(self.dateEdit)
                self.verticalLayout_12.addWidget(self.widget_23)
                spacerItem9 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_12.addItem(spacerItem9)
                self.widget_5 = QtWidgets.QWidget(self.ContentOnUpdateWork)
                self.widget_5.setObjectName("widget_5")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.pushButton_10 = QtWidgets.QPushButton(self.widget_5)
                self.pushButton_10.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                self.pushButton_10.setObjectName("pushButton_10")
                self.horizontalLayout_4.addWidget(self.pushButton_10)
                self.verticalLayout_12.addWidget(self.widget_5)
                spacerItem10 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_12.addItem(spacerItem10)
                self.verticalLayout_11.addWidget(self.ContentOnUpdateWork)
                self.RightForm.addWidget(self.UpdateWork)
                self.page = QtWidgets.QWidget()
                self.page.setObjectName("page")
                self.verticalLayout_157 = QtWidgets.QVBoxLayout(self.page)
                self.verticalLayout_157.setObjectName("verticalLayout_157")
                self.UpperPartOnUpdateWork_3 = QtWidgets.QWidget(self.page)
                self.UpperPartOnUpdateWork_3.setStyleSheet("background-color: white;")
                self.UpperPartOnUpdateWork_3.setObjectName("UpperPartOnUpdateWork_3")
                self.horizontalLayout_195 = QtWidgets.QHBoxLayout(
                self.UpperPartOnUpdateWork_3)
                self.horizontalLayout_195.setObjectName("horizontalLayout_195")
                self.MenuButtonMiscOnUpdateWork_3 = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork_3)
                self.MenuButtonMiscOnUpdateWork_3.setObjectName(
                "MenuButtonMiscOnUpdateWork_3")
                self.horizontalLayout_196 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnUpdateWork_3)
                self.horizontalLayout_196.setObjectName("horizontalLayout_196")
                self.MenuButtonOnUpdateWork_3 = QtWidgets.QPushButton(
                self.MenuButtonMiscOnUpdateWork_3)
                self.MenuButtonOnUpdateWork_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnUpdateWork_3.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnUpdateWork_3.setText("")
                self.MenuButtonOnUpdateWork_3.setIcon(icon16)
                self.MenuButtonOnUpdateWork_3.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnUpdateWork_3.setFlat(True)
                self.MenuButtonOnUpdateWork_3.setObjectName("MenuButtonOnUpdateWork_3")
                self.horizontalLayout_196.addWidget(self.MenuButtonOnUpdateWork_3)
                self.LabelforMenuOnUpdateWork_3 = QtWidgets.QLabel(
                self.MenuButtonMiscOnUpdateWork_3)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnUpdateWork_3.setFont(font)
                self.LabelforMenuOnUpdateWork_3.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnUpdateWork_3.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnUpdateWork_3.setObjectName(
                "LabelforMenuOnUpdateWork_3")
                self.horizontalLayout_196.addWidget(self.LabelforMenuOnUpdateWork_3)
                self.horizontalLayout_195.addWidget(
                self.MenuButtonMiscOnUpdateWork_3, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnUpdateWork_3 = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork_3)
                self.SearchBarMiscOnUpdateWork_3.setObjectName(
                "SearchBarMiscOnUpdateWork_3")
                self.horizontalLayout_197 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnUpdateWork_3)
                self.horizontalLayout_197.setObjectName("horizontalLayout_197")
                self.BlockforSearchOnUpdateWork_3 = QtWidgets.QFrame(
                self.SearchBarMiscOnUpdateWork_3)
                self.BlockforSearchOnUpdateWork_3.setStyleSheet("#BlockforSearchOnUpdateWork{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnUpdateWork_3.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnUpdateWork_3.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnUpdateWork_3.setObjectName(
                "BlockforSearchOnUpdateWork_3")
                self.horizontalLayout_198 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnUpdateWork_3)
                self.horizontalLayout_198.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_198.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_198.setSpacing(0)
                self.horizontalLayout_198.setObjectName("horizontalLayout_198")
                self.SearchIconOnUpdateWork_3 = QtWidgets.QLabel(
                self.BlockforSearchOnUpdateWork_3)
                self.SearchIconOnUpdateWork_3.setText("")
                self.SearchIconOnUpdateWork_3.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnUpdateWork_3.setObjectName("SearchIconOnUpdateWork_3")
                self.horizontalLayout_198.addWidget(self.SearchIconOnUpdateWork_3)
                self.FeildForSearchOnUpdateWork_3 = QtWidgets.QLineEdit(
                self.BlockforSearchOnUpdateWork_3)
                self.FeildForSearchOnUpdateWork_3.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnUpdateWork_3.setObjectName(
                "FeildForSearchOnUpdateWork_3")
                self.horizontalLayout_198.addWidget(self.FeildForSearchOnUpdateWork_3)
                self.horizontalLayout_197.addWidget(
                self.BlockforSearchOnUpdateWork_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_195.addWidget(
                self.SearchBarMiscOnUpdateWork_3, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnUpdateWork_3 = QtWidgets.QWidget(
                self.UpperPartOnUpdateWork_3)
                self.UserButtonMiscOnUpdateWork_3.setObjectName(
                "UserButtonMiscOnUpdateWork_3")
                self.horizontalLayout_199 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnUpdateWork_3)
                self.horizontalLayout_199.setObjectName("horizontalLayout_199")
                self.pushButton_169 = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork_3)
                self.pushButton_169.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_169.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_169.setText("")
                self.pushButton_169.setIcon(icon17)
                self.pushButton_169.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_169.setObjectName("pushButton_169")
                self.horizontalLayout_199.addWidget(self.pushButton_169)
                self.NotificationIconOnUpdateWork_3 = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork_3)
                self.NotificationIconOnUpdateWork_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnUpdateWork_3.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnUpdateWork_3.setText("")
                self.NotificationIconOnUpdateWork_3.setIcon(icon18)
                self.NotificationIconOnUpdateWork_3.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnUpdateWork_3.setObjectName(
                "NotificationIconOnUpdateWork_3")
                self.horizontalLayout_199.addWidget(
                self.NotificationIconOnUpdateWork_3)
                self.UserIconOnUpdateWork_3 = QtWidgets.QPushButton(
                self.UserButtonMiscOnUpdateWork_3)
                self.UserIconOnUpdateWork_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnUpdateWork_3.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnUpdateWork_3.setText("")
                self.UserIconOnUpdateWork_3.setIcon(icon11)
                self.UserIconOnUpdateWork_3.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnUpdateWork_3.setObjectName("UserIconOnUpdateWork_3")
                self.horizontalLayout_199.addWidget(self.UserIconOnUpdateWork_3)
                self.horizontalLayout_195.addWidget(
                self.UserButtonMiscOnUpdateWork_3, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_157.addWidget(self.UpperPartOnUpdateWork_3)
                self.widget_93 = QtWidgets.QWidget(self.page)
                self.widget_93.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_93.setObjectName("widget_93")
                self.verticalLayout_153 = QtWidgets.QVBoxLayout(self.widget_93)
                self.verticalLayout_153.setObjectName("verticalLayout_153")
                self.MessageOnUpdateDesignation = QtWidgets.QLabel(self.widget_93)
                self.MessageOnUpdateDesignation.setMaximumSize(
                QtCore.QSize(16777215, 0))
                self.MessageOnUpdateDesignation.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnUpdateDesignation.setObjectName(
                "MessageOnUpdateDesignation")
                self.verticalLayout_153.addWidget(self.MessageOnUpdateDesignation)
                self.verticalLayout_157.addWidget(self.widget_93)
                self.frameforUserMenu_32 = QtWidgets.QWidget(self.page)
                self.frameforUserMenu_32.setObjectName("frameforUserMenu_32")
                self.horizontalLayout_201 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_32)
                self.horizontalLayout_201.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_201.setSpacing(0)
                self.horizontalLayout_201.setObjectName("horizontalLayout_201")
                self.UserMenuOnUpdateWork_3 = QtWidgets.QWidget(
                self.frameforUserMenu_32)
                self.UserMenuOnUpdateWork_3.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnUpdateWork_3.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnUpdateWork_3.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnUpdateWork_3.setObjectName("UserMenuOnUpdateWork_3")
                self.verticalLayout_156 = QtWidgets.QVBoxLayout(
                self.UserMenuOnUpdateWork_3)
                self.verticalLayout_156.setObjectName("verticalLayout_156")
                self.label_233 = QtWidgets.QLabel(self.UserMenuOnUpdateWork_3)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_233.setFont(font)
                self.label_233.setStyleSheet("color: #2596be;")
                self.label_233.setObjectName("label_233")
                self.verticalLayout_156.addWidget(
                self.label_233, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_171 = QtWidgets.QPushButton(
                self.UserMenuOnUpdateWork_3)
                self.pushButton_171.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_171.setText("")
                self.pushButton_171.setIcon(icon19)
                self.pushButton_171.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_171.setObjectName("pushButton_171")
                self.verticalLayout_156.addWidget(self.pushButton_171)
                self.pushButton_172 = QtWidgets.QPushButton(
                self.UserMenuOnUpdateWork_3)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_172.setFont(font)
                self.pushButton_172.setIcon(icon11)
                self.pushButton_172.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_172.setObjectName("pushButton_172")
                self.verticalLayout_156.addWidget(
                self.pushButton_172, 0, QtCore.Qt.AlignLeft)
                self.pushButton_173 = QtWidgets.QPushButton(
                self.UserMenuOnUpdateWork_3)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_173.setFont(font)
                self.pushButton_173.setIcon(icon20)
                self.pushButton_173.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_173.setObjectName("pushButton_173")
                self.verticalLayout_156.addWidget(
                self.pushButton_173, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_201.addWidget(self.UserMenuOnUpdateWork_3)
                self.verticalLayout_157.addWidget(self.frameforUserMenu_32)
                self.ContentOnUpdateWork_3 = QtWidgets.QWidget(self.page)
                self.ContentOnUpdateWork_3.setObjectName("ContentOnUpdateWork_3")
                self.verticalLayout_154 = QtWidgets.QVBoxLayout(
                self.ContentOnUpdateWork_3)
                self.verticalLayout_154.setObjectName("verticalLayout_154")
                spacerItem11 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_154.addItem(spacerItem11)
                self.label_230 = QtWidgets.QLabel(self.ContentOnUpdateWork_3)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_230.setFont(font)
                self.label_230.setObjectName("label_230")
                self.verticalLayout_154.addWidget(self.label_230)
                self.comboBox_11 = QtWidgets.QComboBox(self.ContentOnUpdateWork_3)
                self.comboBox_11.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_11.setObjectName("comboBox_11")
                self.verticalLayout_154.addWidget(self.comboBox_11)
                self.label_231 = QtWidgets.QLabel(self.ContentOnUpdateWork_3)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_231.setFont(font)
                self.label_231.setObjectName("label_231")
                self.verticalLayout_154.addWidget(self.label_231)
                self.comboBox_12 = QtWidgets.QComboBox(self.ContentOnUpdateWork_3)
                self.comboBox_12.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_12.setObjectName("comboBox_12")
                self.verticalLayout_154.addWidget(self.comboBox_12)
                self.widget_94 = QtWidgets.QWidget(self.ContentOnUpdateWork_3)
                self.widget_94.setObjectName("widget_94")
                self.verticalLayout_155 = QtWidgets.QVBoxLayout(self.widget_94)
                self.verticalLayout_155.setObjectName("verticalLayout_155")
                self.label_232 = QtWidgets.QLabel(self.widget_94)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_232.setFont(font)
                self.label_232.setObjectName("label_232")
                self.verticalLayout_155.addWidget(self.label_232)
                self.lineEdit_33 = QtWidgets.QLineEdit(self.widget_94)
                self.lineEdit_33.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.lineEdit_33.setObjectName("lineEdit_33")
                self.verticalLayout_155.addWidget(self.lineEdit_33)
                self.verticalLayout_154.addWidget(self.widget_94)
                spacerItem12 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_154.addItem(spacerItem12)
                self.widget_95 = QtWidgets.QWidget(self.ContentOnUpdateWork_3)
                self.widget_95.setObjectName("widget_95")
                self.horizontalLayout_200 = QtWidgets.QHBoxLayout(self.widget_95)
                self.horizontalLayout_200.setObjectName("horizontalLayout_200")
                self.pushButton_170 = QtWidgets.QPushButton(self.widget_95)
                self.pushButton_170.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                self.pushButton_170.setObjectName("pushButton_170")
                self.horizontalLayout_200.addWidget(self.pushButton_170)
                self.verticalLayout_154.addWidget(self.widget_95)
                spacerItem13 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_154.addItem(spacerItem13)
                self.verticalLayout_157.addWidget(self.ContentOnUpdateWork_3)
                self.RightForm.addWidget(self.page)
                self.ManageLeaves = QtWidgets.QWidget()
                self.ManageLeaves.setObjectName("ManageLeaves")
                self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.ManageLeaves)
                self.verticalLayout_60.setObjectName("verticalLayout_60")
                self.UpperPartDashboard_3 = QtWidgets.QWidget(self.ManageLeaves)
                self.UpperPartDashboard_3.setObjectName("UpperPartDashboard_3")
                self.horizontalLayout_108 = QtWidgets.QHBoxLayout(
                self.UpperPartDashboard_3)
                self.horizontalLayout_108.setContentsMargins(6, 6, 6, 6)
                self.horizontalLayout_108.setSpacing(6)
                self.horizontalLayout_108.setObjectName("horizontalLayout_108")
                self.MenuMiscContainerDashboard_3 = QtWidgets.QWidget(
                self.UpperPartDashboard_3)
                self.MenuMiscContainerDashboard_3.setObjectName(
                "MenuMiscContainerDashboard_3")
                self.horizontalLayout_109 = QtWidgets.QHBoxLayout(
                self.MenuMiscContainerDashboard_3)
                self.horizontalLayout_109.setObjectName("horizontalLayout_109")
                self.MenuButtonOnDashboard_3 = QtWidgets.QPushButton(
                self.MenuMiscContainerDashboard_3)
                self.MenuButtonOnDashboard_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnDashboard_3.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.MenuButtonOnDashboard_3.setText("")
                self.MenuButtonOnDashboard_3.setIcon(icon16)
                self.MenuButtonOnDashboard_3.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnDashboard_3.setFlat(True)
                self.MenuButtonOnDashboard_3.setObjectName("MenuButtonOnDashboard_3")
                self.horizontalLayout_109.addWidget(self.MenuButtonOnDashboard_3)
                self.PageNameOnDashboard_3 = QtWidgets.QLabel(
                self.MenuMiscContainerDashboard_3)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.PageNameOnDashboard_3.setFont(font)
                self.PageNameOnDashboard_3.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.PageNameOnDashboard_3.setAlignment(QtCore.Qt.AlignCenter)
                self.PageNameOnDashboard_3.setObjectName("PageNameOnDashboard_3")
                self.horizontalLayout_109.addWidget(self.PageNameOnDashboard_3)
                self.horizontalLayout_108.addWidget(
                self.MenuMiscContainerDashboard_3, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.SearchMiscContainerDashboard_3 = QtWidgets.QWidget(
                self.UpperPartDashboard_3)
                self.SearchMiscContainerDashboard_3.setObjectName(
                "SearchMiscContainerDashboard_3")
                self.horizontalLayout_110 = QtWidgets.QHBoxLayout(
                self.SearchMiscContainerDashboard_3)
                self.horizontalLayout_110.setObjectName("horizontalLayout_110")
                self.BlockforSearch_3 = QtWidgets.QFrame(
                self.SearchMiscContainerDashboard_3)
                self.BlockforSearch_3.setStyleSheet("#BlockforSearch_3{\n"
                                                "border: 2px solid lightblue;\n"
                                                "border-radius: 5px;\n"
                                                "}\n"
                                                "")
                self.BlockforSearch_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BlockforSearch_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearch_3.setObjectName("BlockforSearch_3")
                self.horizontalLayout_111 = QtWidgets.QHBoxLayout(
                self.BlockforSearch_3)
                self.horizontalLayout_111.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_111.setSpacing(0)
                self.horizontalLayout_111.setObjectName("horizontalLayout_111")
                self.SearchIcon_3 = QtWidgets.QLabel(self.BlockforSearch_3)
                self.SearchIcon_3.setText("")
                self.SearchIcon_3.setPixmap(QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIcon_3.setObjectName("SearchIcon_3")
                self.horizontalLayout_111.addWidget(
                self.SearchIcon_3, 0, QtCore.Qt.AlignRight)
                self.FeildForSearch_3 = QtWidgets.QLineEdit(self.BlockforSearch_3)
                self.FeildForSearch_3.setStyleSheet("#FeildForSearch_2{\n"
                                                "border-radius:5px;\n"
                                                "background: transparent;\n"
                                                "}\n"
                                                "#FeildForSearch_2:focus{\n"
                                                "border: 2px solid\n"
                                                "}")
                self.FeildForSearch_3.setObjectName("FeildForSearch_3")
                self.horizontalLayout_111.addWidget(
                self.FeildForSearch_3, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_110.addWidget(
                self.BlockforSearch_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_108.addWidget(
                self.SearchMiscContainerDashboard_3)
                self.RightIconMiscContainer_3 = QtWidgets.QWidget(
                self.UpperPartDashboard_3)
                self.RightIconMiscContainer_3.setObjectName("RightIconMiscContainer_3")
                self.horizontalLayout_43 = QtWidgets.QHBoxLayout(
                self.RightIconMiscContainer_3)
                self.horizontalLayout_43.setObjectName("horizontalLayout_43")
                self.pushButton_22 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_3)
                self.pushButton_22.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_22.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_22.setText("")
                self.pushButton_22.setIcon(icon17)
                self.pushButton_22.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_22.setObjectName("pushButton_22")
                self.horizontalLayout_43.addWidget(self.pushButton_22)
                self.NotificationIconDashboard_3 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_3)
                self.NotificationIconDashboard_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconDashboard_3.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconDashboard_3.setText("")
                self.NotificationIconDashboard_3.setIcon(icon18)
                self.NotificationIconDashboard_3.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconDashboard_3.setObjectName(
                "NotificationIconDashboard_3")
                self.horizontalLayout_43.addWidget(self.NotificationIconDashboard_3)
                self.UserIconDashboard_3 = QtWidgets.QPushButton(
                self.RightIconMiscContainer_3)
                self.UserIconDashboard_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconDashboard_3.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "}\n"
                                                "")
                self.UserIconDashboard_3.setText("")
                self.UserIconDashboard_3.setIcon(icon11)
                self.UserIconDashboard_3.setIconSize(QtCore.QSize(32, 32))
                self.UserIconDashboard_3.setObjectName("UserIconDashboard_3")
                self.horizontalLayout_43.addWidget(self.UserIconDashboard_3)
                self.horizontalLayout_108.addWidget(
                self.RightIconMiscContainer_3, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_60.addWidget(self.UpperPartDashboard_3)
                self.widget_43 = QtWidgets.QWidget(self.ManageLeaves)
                self.widget_43.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_43.setObjectName("widget_43")
                self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.widget_43)
                self.verticalLayout_74.setObjectName("verticalLayout_74")
                self.MessageOnManageLeaves = QtWidgets.QLabel(self.widget_43)
                self.MessageOnManageLeaves.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnManageLeaves.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnManageLeaves.setObjectName("MessageOnManageLeaves")
                self.verticalLayout_74.addWidget(self.MessageOnManageLeaves)
                self.verticalLayout_60.addWidget(self.widget_43)
                self.frameforUserMenu_17 = QtWidgets.QWidget(self.ManageLeaves)
                self.frameforUserMenu_17.setObjectName("frameforUserMenu_17")
                self.horizontalLayout_113 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_17)
                self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_113.setSpacing(0)
                self.horizontalLayout_113.setObjectName("horizontalLayout_113")
                self.UserMenuOnDashboard_3 = QtWidgets.QWidget(
                self.frameforUserMenu_17)
                self.UserMenuOnDashboard_3.setEnabled(False)
                self.UserMenuOnDashboard_3.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnDashboard_3.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnDashboard_3.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnDashboard_3.setObjectName("UserMenuOnDashboard_3")
                self.verticalLayout_59 = QtWidgets.QVBoxLayout(
                self.UserMenuOnDashboard_3)
                self.verticalLayout_59.setObjectName("verticalLayout_59")
                self.label_150 = QtWidgets.QLabel(self.UserMenuOnDashboard_3)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_150.setFont(font)
                self.label_150.setStyleSheet("color: #2596be;")
                self.label_150.setObjectName("label_150")
                self.verticalLayout_59.addWidget(
                self.label_150, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_96 = QtWidgets.QPushButton(self.UserMenuOnDashboard_3)
                self.pushButton_96.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_96.setText("")
                self.pushButton_96.setIcon(icon19)
                self.pushButton_96.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_96.setObjectName("pushButton_96")
                self.verticalLayout_59.addWidget(
                self.pushButton_96, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_97 = QtWidgets.QPushButton(self.UserMenuOnDashboard_3)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_97.setFont(font)
                self.pushButton_97.setIcon(icon11)
                self.pushButton_97.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_97.setObjectName("pushButton_97")
                self.verticalLayout_59.addWidget(
                self.pushButton_97, 0, QtCore.Qt.AlignLeft)
                self.pushButton_98 = QtWidgets.QPushButton(self.UserMenuOnDashboard_3)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_98.setFont(font)
                self.pushButton_98.setIcon(icon20)
                self.pushButton_98.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_98.setObjectName("pushButton_98")
                self.verticalLayout_59.addWidget(
                self.pushButton_98, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_113.addWidget(self.UserMenuOnDashboard_3)
                self.verticalLayout_60.addWidget(
                self.frameforUserMenu_17, 0, QtCore.Qt.AlignRight)
                self.widget = QtWidgets.QWidget(self.ManageLeaves)
                self.widget.setObjectName("widget")
                self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout_61.setObjectName("verticalLayout_61")
                spacerItem14 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_61.addItem(spacerItem14)
                self.pushButton_35 = QtWidgets.QPushButton(self.widget)
                self.pushButton_35.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n"
                                                "")
                self.pushButton_35.setObjectName("pushButton_35")
                self.verticalLayout_61.addWidget(
                self.pushButton_35, 0, QtCore.Qt.AlignHCenter)
                self.label_4 = QtWidgets.QLabel(self.widget)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.verticalLayout_61.addWidget(self.label_4)
                self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
                self.spinBox_2.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.spinBox_2.setObjectName("spinBox_2")
                self.verticalLayout_61.addWidget(self.spinBox_2)
                self.label_35 = QtWidgets.QLabel(self.widget)
                self.label_35.setObjectName("label_35")
                self.verticalLayout_61.addWidget(self.label_35)
                self.textEdit = QtWidgets.QTextEdit(self.widget)
                self.textEdit.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.textEdit.setObjectName("textEdit")
                self.verticalLayout_61.addWidget(self.textEdit)
                self.label_73 = QtWidgets.QLabel(self.widget)
                self.label_73.setObjectName("label_73")
                self.verticalLayout_61.addWidget(self.label_73)
                self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
                self.dateEdit_2.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.dateEdit_2.setObjectName("dateEdit_2")
                self.verticalLayout_61.addWidget(self.dateEdit_2)
                self.label_81 = QtWidgets.QLabel(self.widget)
                self.label_81.setObjectName("label_81")
                self.verticalLayout_61.addWidget(self.label_81)
                self.dateEdit_4 = QtWidgets.QDateEdit(self.widget)
                self.dateEdit_4.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.dateEdit_4.setObjectName("dateEdit_4")
                self.verticalLayout_61.addWidget(self.dateEdit_4)
                self.label_5 = QtWidgets.QLabel(self.widget)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.verticalLayout_61.addWidget(self.label_5)
                self.comboBox_9 = QtWidgets.QComboBox(self.widget)
                self.comboBox_9.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox_9.setObjectName("comboBox_9")
                self.comboBox_9.addItem("")
                self.comboBox_9.addItem("")
                self.verticalLayout_61.addWidget(self.comboBox_9)
                spacerItem15 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_61.addItem(spacerItem15)
                self.pushButton_8 = QtWidgets.QPushButton(self.widget)
                self.pushButton_8.setStyleSheet("background-color: pink;\n"
                                                "padding: 15px;\n"
                                                "color: black;\n"
                                                "")
                self.pushButton_8.setObjectName("pushButton_8")
                self.verticalLayout_61.addWidget(
                self.pushButton_8, 0, QtCore.Qt.AlignHCenter)
                spacerItem16 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_61.addItem(spacerItem16)
                self.tableWidget_4 = QtWidgets.QTableWidget(self.widget)
                self.tableWidget_4.setObjectName("tableWidget_4")
                self.tableWidget_4.setColumnCount(5)
                self.tableWidget_4.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_4.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_4.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_4.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_4.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_4.setHorizontalHeaderItem(4, item)
                self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget_4.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
                self.tableWidget_4.verticalHeader().setCascadingSectionResizes(True)
                self.tableWidget_4.verticalHeader().setSortIndicatorShown(True)
                self.tableWidget_4.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_61.addWidget(self.tableWidget_4)
                self.verticalLayout_60.addWidget(self.widget)
                self.RightForm.addWidget(self.ManageLeaves)
                self.UserProfile = QtWidgets.QWidget()
                self.UserProfile.setObjectName("UserProfile")
                self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.UserProfile)
                self.verticalLayout_13.setObjectName("verticalLayout_13")
                self.UpperPartOnUserProfile = QtWidgets.QWidget(self.UserProfile)
                self.UpperPartOnUserProfile.setStyleSheet("background-color: white;")
                self.UpperPartOnUserProfile.setObjectName("UpperPartOnUserProfile")
                self.horizontalLayout_44 = QtWidgets.QHBoxLayout(
                self.UpperPartOnUserProfile)
                self.horizontalLayout_44.setObjectName("horizontalLayout_44")
                self.MenuButtonMiscOnUserProfile = QtWidgets.QWidget(
                self.UpperPartOnUserProfile)
                self.MenuButtonMiscOnUserProfile.setObjectName(
                "MenuButtonMiscOnUserProfile")
                self.horizontalLayout_45 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnUserProfile)
                self.horizontalLayout_45.setObjectName("horizontalLayout_45")
                self.MenuButtonOnUserProfile = QtWidgets.QPushButton(
                self.MenuButtonMiscOnUserProfile)
                self.MenuButtonOnUserProfile.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnUserProfile.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnUserProfile.setText("")
                self.MenuButtonOnUserProfile.setIcon(icon16)
                self.MenuButtonOnUserProfile.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnUserProfile.setFlat(True)
                self.MenuButtonOnUserProfile.setObjectName("MenuButtonOnUserProfile")
                self.horizontalLayout_45.addWidget(self.MenuButtonOnUserProfile)
                self.LabelforMenuOnUserProfile = QtWidgets.QLabel(
                self.MenuButtonMiscOnUserProfile)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnUserProfile.setFont(font)
                self.LabelforMenuOnUserProfile.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnUserProfile.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnUserProfile.setObjectName(
                "LabelforMenuOnUserProfile")
                self.horizontalLayout_45.addWidget(self.LabelforMenuOnUserProfile)
                self.horizontalLayout_44.addWidget(
                self.MenuButtonMiscOnUserProfile, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnUserProfile = QtWidgets.QWidget(
                self.UpperPartOnUserProfile)
                self.SearchBarMiscOnUserProfile.setObjectName(
                "SearchBarMiscOnUserProfile")
                self.horizontalLayout_46 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnUserProfile)
                self.horizontalLayout_46.setObjectName("horizontalLayout_46")
                self.BlockforSearchOnUserProfile = QtWidgets.QFrame(
                self.SearchBarMiscOnUserProfile)
                self.BlockforSearchOnUserProfile.setStyleSheet("#BlockforSearchOnUserProfile{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                self.BlockforSearchOnUserProfile.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnUserProfile.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnUserProfile.setObjectName(
                "BlockforSearchOnUserProfile")
                self.horizontalLayout_47 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnUserProfile)
                self.horizontalLayout_47.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_47.setSpacing(0)
                self.horizontalLayout_47.setObjectName("horizontalLayout_47")
                self.SearchIconOnUserProfile = QtWidgets.QLabel(
                self.BlockforSearchOnUserProfile)
                self.SearchIconOnUserProfile.setText("")
                self.SearchIconOnUserProfile.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnUserProfile.setObjectName("SearchIconOnUserProfile")
                self.horizontalLayout_47.addWidget(self.SearchIconOnUserProfile)
                self.FeildForSearchOnUserProfile = QtWidgets.QLineEdit(
                self.BlockforSearchOnUserProfile)
                self.FeildForSearchOnUserProfile.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                self.FeildForSearchOnUserProfile.setObjectName(
                "FeildForSearchOnUserProfile")
                self.horizontalLayout_47.addWidget(self.FeildForSearchOnUserProfile)
                self.horizontalLayout_46.addWidget(
                self.BlockforSearchOnUserProfile, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_44.addWidget(
                self.SearchBarMiscOnUserProfile, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMIscOnUserProfile = QtWidgets.QWidget(
                self.UpperPartOnUserProfile)
                self.UserButtonMIscOnUserProfile.setObjectName(
                "UserButtonMIscOnUserProfile")
                self.horizontalLayout_48 = QtWidgets.QHBoxLayout(
                self.UserButtonMIscOnUserProfile)
                self.horizontalLayout_48.setObjectName("horizontalLayout_48")
                self.pushButton_24 = QtWidgets.QPushButton(
                self.UserButtonMIscOnUserProfile)
                self.pushButton_24.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_24.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_24.setText("")
                self.pushButton_24.setIcon(icon17)
                self.pushButton_24.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_24.setObjectName("pushButton_24")
                self.horizontalLayout_48.addWidget(self.pushButton_24)
                self.NotificationIconOnUserProfile = QtWidgets.QPushButton(
                self.UserButtonMIscOnUserProfile)
                self.NotificationIconOnUserProfile.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnUserProfile.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnUserProfile.setText("")
                self.NotificationIconOnUserProfile.setIcon(icon18)
                self.NotificationIconOnUserProfile.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnUserProfile.setObjectName(
                "NotificationIconOnUserProfile")
                self.horizontalLayout_48.addWidget(self.NotificationIconOnUserProfile)
                self.UserIconOnUserProfile = QtWidgets.QPushButton(
                self.UserButtonMIscOnUserProfile)
                self.UserIconOnUserProfile.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnUserProfile.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnUserProfile.setText("")
                self.UserIconOnUserProfile.setIcon(icon11)
                self.UserIconOnUserProfile.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnUserProfile.setObjectName("UserIconOnUserProfile")
                self.horizontalLayout_48.addWidget(self.UserIconOnUserProfile)
                self.horizontalLayout_44.addWidget(
                self.UserButtonMIscOnUserProfile, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_13.addWidget(self.UpperPartOnUserProfile)
                self.widget_44 = QtWidgets.QWidget(self.UserProfile)
                self.widget_44.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_44.setObjectName("widget_44")
                self.verticalLayout_75 = QtWidgets.QVBoxLayout(self.widget_44)
                self.verticalLayout_75.setObjectName("verticalLayout_75")
                self.MessageOnProfile = QtWidgets.QLabel(self.widget_44)
                self.MessageOnProfile.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnProfile.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnProfile.setObjectName("MessageOnProfile")
                self.verticalLayout_75.addWidget(self.MessageOnProfile)
                self.verticalLayout_13.addWidget(self.widget_44)
                self.frameforUserMenu_10 = QtWidgets.QWidget(self.UserProfile)
                self.frameforUserMenu_10.setObjectName("frameforUserMenu_10")
                self.horizontalLayout_100 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_10)
                self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_100.setSpacing(0)
                self.horizontalLayout_100.setObjectName("horizontalLayout_100")
                self.UserMenuOnUserProfile = QtWidgets.QWidget(
                self.frameforUserMenu_10)
                self.UserMenuOnUserProfile.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnUserProfile.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnUserProfile.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnUserProfile.setObjectName("UserMenuOnUserProfile")
                self.verticalLayout_52 = QtWidgets.QVBoxLayout(
                self.UserMenuOnUserProfile)
                self.verticalLayout_52.setObjectName("verticalLayout_52")
                self.label_143 = QtWidgets.QLabel(self.UserMenuOnUserProfile)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_143.setFont(font)
                self.label_143.setStyleSheet("color: #2596be;")
                self.label_143.setObjectName("label_143")
                self.verticalLayout_52.addWidget(
                self.label_143, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_75 = QtWidgets.QPushButton(self.UserMenuOnUserProfile)
                self.pushButton_75.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_75.setText("")
                self.pushButton_75.setIcon(icon19)
                self.pushButton_75.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_75.setObjectName("pushButton_75")
                self.verticalLayout_52.addWidget(self.pushButton_75)
                self.pushButton_76 = QtWidgets.QPushButton(self.UserMenuOnUserProfile)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_76.setFont(font)
                self.pushButton_76.setIcon(icon11)
                self.pushButton_76.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_76.setObjectName("pushButton_76")
                self.verticalLayout_52.addWidget(
                self.pushButton_76, 0, QtCore.Qt.AlignLeft)
                self.pushButton_77 = QtWidgets.QPushButton(self.UserMenuOnUserProfile)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_77.setFont(font)
                self.pushButton_77.setIcon(icon20)
                self.pushButton_77.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_77.setObjectName("pushButton_77")
                self.verticalLayout_52.addWidget(
                self.pushButton_77, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_100.addWidget(self.UserMenuOnUserProfile)
                self.verticalLayout_13.addWidget(
                self.frameforUserMenu_10, 0, QtCore.Qt.AlignRight)
                self.ContentOnUserProfile = QtWidgets.QWidget(self.UserProfile)
                self.ContentOnUserProfile.setObjectName("ContentOnUserProfile")
                self.verticalLayout_14 = QtWidgets.QVBoxLayout(
                self.ContentOnUserProfile)
                self.verticalLayout_14.setObjectName("verticalLayout_14")
                self.label_19 = QtWidgets.QLabel(self.ContentOnUserProfile)
                self.label_19.setText("")
                self.label_19.setPixmap(QtGui.QPixmap("../Icons/Template Image.png"))
                self.label_19.setObjectName("label_19")
                self.verticalLayout_14.addWidget(
                self.label_19, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_34 = QtWidgets.QPushButton(self.ContentOnUserProfile)
                self.pushButton_34.setStyleSheet("#pushButton_34{\n"
                                                "background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "}\n"
                                                "#pushButton_34:hover{\n"
                                                "background-color: lightgreen;\n"
                                                "padding: 10px;\n"
                                                "}\n"
                                                "")
                self.pushButton_34.setObjectName("pushButton_34")
                self.verticalLayout_14.addWidget(
                self.pushButton_34, 0, QtCore.Qt.AlignHCenter)
                spacerItem17 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_14.addItem(spacerItem17)
                self.verticalLayout_13.addWidget(self.ContentOnUserProfile)
                self.widget_6 = QtWidgets.QWidget(self.UserProfile)
                self.widget_6.setObjectName("widget_6")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_6)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.label_25 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_25.setFont(font)
                self.label_25.setObjectName("label_25")
                self.gridLayout_2.addWidget(
                self.label_25, 5, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_28 = QtWidgets.QLabel(self.widget_6)
                self.label_28.setObjectName("label_28")
                self.gridLayout_2.addWidget(self.label_28, 2, 1, 1, 1)
                self.label_26 = QtWidgets.QLabel(self.widget_6)
                self.label_26.setObjectName("label_26")
                self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)
                self.label_27 = QtWidgets.QLabel(self.widget_6)
                self.label_27.setObjectName("label_27")
                self.gridLayout_2.addWidget(self.label_27, 1, 1, 1, 1)
                self.label_29 = QtWidgets.QLabel(self.widget_6)
                self.label_29.setObjectName("label_29")
                self.gridLayout_2.addWidget(self.label_29, 3, 1, 1, 1)
                self.label_30 = QtWidgets.QLabel(self.widget_6)
                self.label_30.setObjectName("label_30")
                self.gridLayout_2.addWidget(self.label_30, 4, 1, 1, 1)
                self.label_31 = QtWidgets.QLabel(self.widget_6)
                self.label_31.setObjectName("label_31")
                self.gridLayout_2.addWidget(self.label_31, 5, 1, 1, 1)
                self.label_32 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_32.setFont(font)
                self.label_32.setObjectName("label_32")
                self.gridLayout_2.addWidget(
                self.label_32, 6, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_20 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_20.setFont(font)
                self.label_20.setObjectName("label_20")
                self.gridLayout_2.addWidget(
                self.label_20, 0, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_23 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_23.setFont(font)
                self.label_23.setObjectName("label_23")
                self.gridLayout_2.addWidget(
                self.label_23, 3, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_22 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_22.setFont(font)
                self.label_22.setObjectName("label_22")
                self.gridLayout_2.addWidget(
                self.label_22, 2, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_21 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_21.setFont(font)
                self.label_21.setObjectName("label_21")
                self.gridLayout_2.addWidget(
                self.label_21, 1, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_24 = QtWidgets.QLabel(self.widget_6)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_24.setFont(font)
                self.label_24.setObjectName("label_24")
                self.gridLayout_2.addWidget(
                self.label_24, 4, 0, 1, 1, QtCore.Qt.AlignRight)
                self.label_2 = QtWidgets.QLabel(self.widget_6)
                self.label_2.setObjectName("label_2")
                self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
                self.verticalLayout_13.addWidget(self.widget_6)
                self.widget_7 = QtWidgets.QWidget(self.UserProfile)
                self.widget_7.setObjectName("widget_7")
                self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_7)
                self.verticalLayout_16.setObjectName("verticalLayout_16")
                spacerItem18 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_16.addItem(spacerItem18)
                self.pushButton_9 = QtWidgets.QPushButton(self.widget_7)
                self.pushButton_9.setStyleSheet("background-color: pink;\n"
                                                "padding: 10px;\n"
                                                "color: white;\n"
                                                "")
                self.pushButton_9.setObjectName("pushButton_9")
                self.verticalLayout_16.addWidget(
                self.pushButton_9, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_13.addWidget(self.widget_7)
                self.RightForm.addWidget(self.UserProfile)
                self.TDLProductivity = QtWidgets.QWidget()
                self.TDLProductivity.setObjectName("TDLProductivity")
                self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.TDLProductivity)
                self.verticalLayout_23.setObjectName("verticalLayout_23")
                self.UpperPartOnTDLProductivity = QtWidgets.QWidget(
                self.TDLProductivity)
                self.UpperPartOnTDLProductivity.setStyleSheet(
                "background-color: white;")
                self.UpperPartOnTDLProductivity.setObjectName(
                "UpperPartOnTDLProductivity")
                self.horizontalLayout_54 = QtWidgets.QHBoxLayout(
                self.UpperPartOnTDLProductivity)
                self.horizontalLayout_54.setObjectName("horizontalLayout_54")
                self.MenuButtonMiscOnTDLProductivity = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity)
                self.MenuButtonMiscOnTDLProductivity.setObjectName(
                "MenuButtonMiscOnTDLProductivity")
                self.horizontalLayout_55 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnTDLProductivity)
                self.horizontalLayout_55.setObjectName("horizontalLayout_55")
                self.MenuButtonOnTDLProductivity = QtWidgets.QPushButton(
                self.MenuButtonMiscOnTDLProductivity)
                self.MenuButtonOnTDLProductivity.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnTDLProductivity.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnTDLProductivity.setText("")
                self.MenuButtonOnTDLProductivity.setIcon(icon16)
                self.MenuButtonOnTDLProductivity.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnTDLProductivity.setFlat(True)
                self.MenuButtonOnTDLProductivity.setObjectName(
                "MenuButtonOnTDLProductivity")
                self.horizontalLayout_55.addWidget(self.MenuButtonOnTDLProductivity)
                self.LabelforMenuOnTDLProductivity = QtWidgets.QLabel(
                self.MenuButtonMiscOnTDLProductivity)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnTDLProductivity.setFont(font)
                self.LabelforMenuOnTDLProductivity.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                self.LabelforMenuOnTDLProductivity.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnTDLProductivity.setObjectName(
                "LabelforMenuOnTDLProductivity")
                self.horizontalLayout_55.addWidget(self.LabelforMenuOnTDLProductivity)
                self.horizontalLayout_54.addWidget(
                self.MenuButtonMiscOnTDLProductivity, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnTDLProductivity = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity)
                self.SearchBarMiscOnTDLProductivity.setObjectName(
                "SearchBarMiscOnTDLProductivity")
                self.horizontalLayout_56 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnTDLProductivity)
                self.horizontalLayout_56.setObjectName("horizontalLayout_56")
                self.BlockforSearchOnTDLProductivity = QtWidgets.QFrame(
                self.SearchBarMiscOnTDLProductivity)
                self.BlockforSearchOnTDLProductivity.setStyleSheet("#BlockforSearchOnTDLProductivity{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnTDLProductivity.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnTDLProductivity.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnTDLProductivity.setObjectName(
                "BlockforSearchOnTDLProductivity")
                self.horizontalLayout_57 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnTDLProductivity)
                self.horizontalLayout_57.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_57.setSpacing(0)
                self.horizontalLayout_57.setObjectName("horizontalLayout_57")
                self.SearchIconOnTDLProductivity = QtWidgets.QLabel(
                self.BlockforSearchOnTDLProductivity)
                self.SearchIconOnTDLProductivity.setText("")
                self.SearchIconOnTDLProductivity.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnTDLProductivity.setObjectName(
                "SearchIconOnTDLProductivity")
                self.horizontalLayout_57.addWidget(self.SearchIconOnTDLProductivity)
                self.FeildForSearchOnTDLProductivity = QtWidgets.QLineEdit(
                self.BlockforSearchOnTDLProductivity)
                self.FeildForSearchOnTDLProductivity.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnTDLProductivity.setObjectName(
                "FeildForSearchOnTDLProductivity")
                self.horizontalLayout_57.addWidget(
                self.FeildForSearchOnTDLProductivity)
                self.horizontalLayout_56.addWidget(
                self.BlockforSearchOnTDLProductivity, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_54.addWidget(
                self.SearchBarMiscOnTDLProductivity, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnTDLProductivity = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity)
                self.UserButtonMiscOnTDLProductivity.setObjectName(
                "UserButtonMiscOnTDLProductivity")
                self.horizontalLayout_49 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnTDLProductivity)
                self.horizontalLayout_49.setObjectName("horizontalLayout_49")
                self.pushButton_25 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity)
                self.pushButton_25.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_25.setText("")
                self.pushButton_25.setIcon(icon17)
                self.pushButton_25.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_25.setObjectName("pushButton_25")
                self.horizontalLayout_49.addWidget(self.pushButton_25)
                self.NotificationIconOnTDLProductivity = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity)
                self.NotificationIconOnTDLProductivity.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnTDLProductivity.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnTDLProductivity.setText("")
                self.NotificationIconOnTDLProductivity.setIcon(icon18)
                self.NotificationIconOnTDLProductivity.setIconSize(
                QtCore.QSize(30, 30))
                self.NotificationIconOnTDLProductivity.setObjectName(
                "NotificationIconOnTDLProductivity")
                self.horizontalLayout_49.addWidget(
                self.NotificationIconOnTDLProductivity)
                self.UserIconOnTDLProductivity = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity)
                self.UserIconOnTDLProductivity.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnTDLProductivity.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnTDLProductivity.setText("")
                self.UserIconOnTDLProductivity.setIcon(icon11)
                self.UserIconOnTDLProductivity.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnTDLProductivity.setObjectName(
                "UserIconOnTDLProductivity")
                self.horizontalLayout_49.addWidget(self.UserIconOnTDLProductivity)
                self.horizontalLayout_54.addWidget(
                self.UserButtonMiscOnTDLProductivity, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_23.addWidget(self.UpperPartOnTDLProductivity)
                self.widget_45 = QtWidgets.QWidget(self.TDLProductivity)
                self.widget_45.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_45.setObjectName("widget_45")
                self.verticalLayout_76 = QtWidgets.QVBoxLayout(self.widget_45)
                self.verticalLayout_76.setObjectName("verticalLayout_76")
                self.MessageOnTDL = QtWidgets.QLabel(self.widget_45)
                self.MessageOnTDL.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnTDL.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnTDL.setObjectName("MessageOnTDL")
                self.verticalLayout_76.addWidget(self.MessageOnTDL)
                self.verticalLayout_23.addWidget(self.widget_45)
                self.frameforUserMenu_12 = QtWidgets.QWidget(self.TDLProductivity)
                self.frameforUserMenu_12.setObjectName("frameforUserMenu_12")
                self.horizontalLayout_102 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_12)
                self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_102.setSpacing(0)
                self.horizontalLayout_102.setObjectName("horizontalLayout_102")
                self.UserMenuOnTDLProductivity = QtWidgets.QWidget(
                self.frameforUserMenu_12)
                self.UserMenuOnTDLProductivity.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnTDLProductivity.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnTDLProductivity.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnTDLProductivity.setObjectName(
                "UserMenuOnTDLProductivity")
                self.verticalLayout_54 = QtWidgets.QVBoxLayout(
                self.UserMenuOnTDLProductivity)
                self.verticalLayout_54.setObjectName("verticalLayout_54")
                self.label_145 = QtWidgets.QLabel(self.UserMenuOnTDLProductivity)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_145.setFont(font)
                self.label_145.setStyleSheet("color: #2596be;")
                self.label_145.setObjectName("label_145")
                self.verticalLayout_54.addWidget(
                self.label_145, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_81 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity)
                self.pushButton_81.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_81.setText("")
                self.pushButton_81.setIcon(icon19)
                self.pushButton_81.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_81.setObjectName("pushButton_81")
                self.verticalLayout_54.addWidget(self.pushButton_81)
                self.pushButton_82 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_82.setFont(font)
                self.pushButton_82.setIcon(icon11)
                self.pushButton_82.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_82.setObjectName("pushButton_82")
                self.verticalLayout_54.addWidget(
                self.pushButton_82, 0, QtCore.Qt.AlignLeft)
                self.pushButton_83 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_83.setFont(font)
                self.pushButton_83.setIcon(icon20)
                self.pushButton_83.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_83.setObjectName("pushButton_83")
                self.verticalLayout_54.addWidget(
                self.pushButton_83, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_102.addWidget(self.UserMenuOnTDLProductivity)
                self.verticalLayout_23.addWidget(
                self.frameforUserMenu_12, 0, QtCore.Qt.AlignRight)
                self.ContentOnTDLProductivity = QtWidgets.QWidget(self.TDLProductivity)
                self.ContentOnTDLProductivity.setObjectName("ContentOnTDLProductivity")
                self.gridLayout_3 = QtWidgets.QGridLayout(
                self.ContentOnTDLProductivity)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.widget_8 = QtWidgets.QWidget(self.ContentOnTDLProductivity)
                self.widget_8.setObjectName("widget_8")
                self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.widget_8)
                self.verticalLayout_27.setObjectName("verticalLayout_27")
                self.label_36 = QtWidgets.QLabel(self.widget_8)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_36.setFont(font)
                self.label_36.setObjectName("label_36")
                self.verticalLayout_27.addWidget(self.label_36)
                self.lineEdit = QtWidgets.QLineEdit(self.widget_8)
                self.lineEdit.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.lineEdit.setObjectName("lineEdit")
                self.verticalLayout_27.addWidget(self.lineEdit)
                self.label_15 = QtWidgets.QLabel(self.widget_8)
                self.label_15.setObjectName("label_15")
                self.verticalLayout_27.addWidget(self.label_15)
                self.dateEdit_3 = QtWidgets.QDateEdit(self.widget_8)
                self.dateEdit_3.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.dateEdit_3.setObjectName("dateEdit_3")
                self.verticalLayout_27.addWidget(self.dateEdit_3)
                self.pushButton_18 = QtWidgets.QPushButton(self.widget_8)
                self.pushButton_18.setStyleSheet("color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                self.pushButton_18.setObjectName("pushButton_18")
                self.verticalLayout_27.addWidget(self.pushButton_18)
                self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)
                self.label_34 = QtWidgets.QLabel(self.ContentOnTDLProductivity)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_34.setFont(font)
                self.label_34.setObjectName("label_34")
                self.gridLayout_3.addWidget(
                self.label_34, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
                spacerItem19 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout_3.addItem(spacerItem19, 1, 0, 1, 1)
                self.pushButton_17 = QtWidgets.QPushButton(
                self.ContentOnTDLProductivity)
                self.pushButton_17.setStyleSheet("color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;")
                self.pushButton_17.setObjectName("pushButton_17")
                self.gridLayout_3.addWidget(self.pushButton_17, 2, 0, 1, 1)
                spacerItem20 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout_3.addItem(spacerItem20, 6, 0, 1, 1)
                self.tableWidget_5 = QtWidgets.QTableWidget(
                self.ContentOnTDLProductivity)
                self.tableWidget_5.setObjectName("tableWidget_5")
                self.tableWidget_5.setColumnCount(2)
                self.tableWidget_5.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_5.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_5.setHorizontalHeaderItem(1, item)
                self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget_5.horizontalHeader().setDefaultSectionSize(160)
                self.tableWidget_5.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
                self.gridLayout_3.addWidget(self.tableWidget_5, 5, 0, 1, 1)
                self.verticalLayout_23.addWidget(self.ContentOnTDLProductivity)
                self.RightForm.addWidget(self.TDLProductivity)
                self.ManageTeamLeavesPage = QtWidgets.QWidget()
                self.ManageTeamLeavesPage.setObjectName("ManageTeamLeavesPage")
                self.verticalLayout_42 = QtWidgets.QVBoxLayout(
                self.ManageTeamLeavesPage)
                self.verticalLayout_42.setObjectName("verticalLayout_42")
                self.UpperPartOnTDLProductivity_3 = QtWidgets.QWidget(
                self.ManageTeamLeavesPage)
                self.UpperPartOnTDLProductivity_3.setStyleSheet(
                "background-color: white;")
                self.UpperPartOnTDLProductivity_3.setObjectName(
                "UpperPartOnTDLProductivity_3")
                self.horizontalLayout_65 = QtWidgets.QHBoxLayout(
                self.UpperPartOnTDLProductivity_3)
                self.horizontalLayout_65.setObjectName("horizontalLayout_65")
                self.MenuButtonMiscOnTDLProductivity_3 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_3)
                self.MenuButtonMiscOnTDLProductivity_3.setObjectName(
                "MenuButtonMiscOnTDLProductivity_3")
                self.horizontalLayout_66 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnTDLProductivity_3)
                self.horizontalLayout_66.setObjectName("horizontalLayout_66")
                self.MenuButtonOnTDLProductivity_3 = QtWidgets.QPushButton(
                self.MenuButtonMiscOnTDLProductivity_3)
                self.MenuButtonOnTDLProductivity_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnTDLProductivity_3.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")
                self.MenuButtonOnTDLProductivity_3.setText("")
                self.MenuButtonOnTDLProductivity_3.setIcon(icon16)
                self.MenuButtonOnTDLProductivity_3.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnTDLProductivity_3.setFlat(True)
                self.MenuButtonOnTDLProductivity_3.setObjectName(
                "MenuButtonOnTDLProductivity_3")
                self.horizontalLayout_66.addWidget(self.MenuButtonOnTDLProductivity_3)
                self.LabelforMenuOnTDLProductivity_3 = QtWidgets.QLabel(
                self.MenuButtonMiscOnTDLProductivity_3)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnTDLProductivity_3.setFont(font)
                self.LabelforMenuOnTDLProductivity_3.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                self.LabelforMenuOnTDLProductivity_3.setAlignment(
                QtCore.Qt.AlignCenter)
                self.LabelforMenuOnTDLProductivity_3.setObjectName(
                "LabelforMenuOnTDLProductivity_3")
                self.horizontalLayout_66.addWidget(
                self.LabelforMenuOnTDLProductivity_3)
                self.horizontalLayout_65.addWidget(
                self.MenuButtonMiscOnTDLProductivity_3, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.SearchBarMiscOnTDLProductivity_3 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_3)
                self.SearchBarMiscOnTDLProductivity_3.setObjectName(
                "SearchBarMiscOnTDLProductivity_3")
                self.horizontalLayout_67 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnTDLProductivity_3)
                self.horizontalLayout_67.setObjectName("horizontalLayout_67")
                self.BlockforSearchOnTDLProductivity_3 = QtWidgets.QFrame(
                self.SearchBarMiscOnTDLProductivity_3)
                self.BlockforSearchOnTDLProductivity_3.setStyleSheet("#BlockforSearchOnTDLProductivity{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnTDLProductivity_3.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnTDLProductivity_3.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnTDLProductivity_3.setObjectName(
                "BlockforSearchOnTDLProductivity_3")
                self.horizontalLayout_68 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnTDLProductivity_3)
                self.horizontalLayout_68.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_68.setSpacing(0)
                self.horizontalLayout_68.setObjectName("horizontalLayout_68")
                self.SearchIconOnTDLProductivity_3 = QtWidgets.QLabel(
                self.BlockforSearchOnTDLProductivity_3)
                self.SearchIconOnTDLProductivity_3.setText("")
                self.SearchIconOnTDLProductivity_3.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnTDLProductivity_3.setObjectName(
                "SearchIconOnTDLProductivity_3")
                self.horizontalLayout_68.addWidget(self.SearchIconOnTDLProductivity_3)
                self.FeildForSearchOnTDLProductivity_3 = QtWidgets.QLineEdit(
                self.BlockforSearchOnTDLProductivity_3)
                self.FeildForSearchOnTDLProductivity_3.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnTDLProductivity_3.setObjectName(
                "FeildForSearchOnTDLProductivity_3")
                self.horizontalLayout_68.addWidget(
                self.FeildForSearchOnTDLProductivity_3)
                self.horizontalLayout_67.addWidget(
                self.BlockforSearchOnTDLProductivity_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_65.addWidget(
                self.SearchBarMiscOnTDLProductivity_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.UserButtonMiscOnTDLProductivity_3 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_3)
                self.UserButtonMiscOnTDLProductivity_3.setObjectName(
                "UserButtonMiscOnTDLProductivity_3")
                self.horizontalLayout_69 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnTDLProductivity_3)
                self.horizontalLayout_69.setObjectName("horizontalLayout_69")
                self.pushButton_31 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_3)
                self.pushButton_31.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_31.setText("")
                self.pushButton_31.setIcon(icon17)
                self.pushButton_31.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_31.setObjectName("pushButton_31")
                self.horizontalLayout_69.addWidget(self.pushButton_31)
                self.NotificationIconOnTDLProductivity_3 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_3)
                self.NotificationIconOnTDLProductivity_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnTDLProductivity_3.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnTDLProductivity_3.setText("")
                self.NotificationIconOnTDLProductivity_3.setIcon(icon18)
                self.NotificationIconOnTDLProductivity_3.setIconSize(
                QtCore.QSize(30, 30))
                self.NotificationIconOnTDLProductivity_3.setObjectName(
                "NotificationIconOnTDLProductivity_3")
                self.horizontalLayout_69.addWidget(
                self.NotificationIconOnTDLProductivity_3)
                self.UserIconOnTDLProductivity_3 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_3)
                self.UserIconOnTDLProductivity_3.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnTDLProductivity_3.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnTDLProductivity_3.setText("")
                self.UserIconOnTDLProductivity_3.setIcon(icon11)
                self.UserIconOnTDLProductivity_3.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnTDLProductivity_3.setObjectName(
                "UserIconOnTDLProductivity_3")
                self.horizontalLayout_69.addWidget(self.UserIconOnTDLProductivity_3)
                self.horizontalLayout_65.addWidget(
                self.UserButtonMiscOnTDLProductivity_3, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_42.addWidget(self.UpperPartOnTDLProductivity_3)
                self.widget_46 = QtWidgets.QWidget(self.ManageTeamLeavesPage)
                self.widget_46.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_46.setObjectName("widget_46")
                self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.widget_46)
                self.verticalLayout_77.setObjectName("verticalLayout_77")
                self.MessageOnManageTeamLeaves = QtWidgets.QLabel(self.widget_46)
                self.MessageOnManageTeamLeaves.setMaximumSize(
                QtCore.QSize(16777215, 0))
                self.MessageOnManageTeamLeaves.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnManageTeamLeaves.setObjectName(
                "MessageOnManageTeamLeaves")
                self.verticalLayout_77.addWidget(self.MessageOnManageTeamLeaves)
                self.verticalLayout_42.addWidget(self.widget_46)
                self.frameforUserMenu_13 = QtWidgets.QWidget(self.ManageTeamLeavesPage)
                self.frameforUserMenu_13.setObjectName("frameforUserMenu_13")
                self.horizontalLayout_103 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_13)
                self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_103.setSpacing(0)
                self.horizontalLayout_103.setObjectName("horizontalLayout_103")
                self.UserMenuOnTDLProductivity_2 = QtWidgets.QWidget(
                self.frameforUserMenu_13)
                self.UserMenuOnTDLProductivity_2.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnTDLProductivity_2.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnTDLProductivity_2.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnTDLProductivity_2.setObjectName(
                "UserMenuOnTDLProductivity_2")
                self.verticalLayout_56 = QtWidgets.QVBoxLayout(
                self.UserMenuOnTDLProductivity_2)
                self.verticalLayout_56.setObjectName("verticalLayout_56")
                self.label_146 = QtWidgets.QLabel(self.UserMenuOnTDLProductivity_2)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_146.setFont(font)
                self.label_146.setStyleSheet("color: #2596be;")
                self.label_146.setObjectName("label_146")
                self.verticalLayout_56.addWidget(
                self.label_146, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_84 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity_2)
                self.pushButton_84.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_84.setText("")
                self.pushButton_84.setIcon(icon19)
                self.pushButton_84.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_84.setObjectName("pushButton_84")
                self.verticalLayout_56.addWidget(self.pushButton_84)
                self.pushButton_85 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_85.setFont(font)
                self.pushButton_85.setIcon(icon11)
                self.pushButton_85.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_85.setObjectName("pushButton_85")
                self.verticalLayout_56.addWidget(
                self.pushButton_85, 0, QtCore.Qt.AlignLeft)
                self.pushButton_86 = QtWidgets.QPushButton(
                self.UserMenuOnTDLProductivity_2)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_86.setFont(font)
                self.pushButton_86.setIcon(icon20)
                self.pushButton_86.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_86.setObjectName("pushButton_86")
                self.verticalLayout_56.addWidget(
                self.pushButton_86, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_103.addWidget(self.UserMenuOnTDLProductivity_2)
                self.verticalLayout_42.addWidget(
                self.frameforUserMenu_13, 0, QtCore.Qt.AlignRight)
                self.widget_24 = QtWidgets.QWidget(self.ManageTeamLeavesPage)
                self.widget_24.setObjectName("widget_24")
                self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.widget_24)
                self.verticalLayout_45.setObjectName("verticalLayout_45")
                self.tableWidget_6 = QtWidgets.QTableWidget(self.widget_24)
                self.tableWidget_6.setObjectName("tableWidget_6")
                self.tableWidget_6.setColumnCount(4)
                self.tableWidget_6.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_6.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_6.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_6.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_6.setHorizontalHeaderItem(3, item)
                self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget_6.horizontalHeader().setSortIndicatorShown(True)
                self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
                self.tableWidget_6.verticalHeader().setCascadingSectionResizes(True)
                self.tableWidget_6.verticalHeader().setSortIndicatorShown(True)
                self.tableWidget_6.verticalHeader().setStretchLastSection(True)
                self.verticalLayout_45.addWidget(self.tableWidget_6)
                self.widget_25 = QtWidgets.QWidget(self.widget_24)
                self.widget_25.setObjectName("widget_25")
                self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_25)
                self.gridLayout_5.setObjectName("gridLayout_5")
                self.label_75 = QtWidgets.QLabel(self.widget_25)
                self.label_75.setObjectName("label_75")
                self.gridLayout_5.addWidget(self.label_75, 1, 1, 1, 1)
                self.label_76 = QtWidgets.QLabel(self.widget_25)
                self.label_76.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                self.label_76.setObjectName("label_76")
                self.gridLayout_5.addWidget(self.label_76, 2, 0, 1, 1)
                self.label_78 = QtWidgets.QLabel(self.widget_25)
                self.label_78.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                self.label_78.setObjectName("label_78")
                self.gridLayout_5.addWidget(self.label_78, 3, 0, 1, 1)
                self.label_77 = QtWidgets.QLabel(self.widget_25)
                self.label_77.setScaledContents(True)
                self.label_77.setObjectName("label_77")
                self.gridLayout_5.addWidget(self.label_77, 2, 1, 1, 1)
                self.pushButton_33 = QtWidgets.QPushButton(self.widget_25)
                self.pushButton_33.setStyleSheet("#pushButton_33{\n"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                " }\n"
                                                "#pushButton_33:hover {background-color: red; \\n padding: 10px; }")
                self.pushButton_33.setObjectName("pushButton_33")
                self.gridLayout_5.addWidget(self.pushButton_33, 4, 1, 1, 1)
                self.pushButton_32 = QtWidgets.QPushButton(self.widget_25)
                self.pushButton_32.setStyleSheet("#pushButton_32{\n"
                                                "    background-color: pink;\n"
                                                "     padding: 10px; \n"
                                                " }\n"
                                                "#pushButton_32:hover {background-color: lightgreen; \\n padding: 10px; }")
                self.pushButton_32.setObjectName("pushButton_32")
                self.gridLayout_5.addWidget(self.pushButton_32, 4, 0, 1, 1)
                self.label_79 = QtWidgets.QLabel(self.widget_25)
                self.label_79.setObjectName("label_79")
                self.gridLayout_5.addWidget(self.label_79, 3, 1, 1, 1)
                self.label_74 = QtWidgets.QLabel(self.widget_25)
                self.label_74.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                self.label_74.setObjectName("label_74")
                self.gridLayout_5.addWidget(self.label_74, 1, 0, 1, 1)
                self.widget_26 = QtWidgets.QWidget(self.widget_25)
                self.widget_26.setObjectName("widget_26")
                self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.widget_26)
                self.verticalLayout_55.setObjectName("verticalLayout_55")
                self.label_80 = QtWidgets.QLabel(self.widget_26)
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.label_80.setFont(font)
                self.label_80.setAlignment(QtCore.Qt.AlignCenter)
                self.label_80.setObjectName("label_80")
                self.verticalLayout_55.addWidget(self.label_80)
                self.gridLayout_5.addWidget(self.widget_26, 0, 0, 1, 2)
                self.verticalLayout_45.addWidget(self.widget_25)
                self.verticalLayout_42.addWidget(self.widget_24)
                self.RightForm.addWidget(self.ManageTeamLeavesPage)
                self.EvaluationPage = QtWidgets.QWidget()
                self.EvaluationPage.setObjectName("EvaluationPage")
                self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.EvaluationPage)
                self.verticalLayout_26.setObjectName("verticalLayout_26")
                self.UpperPartOnTDLProductivity_2 = QtWidgets.QWidget(
                self.EvaluationPage)
                self.UpperPartOnTDLProductivity_2.setStyleSheet(
                "background-color: white;")
                self.UpperPartOnTDLProductivity_2.setObjectName(
                "UpperPartOnTDLProductivity_2")
                self.horizontalLayout_58 = QtWidgets.QHBoxLayout(
                self.UpperPartOnTDLProductivity_2)
                self.horizontalLayout_58.setObjectName("horizontalLayout_58")
                self.MenuButtonMiscOnTDLProductivity_2 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_2)
                self.MenuButtonMiscOnTDLProductivity_2.setObjectName(
                "MenuButtonMiscOnTDLProductivity_2")
                self.horizontalLayout_59 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnTDLProductivity_2)
                self.horizontalLayout_59.setObjectName("horizontalLayout_59")
                self.MenuButtonOnTDLProductivity_2 = QtWidgets.QPushButton(
                self.MenuButtonMiscOnTDLProductivity_2)
                self.MenuButtonOnTDLProductivity_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                                "background-color: #2596be;\n"
                                                                "}")
                self.MenuButtonOnTDLProductivity_2.setText("")
                self.MenuButtonOnTDLProductivity_2.setIcon(icon16)
                self.MenuButtonOnTDLProductivity_2.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnTDLProductivity_2.setFlat(True)
                self.MenuButtonOnTDLProductivity_2.setObjectName(
                "MenuButtonOnTDLProductivity_2")
                self.horizontalLayout_59.addWidget(self.MenuButtonOnTDLProductivity_2)
                self.LabelforMenuOnTDLProductivity_2 = QtWidgets.QLabel(
                self.MenuButtonMiscOnTDLProductivity_2)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnTDLProductivity_2.setFont(font)
                self.LabelforMenuOnTDLProductivity_2.setStyleSheet("color : #2596be;\n"
                                                                "font: bold;\n"
                                                                "")
                self.LabelforMenuOnTDLProductivity_2.setAlignment(
                QtCore.Qt.AlignCenter)
                self.LabelforMenuOnTDLProductivity_2.setObjectName(
                "LabelforMenuOnTDLProductivity_2")
                self.horizontalLayout_59.addWidget(
                self.LabelforMenuOnTDLProductivity_2)
                self.horizontalLayout_58.addWidget(
                self.MenuButtonMiscOnTDLProductivity_2, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnTDLProductivity_2 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_2)
                self.SearchBarMiscOnTDLProductivity_2.setObjectName(
                "SearchBarMiscOnTDLProductivity_2")
                self.horizontalLayout_60 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnTDLProductivity_2)
                self.horizontalLayout_60.setObjectName("horizontalLayout_60")
                self.BlockforSearchOnTDLProductivity_2 = QtWidgets.QFrame(
                self.SearchBarMiscOnTDLProductivity_2)
                self.BlockforSearchOnTDLProductivity_2.setStyleSheet("#BlockforSearchOnTDLProductivity{\n"
                                                                "border: 2px solid lightblue;\n"
                                                                "border-radius: 5px;\n"
                                                                "}\n"
                                                                "")
                self.BlockforSearchOnTDLProductivity_2.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnTDLProductivity_2.setFrameShadow(
                QtWidgets.QFrame.Raised)
                self.BlockforSearchOnTDLProductivity_2.setObjectName(
                "BlockforSearchOnTDLProductivity_2")
                self.horizontalLayout_61 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnTDLProductivity_2)
                self.horizontalLayout_61.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_61.setSpacing(0)
                self.horizontalLayout_61.setObjectName("horizontalLayout_61")
                self.SearchIconOnTDLProductivity_2 = QtWidgets.QLabel(
                self.BlockforSearchOnTDLProductivity_2)
                self.SearchIconOnTDLProductivity_2.setText("")
                self.SearchIconOnTDLProductivity_2.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnTDLProductivity_2.setObjectName(
                "SearchIconOnTDLProductivity_2")
                self.horizontalLayout_61.addWidget(self.SearchIconOnTDLProductivity_2)
                self.FeildForSearchOnTDLProductivity_2 = QtWidgets.QLineEdit(
                self.BlockforSearchOnTDLProductivity_2)
                self.FeildForSearchOnTDLProductivity_2.setStyleSheet("border-radius:5px;\n"
                                                                "background: transparent;")
                self.FeildForSearchOnTDLProductivity_2.setObjectName(
                "FeildForSearchOnTDLProductivity_2")
                self.horizontalLayout_61.addWidget(
                self.FeildForSearchOnTDLProductivity_2)
                self.horizontalLayout_60.addWidget(
                self.BlockforSearchOnTDLProductivity_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_58.addWidget(
                self.SearchBarMiscOnTDLProductivity_2, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnTDLProductivity_2 = QtWidgets.QWidget(
                self.UpperPartOnTDLProductivity_2)
                self.UserButtonMiscOnTDLProductivity_2.setObjectName(
                "UserButtonMiscOnTDLProductivity_2")
                self.horizontalLayout_50 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnTDLProductivity_2)
                self.horizontalLayout_50.setObjectName("horizontalLayout_50")
                self.pushButton_26 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_2)
                self.pushButton_26.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_26.setText("")
                self.pushButton_26.setIcon(icon17)
                self.pushButton_26.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_26.setObjectName("pushButton_26")
                self.horizontalLayout_50.addWidget(self.pushButton_26)
                self.NotificationIconOnTDLProductivity_2 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_2)
                self.NotificationIconOnTDLProductivity_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                                "border-radius:5px;\n"
                                                                "background-color: #2596be;\n"
                                                                "padding:15px;\n"
                                                                "\n"
                                                                "}\n"
                                                                "")
                self.NotificationIconOnTDLProductivity_2.setText("")
                self.NotificationIconOnTDLProductivity_2.setIcon(icon18)
                self.NotificationIconOnTDLProductivity_2.setIconSize(
                QtCore.QSize(30, 30))
                self.NotificationIconOnTDLProductivity_2.setObjectName(
                "NotificationIconOnTDLProductivity_2")
                self.horizontalLayout_50.addWidget(
                self.NotificationIconOnTDLProductivity_2)
                self.UserIconOnTDLProductivity_2 = QtWidgets.QPushButton(
                self.UserButtonMiscOnTDLProductivity_2)
                self.UserIconOnTDLProductivity_2.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnTDLProductivity_2.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.UserIconOnTDLProductivity_2.setText("")
                self.UserIconOnTDLProductivity_2.setIcon(icon11)
                self.UserIconOnTDLProductivity_2.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnTDLProductivity_2.setObjectName(
                "UserIconOnTDLProductivity_2")
                self.horizontalLayout_50.addWidget(self.UserIconOnTDLProductivity_2)
                self.horizontalLayout_58.addWidget(
                self.UserButtonMiscOnTDLProductivity_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_26.addWidget(self.UpperPartOnTDLProductivity_2)
                self.widget_49 = QtWidgets.QWidget(self.EvaluationPage)
                self.widget_49.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_49.setObjectName("widget_49")
                self.verticalLayout_80 = QtWidgets.QVBoxLayout(self.widget_49)
                self.verticalLayout_80.setObjectName("verticalLayout_80")
                self.MessageOnEvaluation = QtWidgets.QLabel(self.widget_49)
                self.MessageOnEvaluation.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnEvaluation.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnEvaluation.setObjectName("MessageOnEvaluation")
                self.verticalLayout_80.addWidget(self.MessageOnEvaluation)
                self.verticalLayout_26.addWidget(self.widget_49)
                self.widget_50 = QtWidgets.QWidget(self.EvaluationPage)
                self.widget_50.setObjectName("widget_50")
                self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.widget_50)
                self.verticalLayout_81.setObjectName("verticalLayout_81")
                self.label_97 = QtWidgets.QLabel(self.widget_50)
                self.label_97.setObjectName("label_97")
                self.verticalLayout_81.addWidget(self.label_97)
                self.comboBox = QtWidgets.QComboBox(self.widget_50)
                self.comboBox.setStyleSheet("border: 2px solid grey; \n"
                                        " border-radius:5px;\n"
                                        " padding:5px")
                self.comboBox.setObjectName("comboBox")
                self.verticalLayout_81.addWidget(self.comboBox)
                self.verticalLayout_26.addWidget(self.widget_50)
                self.frameforUserMenu_18 = QtWidgets.QWidget(self.EvaluationPage)
                self.frameforUserMenu_18.setObjectName("frameforUserMenu_18")
                self.horizontalLayout_115 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_18)
                self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_115.setSpacing(0)
                self.horizontalLayout_115.setObjectName("horizontalLayout_115")
                self.UserMenuOnDashboard_4 = QtWidgets.QWidget(
                self.frameforUserMenu_18)
                self.UserMenuOnDashboard_4.setEnabled(False)
                self.UserMenuOnDashboard_4.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnDashboard_4.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnDashboard_4.setStyleSheet("background-color:white;\n"
                                                        " border-radius:10px;")
                self.UserMenuOnDashboard_4.setObjectName("UserMenuOnDashboard_4")
                self.verticalLayout_65 = QtWidgets.QVBoxLayout(
                self.UserMenuOnDashboard_4)
                self.verticalLayout_65.setObjectName("verticalLayout_65")
                self.label_151 = QtWidgets.QLabel(self.UserMenuOnDashboard_4)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_151.setFont(font)
                self.label_151.setStyleSheet("color: #2596be;")
                self.label_151.setObjectName("label_151")
                self.verticalLayout_65.addWidget(
                self.label_151, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_99 = QtWidgets.QPushButton(self.UserMenuOnDashboard_4)
                self.pushButton_99.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_99.setText("")
                self.pushButton_99.setIcon(icon19)
                self.pushButton_99.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_99.setObjectName("pushButton_99")
                self.verticalLayout_65.addWidget(
                self.pushButton_99, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_100 = QtWidgets.QPushButton(self.UserMenuOnDashboard_4)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_100.setFont(font)
                self.pushButton_100.setIcon(icon11)
                self.pushButton_100.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_100.setObjectName("pushButton_100")
                self.verticalLayout_65.addWidget(
                self.pushButton_100, 0, QtCore.Qt.AlignLeft)
                self.pushButton_101 = QtWidgets.QPushButton(self.UserMenuOnDashboard_4)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_101.setFont(font)
                self.pushButton_101.setIcon(icon20)
                self.pushButton_101.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_101.setObjectName("pushButton_101")
                self.verticalLayout_65.addWidget(
                self.pushButton_101, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_115.addWidget(self.UserMenuOnDashboard_4)
                self.verticalLayout_26.addWidget(
                self.frameforUserMenu_18, 0, QtCore.Qt.AlignRight)
                self.ContentOnEvaluatePage = QtWidgets.QWidget(self.EvaluationPage)
                self.ContentOnEvaluatePage.setStyleSheet(
                "QLineEdit{border:2px solid black; border-radius: 5px;}")
                self.ContentOnEvaluatePage.setObjectName("ContentOnEvaluatePage")
                self.gridLayout_4 = QtWidgets.QGridLayout(self.ContentOnEvaluatePage)
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.label_61 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_61.setMinimumSize(QtCore.QSize(200, 0))
                self.label_61.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_61.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_61.setAlignment(QtCore.Qt.AlignCenter)
                self.label_61.setObjectName("label_61")
                self.gridLayout_4.addWidget(self.label_61, 4, 0, 1, 1)
                self.lineEdit_6 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_6.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_6.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.gridLayout_4.addWidget(self.lineEdit_6, 3, 1, 1, 1)
                self.label_62 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_62.setMinimumSize(QtCore.QSize(200, 0))
                self.label_62.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_62.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_62.setAlignment(QtCore.Qt.AlignCenter)
                self.label_62.setObjectName("label_62")
                self.gridLayout_4.addWidget(self.label_62, 5, 0, 1, 1)
                self.label_63 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_63.setMinimumSize(QtCore.QSize(200, 0))
                self.label_63.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_63.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_63.setAlignment(QtCore.Qt.AlignCenter)
                self.label_63.setObjectName("label_63")
                self.gridLayout_4.addWidget(self.label_63, 6, 0, 1, 1)
                self.lineEdit_8 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_8.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_8.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_8.setObjectName("lineEdit_8")
                self.gridLayout_4.addWidget(self.lineEdit_8, 5, 1, 1, 1)
                self.lineEdit_7 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_7.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_7.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_7.setObjectName("lineEdit_7")
                self.gridLayout_4.addWidget(self.lineEdit_7, 4, 1, 1, 1)
                self.lineEdit_9 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_9.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_9.setObjectName("lineEdit_9")
                self.gridLayout_4.addWidget(self.lineEdit_9, 6, 1, 1, 1)
                self.label_64 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_64.setMinimumSize(QtCore.QSize(200, 0))
                self.label_64.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_64.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_64.setAlignment(QtCore.Qt.AlignCenter)
                self.label_64.setObjectName("label_64")
                self.gridLayout_4.addWidget(self.label_64, 7, 0, 1, 1)
                self.lineEdit_4 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_4.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_4.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_4.setStyleSheet("")
                self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.gridLayout_4.addWidget(self.lineEdit_4, 1, 1, 1, 1)
                self.label_58 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_58.setMinimumSize(QtCore.QSize(200, 0))
                self.label_58.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_58.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_58.setAlignment(QtCore.Qt.AlignCenter)
                self.label_58.setObjectName("label_58")
                self.gridLayout_4.addWidget(self.label_58, 2, 0, 1, 1)
                self.lineEdit_5 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_5.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_5.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_5.setStyleSheet("")
                self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.gridLayout_4.addWidget(self.lineEdit_5, 2, 1, 1, 1)
                self.label_60 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_60.setMinimumSize(QtCore.QSize(200, 0))
                self.label_60.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_60.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_60.setAlignment(QtCore.Qt.AlignCenter)
                self.label_60.setObjectName("label_60")
                self.gridLayout_4.addWidget(self.label_60, 3, 0, 1, 1)
                self.label_65 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_65.setMinimumSize(QtCore.QSize(200, 0))
                self.label_65.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_65.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setObjectName("label_65")
                self.gridLayout_4.addWidget(self.label_65, 8, 0, 1, 1)
                self.lineEdit_10 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_10.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_10.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_10.setObjectName("lineEdit_10")
                self.gridLayout_4.addWidget(self.lineEdit_10, 7, 1, 1, 1)
                self.label_66 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_66.setMinimumSize(QtCore.QSize(200, 0))
                self.label_66.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_66.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_66.setAlignment(QtCore.Qt.AlignCenter)
                self.label_66.setObjectName("label_66")
                self.gridLayout_4.addWidget(self.label_66, 9, 0, 1, 1)
                self.lineEdit_11 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_11.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_11.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_11.setObjectName("lineEdit_11")
                self.gridLayout_4.addWidget(self.lineEdit_11, 8, 1, 1, 1)
                self.lineEdit_12 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_12.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_12.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_12.setObjectName("lineEdit_12")
                self.gridLayout_4.addWidget(self.lineEdit_12, 9, 1, 1, 1)
                self.label_67 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_67.setMinimumSize(QtCore.QSize(200, 0))
                self.label_67.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_67.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_67.setAlignment(QtCore.Qt.AlignCenter)
                self.label_67.setObjectName("label_67")
                self.gridLayout_4.addWidget(self.label_67, 10, 0, 1, 1)
                self.label_57 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_57.setMinimumSize(QtCore.QSize(200, 0))
                self.label_57.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_57.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_57.setAlignment(QtCore.Qt.AlignCenter)
                self.label_57.setObjectName("label_57")
                self.gridLayout_4.addWidget(self.label_57, 1, 0, 1, 1)
                self.lineEdit_13 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_13.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_13.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_13.setObjectName("lineEdit_13")
                self.gridLayout_4.addWidget(self.lineEdit_13, 10, 1, 1, 1)
                self.lineEdit_3 = QtWidgets.QLineEdit(self.ContentOnEvaluatePage)
                self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 0))
                self.lineEdit_3.setMaximumSize(QtCore.QSize(50, 16777215))
                self.lineEdit_3.setStyleSheet("")
                self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.gridLayout_4.addWidget(self.lineEdit_3, 0, 1, 1, 1)
                self.label_56 = QtWidgets.QLabel(self.ContentOnEvaluatePage)
                self.label_56.setMinimumSize(QtCore.QSize(200, 0))
                self.label_56.setMaximumSize(QtCore.QSize(0, 16777215))
                self.label_56.setStyleSheet(
                "border-radius:10px; border: 2px solid lightblue; border-left: 0px; border-radius: 10px; padding: 10px;")
                self.label_56.setAlignment(QtCore.Qt.AlignCenter)
                self.label_56.setObjectName("label_56")
                self.gridLayout_4.addWidget(self.label_56, 0, 0, 1, 1)
                self.verticalLayout_26.addWidget(self.ContentOnEvaluatePage)
                self.widget_51 = QtWidgets.QWidget(self.EvaluationPage)
                self.widget_51.setObjectName("widget_51")
                self.verticalLayout_82 = QtWidgets.QVBoxLayout(self.widget_51)
                self.verticalLayout_82.setObjectName("verticalLayout_82")
                self.pushButton_23 = QtWidgets.QPushButton(self.widget_51)
                self.pushButton_23.setStyleSheet("#pushButton_23{\n"
                                                "color: white;\n"
                                                "padding: 10px;\n"
                                                "background-color: pink;}\n"
                                                "#pushButton_23:hover{\n"
                                                "color: white;\n"
                                                "padding: 5px;\n"
                                                "background-color: lightblue;}")
                self.pushButton_23.setObjectName("pushButton_23")
                self.verticalLayout_82.addWidget(self.pushButton_23)
                self.verticalLayout_26.addWidget(self.widget_51)
                spacerItem21 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_26.addItem(spacerItem21)
                self.RightForm.addWidget(self.EvaluationPage)
                self.ContactUs = QtWidgets.QWidget()
                self.ContactUs.setObjectName("ContactUs")
                self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.ContactUs)
                self.verticalLayout_36.setObjectName("verticalLayout_36")
                self.UpperPartOnContactUs = QtWidgets.QWidget(self.ContactUs)
                self.UpperPartOnContactUs.setStyleSheet("background-color: white;")
                self.UpperPartOnContactUs.setObjectName("UpperPartOnContactUs")
                self.horizontalLayout_80 = QtWidgets.QHBoxLayout(
                self.UpperPartOnContactUs)
                self.horizontalLayout_80.setObjectName("horizontalLayout_80")
                self.MenuButtonMiscOnContactUs = QtWidgets.QWidget(
                self.UpperPartOnContactUs)
                self.MenuButtonMiscOnContactUs.setObjectName(
                "MenuButtonMiscOnContactUs")
                self.horizontalLayout_81 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnContactUs)
                self.horizontalLayout_81.setObjectName("horizontalLayout_81")
                self.MenuButtonOnContactUs = QtWidgets.QPushButton(
                self.MenuButtonMiscOnContactUs)
                self.MenuButtonOnContactUs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnContactUs.setStyleSheet(":hover{\n"
                                                        "background-color: #2596be;\n"
                                                        "}")
                self.MenuButtonOnContactUs.setText("")
                self.MenuButtonOnContactUs.setIcon(icon16)
                self.MenuButtonOnContactUs.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnContactUs.setFlat(True)
                self.MenuButtonOnContactUs.setObjectName("MenuButtonOnContactUs")
                self.horizontalLayout_81.addWidget(self.MenuButtonOnContactUs)
                self.LabelforMenuOnContactUs = QtWidgets.QLabel(
                self.MenuButtonMiscOnContactUs)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnContactUs.setFont(font)
                self.LabelforMenuOnContactUs.setStyleSheet("color : #2596be;\n"
                                                        "font: bold;\n"
                                                        "")
                self.LabelforMenuOnContactUs.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnContactUs.setObjectName("LabelforMenuOnContactUs")
                self.horizontalLayout_81.addWidget(
                self.LabelforMenuOnContactUs, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.horizontalLayout_80.addWidget(
                self.MenuButtonMiscOnContactUs, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnContactUs = QtWidgets.QWidget(
                self.UpperPartOnContactUs)
                self.SearchBarMiscOnContactUs.setObjectName("SearchBarMiscOnContactUs")
                self.horizontalLayout_82 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnContactUs)
                self.horizontalLayout_82.setObjectName("horizontalLayout_82")
                self.BlockforSearchOnContactUs = QtWidgets.QFrame(
                self.SearchBarMiscOnContactUs)
                self.BlockforSearchOnContactUs.setStyleSheet("#BlockforSearchOnContactUs{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                self.BlockforSearchOnContactUs.setFrameShape(
                QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnContactUs.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearchOnContactUs.setObjectName(
                "BlockforSearchOnContactUs")
                self.horizontalLayout_83 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnContactUs)
                self.horizontalLayout_83.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_83.setSpacing(0)
                self.horizontalLayout_83.setObjectName("horizontalLayout_83")
                self.SearchIconOnContactUs = QtWidgets.QLabel(
                self.BlockforSearchOnContactUs)
                self.SearchIconOnContactUs.setText("")
                self.SearchIconOnContactUs.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnContactUs.setObjectName("SearchIconOnContactUs")
                self.horizontalLayout_83.addWidget(self.SearchIconOnContactUs)
                self.FeildForSearchOnContactUs = QtWidgets.QLineEdit(
                self.BlockforSearchOnContactUs)
                self.FeildForSearchOnContactUs.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                self.FeildForSearchOnContactUs.setObjectName(
                "FeildForSearchOnContactUs")
                self.horizontalLayout_83.addWidget(self.FeildForSearchOnContactUs)
                self.horizontalLayout_82.addWidget(
                self.BlockforSearchOnContactUs, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_80.addWidget(
                self.SearchBarMiscOnContactUs, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnContactUs = QtWidgets.QWidget(
                self.UpperPartOnContactUs)
                self.UserButtonMiscOnContactUs.setObjectName(
                "UserButtonMiscOnContactUs")
                self.horizontalLayout_51 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnContactUs)
                self.horizontalLayout_51.setObjectName("horizontalLayout_51")
                self.pushButton_27 = QtWidgets.QPushButton(
                self.UserButtonMiscOnContactUs)
                self.pushButton_27.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_27.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_27.setText("")
                self.pushButton_27.setIcon(icon17)
                self.pushButton_27.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_27.setObjectName("pushButton_27")
                self.horizontalLayout_51.addWidget(self.pushButton_27)
                self.NotificationIconOnContactUs = QtWidgets.QPushButton(
                self.UserButtonMiscOnContactUs)
                self.NotificationIconOnContactUs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnContactUs.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconOnContactUs.setText("")
                self.NotificationIconOnContactUs.setIcon(icon18)
                self.NotificationIconOnContactUs.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnContactUs.setObjectName(
                "NotificationIconOnContactUs")
                self.horizontalLayout_51.addWidget(self.NotificationIconOnContactUs)
                self.UserIconOnContactUs = QtWidgets.QPushButton(
                self.UserButtonMiscOnContactUs)
                self.UserIconOnContactUs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnContactUs.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.UserIconOnContactUs.setText("")
                self.UserIconOnContactUs.setIcon(icon11)
                self.UserIconOnContactUs.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnContactUs.setObjectName("UserIconOnContactUs")
                self.horizontalLayout_51.addWidget(self.UserIconOnContactUs)
                self.horizontalLayout_80.addWidget(
                self.UserButtonMiscOnContactUs, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_36.addWidget(self.UpperPartOnContactUs)
                self.widget_47 = QtWidgets.QWidget(self.ContactUs)
                self.widget_47.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_47.setObjectName("widget_47")
                self.verticalLayout_78 = QtWidgets.QVBoxLayout(self.widget_47)
                self.verticalLayout_78.setObjectName("verticalLayout_78")
                self.MessageOnContactUs = QtWidgets.QLabel(self.widget_47)
                self.MessageOnContactUs.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnContactUs.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnContactUs.setObjectName("MessageOnContactUs")
                self.verticalLayout_78.addWidget(self.MessageOnContactUs)
                self.verticalLayout_36.addWidget(self.widget_47)
                self.frameforUserMenu_15 = QtWidgets.QWidget(self.ContactUs)
                self.frameforUserMenu_15.setObjectName("frameforUserMenu_15")
                self.horizontalLayout_105 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_15)
                self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_105.setSpacing(0)
                self.horizontalLayout_105.setObjectName("horizontalLayout_105")
                self.UserMenuOnContactUs = QtWidgets.QWidget(self.frameforUserMenu_15)
                self.UserMenuOnContactUs.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnContactUs.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnContactUs.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                self.UserMenuOnContactUs.setObjectName("UserMenuOnContactUs")
                self.verticalLayout_57 = QtWidgets.QVBoxLayout(
                self.UserMenuOnContactUs)
                self.verticalLayout_57.setObjectName("verticalLayout_57")
                self.label_148 = QtWidgets.QLabel(self.UserMenuOnContactUs)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_148.setFont(font)
                self.label_148.setStyleSheet("color: #2596be;")
                self.label_148.setObjectName("label_148")
                self.verticalLayout_57.addWidget(
                self.label_148, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_90 = QtWidgets.QPushButton(self.UserMenuOnContactUs)
                self.pushButton_90.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_90.setText("")
                self.pushButton_90.setIcon(icon19)
                self.pushButton_90.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_90.setObjectName("pushButton_90")
                self.verticalLayout_57.addWidget(self.pushButton_90)
                self.pushButton_91 = QtWidgets.QPushButton(self.UserMenuOnContactUs)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_91.setFont(font)
                self.pushButton_91.setIcon(icon11)
                self.pushButton_91.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_91.setObjectName("pushButton_91")
                self.verticalLayout_57.addWidget(
                self.pushButton_91, 0, QtCore.Qt.AlignLeft)
                self.pushButton_92 = QtWidgets.QPushButton(self.UserMenuOnContactUs)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_92.setFont(font)
                self.pushButton_92.setIcon(icon20)
                self.pushButton_92.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_92.setObjectName("pushButton_92")
                self.verticalLayout_57.addWidget(
                self.pushButton_92, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_105.addWidget(self.UserMenuOnContactUs)
                self.verticalLayout_36.addWidget(
                self.frameforUserMenu_15, 0, QtCore.Qt.AlignRight)
                self.ContentOnContactUs = QtWidgets.QWidget(self.ContactUs)
                self.ContentOnContactUs.setStyleSheet("background-color: lightgrey;\n"
                                                "border-radius: 15px;")
                self.ContentOnContactUs.setObjectName("ContentOnContactUs")
                self.horizontalLayout_85 = QtWidgets.QHBoxLayout(
                self.ContentOnContactUs)
                self.horizontalLayout_85.setObjectName("horizontalLayout_85")
                self.widget_31 = QtWidgets.QWidget(self.ContentOnContactUs)
                self.widget_31.setStyleSheet("")
                self.widget_31.setObjectName("widget_31")
                self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.widget_31)
                self.verticalLayout_37.setObjectName("verticalLayout_37")
                self.pushButton_41 = QtWidgets.QPushButton(self.widget_31)
                self.pushButton_41.setText("")
                icon21 = QtGui.QIcon()
                icon21.addPixmap(QtGui.QPixmap(":/Icons/Icons/compass.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_41.setIcon(icon21)
                self.pushButton_41.setIconSize(QtCore.QSize(64, 64))
                self.pushButton_41.setFlat(True)
                self.pushButton_41.setObjectName("pushButton_41")
                self.verticalLayout_37.addWidget(self.pushButton_41)
                self.label_126 = QtWidgets.QLabel(self.widget_31)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_126.setFont(font)
                self.label_126.setObjectName("label_126")
                self.verticalLayout_37.addWidget(
                self.label_126, 0, QtCore.Qt.AlignHCenter)
                self.label_127 = QtWidgets.QLabel(self.widget_31)
                font = QtGui.QFont()
                font.setPointSize(8)
                self.label_127.setFont(font)
                self.label_127.setObjectName("label_127")
                self.verticalLayout_37.addWidget(
                self.label_127, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.widget_33 = QtWidgets.QWidget(self.widget_31)
                self.widget_33.setObjectName("widget_33")
                self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.widget_33)
                self.verticalLayout_38.setObjectName("verticalLayout_38")
                self.pushButton_42 = QtWidgets.QPushButton(self.widget_33)
                self.pushButton_42.setText("")
                self.pushButton_42.setIcon(icon13)
                self.pushButton_42.setIconSize(QtCore.QSize(64, 64))
                self.pushButton_42.setFlat(True)
                self.pushButton_42.setObjectName("pushButton_42")
                self.verticalLayout_38.addWidget(self.pushButton_42)
                self.label_125 = QtWidgets.QLabel(self.widget_33)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_125.setFont(font)
                self.label_125.setObjectName("label_125")
                self.verticalLayout_38.addWidget(
                self.label_125, 0, QtCore.Qt.AlignHCenter)
                self.label_128 = QtWidgets.QLabel(self.widget_33)
                self.label_128.setObjectName("label_128")
                self.verticalLayout_38.addWidget(
                self.label_128, 0, QtCore.Qt.AlignHCenter)
                self.label_129 = QtWidgets.QLabel(self.widget_33)
                self.label_129.setObjectName("label_129")
                self.verticalLayout_38.addWidget(
                self.label_129, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_37.addWidget(self.widget_33)
                self.widget_34 = QtWidgets.QWidget(self.widget_31)
                self.widget_34.setObjectName("widget_34")
                self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.widget_34)
                self.verticalLayout_39.setObjectName("verticalLayout_39")
                self.pushButton_43 = QtWidgets.QPushButton(self.widget_34)
                self.pushButton_43.setText("")
                icon22 = QtGui.QIcon()
                icon22.addPixmap(QtGui.QPixmap(":/Icons/Icons/mail.svg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_43.setIcon(icon22)
                self.pushButton_43.setIconSize(QtCore.QSize(64, 64))
                self.pushButton_43.setFlat(True)
                self.pushButton_43.setObjectName("pushButton_43")
                self.verticalLayout_39.addWidget(self.pushButton_43)
                self.label_130 = QtWidgets.QLabel(self.widget_34)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_130.setFont(font)
                self.label_130.setObjectName("label_130")
                self.verticalLayout_39.addWidget(
                self.label_130, 0, QtCore.Qt.AlignHCenter)
                self.label_131 = QtWidgets.QLabel(self.widget_34)
                self.label_131.setObjectName("label_131")
                self.verticalLayout_39.addWidget(
                self.label_131, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_37.addWidget(self.widget_34)
                spacerItem22 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_37.addItem(spacerItem22)
                self.horizontalLayout_85.addWidget(
                self.widget_31, 0, QtCore.Qt.AlignLeft)
                self.widget_32 = QtWidgets.QWidget(self.ContentOnContactUs)
                self.widget_32.setStyleSheet("")
                self.widget_32.setObjectName("widget_32")
                self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_32)
                self.verticalLayout_40.setObjectName("verticalLayout_40")
                self.label_132 = QtWidgets.QLabel(self.widget_32)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_132.setFont(font)
                self.label_132.setObjectName("label_132")
                self.verticalLayout_40.addWidget(self.label_132)
                self.label_133 = QtWidgets.QLabel(self.widget_32)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_133.setFont(font)
                self.label_133.setObjectName("label_133")
                self.verticalLayout_40.addWidget(self.label_133)
                self.lineEdit_15 = QtWidgets.QLineEdit(self.widget_32)
                self.lineEdit_15.setStyleSheet("border-radius: 5px;\n"
                                        "border: 2px solid grey;")
                self.lineEdit_15.setObjectName("lineEdit_15")
                self.verticalLayout_40.addWidget(self.lineEdit_15)
                self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_32)
                self.lineEdit_16.setStyleSheet("border-radius: 5px;\n"
                                        "border: 2px solid grey;")
                self.lineEdit_16.setObjectName("lineEdit_16")
                self.verticalLayout_40.addWidget(self.lineEdit_16)
                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_32)
                self.plainTextEdit.setStyleSheet("border-radius: 15px;\n"
                                                "border: 2px solid grey;")
                self.plainTextEdit.setObjectName("plainTextEdit")
                self.verticalLayout_40.addWidget(
                self.plainTextEdit, 0, QtCore.Qt.AlignTop)
                self.pushButton_44 = QtWidgets.QPushButton(self.widget_32)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_44.setFont(font)
                self.pushButton_44.setStyleSheet("background-color: lightblue;\n"
                                                "color: white;\n"
                                                "padding: 10px;")
                self.pushButton_44.setObjectName("pushButton_44")
                self.verticalLayout_40.addWidget(
                self.pushButton_44, 0, QtCore.Qt.AlignLeft)
                spacerItem23 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_40.addItem(spacerItem23)
                self.horizontalLayout_85.addWidget(self.widget_32)
                self.verticalLayout_36.addWidget(self.ContentOnContactUs)
                self.RightForm.addWidget(self.ContactUs)
                self.FAQs = QtWidgets.QWidget()
                self.FAQs.setObjectName("FAQs")
                self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.FAQs)
                self.verticalLayout_41.setObjectName("verticalLayout_41")
                self.UpperPartOnFAQs = QtWidgets.QWidget(self.FAQs)
                self.UpperPartOnFAQs.setStyleSheet("background-color: white;")
                self.UpperPartOnFAQs.setObjectName("UpperPartOnFAQs")
                self.horizontalLayout_86 = QtWidgets.QHBoxLayout(self.UpperPartOnFAQs)
                self.horizontalLayout_86.setObjectName("horizontalLayout_86")
                self.MenuButtonMiscOnFAQs = QtWidgets.QWidget(self.UpperPartOnFAQs)
                self.MenuButtonMiscOnFAQs.setObjectName("MenuButtonMiscOnFAQs")
                self.horizontalLayout_87 = QtWidgets.QHBoxLayout(
                self.MenuButtonMiscOnFAQs)
                self.horizontalLayout_87.setObjectName("horizontalLayout_87")
                self.MenuButtonOnFAQs = QtWidgets.QPushButton(
                self.MenuButtonMiscOnFAQs)
                self.MenuButtonOnFAQs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.MenuButtonOnFAQs.setStyleSheet(":hover{\n"
                                                "background-color: #2596be;\n"
                                                "}")
                self.MenuButtonOnFAQs.setText("")
                self.MenuButtonOnFAQs.setIcon(icon16)
                self.MenuButtonOnFAQs.setIconSize(QtCore.QSize(32, 32))
                self.MenuButtonOnFAQs.setFlat(True)
                self.MenuButtonOnFAQs.setObjectName("MenuButtonOnFAQs")
                self.horizontalLayout_87.addWidget(self.MenuButtonOnFAQs)
                self.LabelforMenuOnFAQs = QtWidgets.QLabel(self.MenuButtonMiscOnFAQs)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.LabelforMenuOnFAQs.setFont(font)
                self.LabelforMenuOnFAQs.setStyleSheet("color : #2596be;\n"
                                                "font: bold;\n"
                                                "")
                self.LabelforMenuOnFAQs.setAlignment(QtCore.Qt.AlignCenter)
                self.LabelforMenuOnFAQs.setObjectName("LabelforMenuOnFAQs")
                self.horizontalLayout_87.addWidget(
                self.LabelforMenuOnFAQs, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.horizontalLayout_86.addWidget(
                self.MenuButtonMiscOnFAQs, 0, QtCore.Qt.AlignLeft)
                self.SearchBarMiscOnFAQs = QtWidgets.QWidget(self.UpperPartOnFAQs)
                self.SearchBarMiscOnFAQs.setObjectName("SearchBarMiscOnFAQs")
                self.horizontalLayout_88 = QtWidgets.QHBoxLayout(
                self.SearchBarMiscOnFAQs)
                self.horizontalLayout_88.setObjectName("horizontalLayout_88")
                self.BlockforSearchOnFAQs = QtWidgets.QFrame(self.SearchBarMiscOnFAQs)
                self.BlockforSearchOnFAQs.setStyleSheet("#BlockforSearchOnFAQs{\n"
                                                        "border: 2px solid lightblue;\n"
                                                        "border-radius: 5px;\n"
                                                        "}\n"
                                                        "")
                self.BlockforSearchOnFAQs.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BlockforSearchOnFAQs.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BlockforSearchOnFAQs.setObjectName("BlockforSearchOnFAQs")
                self.horizontalLayout_89 = QtWidgets.QHBoxLayout(
                self.BlockforSearchOnFAQs)
                self.horizontalLayout_89.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_89.setSpacing(0)
                self.horizontalLayout_89.setObjectName("horizontalLayout_89")
                self.SearchIconOnFAQs = QtWidgets.QLabel(self.BlockforSearchOnFAQs)
                self.SearchIconOnFAQs.setText("")
                self.SearchIconOnFAQs.setPixmap(
                QtGui.QPixmap(":/Icons/Icons/search.svg"))
                self.SearchIconOnFAQs.setObjectName("SearchIconOnFAQs")
                self.horizontalLayout_89.addWidget(self.SearchIconOnFAQs)
                self.FeildForSearchOnFAQs = QtWidgets.QLineEdit(
                self.BlockforSearchOnFAQs)
                self.FeildForSearchOnFAQs.setStyleSheet("border-radius:5px;\n"
                                                        "background: transparent;")
                self.FeildForSearchOnFAQs.setObjectName("FeildForSearchOnFAQs")
                self.horizontalLayout_89.addWidget(self.FeildForSearchOnFAQs)
                self.horizontalLayout_88.addWidget(
                self.BlockforSearchOnFAQs, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.horizontalLayout_86.addWidget(
                self.SearchBarMiscOnFAQs, 0, QtCore.Qt.AlignHCenter)
                self.UserButtonMiscOnFAQs = QtWidgets.QWidget(self.UpperPartOnFAQs)
                self.UserButtonMiscOnFAQs.setObjectName("UserButtonMiscOnFAQs")
                self.horizontalLayout_52 = QtWidgets.QHBoxLayout(
                self.UserButtonMiscOnFAQs)
                self.horizontalLayout_52.setObjectName("horizontalLayout_52")
                self.pushButton_28 = QtWidgets.QPushButton(self.UserButtonMiscOnFAQs)
                self.pushButton_28.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_28.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.pushButton_28.setText("")
                self.pushButton_28.setIcon(icon17)
                self.pushButton_28.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_28.setObjectName("pushButton_28")
                self.horizontalLayout_52.addWidget(self.pushButton_28)
                self.NotificationIconOnFAQs = QtWidgets.QPushButton(
                self.UserButtonMiscOnFAQs)
                self.NotificationIconOnFAQs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.NotificationIconOnFAQs.setStyleSheet(":hover{\n"
                                                        "border-radius:5px;\n"
                                                        "background-color: #2596be;\n"
                                                        "padding:15px;\n"
                                                        "\n"
                                                        "}\n"
                                                        "")
                self.NotificationIconOnFAQs.setText("")
                self.NotificationIconOnFAQs.setIcon(icon18)
                self.NotificationIconOnFAQs.setIconSize(QtCore.QSize(30, 30))
                self.NotificationIconOnFAQs.setObjectName("NotificationIconOnFAQs")
                self.horizontalLayout_52.addWidget(self.NotificationIconOnFAQs)
                self.UserIconOnFAQs = QtWidgets.QPushButton(self.UserButtonMiscOnFAQs)
                self.UserIconOnFAQs.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.UserIconOnFAQs.setStyleSheet(":hover{\n"
                                                "border-radius:5px;\n"
                                                "background-color: #2596be;\n"
                                                "padding:15px;\n"
                                                "\n"
                                                "}\n"
                                                "")
                self.UserIconOnFAQs.setText("")
                self.UserIconOnFAQs.setIcon(icon11)
                self.UserIconOnFAQs.setIconSize(QtCore.QSize(32, 32))
                self.UserIconOnFAQs.setFlat(True)
                self.UserIconOnFAQs.setObjectName("UserIconOnFAQs")
                self.horizontalLayout_52.addWidget(self.UserIconOnFAQs)
                self.horizontalLayout_86.addWidget(
                self.UserButtonMiscOnFAQs, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
                self.verticalLayout_41.addWidget(self.UpperPartOnFAQs)
                self.widget_48 = QtWidgets.QWidget(self.FAQs)
                self.widget_48.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_48.setObjectName("widget_48")
                self.verticalLayout_79 = QtWidgets.QVBoxLayout(self.widget_48)
                self.verticalLayout_79.setObjectName("verticalLayout_79")
                self.MessageOnFAQs = QtWidgets.QLabel(self.widget_48)
                self.MessageOnFAQs.setMaximumSize(QtCore.QSize(16777215, 0))
                self.MessageOnFAQs.setStyleSheet(
                "background-color: lightgreen; padding: 10px;")
                self.MessageOnFAQs.setObjectName("MessageOnFAQs")
                self.verticalLayout_79.addWidget(self.MessageOnFAQs)
                self.verticalLayout_41.addWidget(self.widget_48)
                self.frameforUserMenu_16 = QtWidgets.QWidget(self.FAQs)
                self.frameforUserMenu_16.setObjectName("frameforUserMenu_16")
                self.horizontalLayout_106 = QtWidgets.QHBoxLayout(
                self.frameforUserMenu_16)
                self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_106.setSpacing(0)
                self.horizontalLayout_106.setObjectName("horizontalLayout_106")
                self.UserMenuOnFAQs = QtWidgets.QWidget(self.frameforUserMenu_16)
                self.UserMenuOnFAQs.setMinimumSize(QtCore.QSize(0, 0))
                self.UserMenuOnFAQs.setMaximumSize(QtCore.QSize(120, 0))
                self.UserMenuOnFAQs.setStyleSheet("background-color:white;\n"
                                                " border-radius:10px;")
                self.UserMenuOnFAQs.setObjectName("UserMenuOnFAQs")
                self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.UserMenuOnFAQs)
                self.verticalLayout_58.setObjectName("verticalLayout_58")
                self.label_149 = QtWidgets.QLabel(self.UserMenuOnFAQs)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_149.setFont(font)
                self.label_149.setStyleSheet("color: #2596be;")
                self.label_149.setObjectName("label_149")
                self.verticalLayout_58.addWidget(
                self.label_149, 0, QtCore.Qt.AlignHCenter)
                self.pushButton_93 = QtWidgets.QPushButton(self.UserMenuOnFAQs)
                self.pushButton_93.setStyleSheet("color:white;\n"
                                                " background-color:white;")
                self.pushButton_93.setText("")
                self.pushButton_93.setIcon(icon19)
                self.pushButton_93.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_93.setObjectName("pushButton_93")
                self.verticalLayout_58.addWidget(self.pushButton_93)
                self.pushButton_94 = QtWidgets.QPushButton(self.UserMenuOnFAQs)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_94.setFont(font)
                self.pushButton_94.setIcon(icon11)
                self.pushButton_94.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_94.setObjectName("pushButton_94")
                self.verticalLayout_58.addWidget(
                self.pushButton_94, 0, QtCore.Qt.AlignLeft)
                self.pushButton_95 = QtWidgets.QPushButton(self.UserMenuOnFAQs)
                font = QtGui.QFont()
                font.setFamily("Nirmala UI Semilight")
                font.setPointSize(8)
                self.pushButton_95.setFont(font)
                self.pushButton_95.setIcon(icon20)
                self.pushButton_95.setIconSize(QtCore.QSize(32, 32))
                self.pushButton_95.setObjectName("pushButton_95")
                self.verticalLayout_58.addWidget(
                self.pushButton_95, 0, QtCore.Qt.AlignLeft)
                self.horizontalLayout_106.addWidget(self.UserMenuOnFAQs)
                self.verticalLayout_41.addWidget(
                self.frameforUserMenu_16, 0, QtCore.Qt.AlignRight)
                self.ContentOnFAQs = QtWidgets.QWidget(self.FAQs)
                self.ContentOnFAQs.setStyleSheet("")
                self.ContentOnFAQs.setObjectName("ContentOnFAQs")
                self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.ContentOnFAQs)
                self.verticalLayout_43.setObjectName("verticalLayout_43")
                self.pushButton_2 = QtWidgets.QPushButton(self.ContentOnFAQs)
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(14)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                self.pushButton_2.setObjectName("pushButton_2")
                self.verticalLayout_43.addWidget(self.pushButton_2)
                self.label_3 = QtWidgets.QLabel(self.ContentOnFAQs)
                self.label_3.setStyleSheet(
                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                self.label_3.setObjectName("label_3")
                self.verticalLayout_43.addWidget(self.label_3)
                self.pushButton_3 = QtWidgets.QPushButton(self.ContentOnFAQs)
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(14)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                self.pushButton_3.setObjectName("pushButton_3")
                self.verticalLayout_43.addWidget(self.pushButton_3)
                self.label_6 = QtWidgets.QLabel(self.ContentOnFAQs)
                self.label_6.setStyleSheet(
                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                self.label_6.setObjectName("label_6")
                self.verticalLayout_43.addWidget(self.label_6)
                self.pushButton_4 = QtWidgets.QPushButton(self.ContentOnFAQs)
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(14)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                self.pushButton_4.setObjectName("pushButton_4")
                self.verticalLayout_43.addWidget(self.pushButton_4)
                self.label_7 = QtWidgets.QLabel(self.ContentOnFAQs)
                self.label_7.setStyleSheet(
                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                self.label_7.setObjectName("label_7")
                self.verticalLayout_43.addWidget(self.label_7)
                self.pushButton_5 = QtWidgets.QPushButton(self.ContentOnFAQs)
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(14)
                self.pushButton_5.setFont(font)
                self.pushButton_5.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                self.pushButton_5.setObjectName("pushButton_5")
                self.verticalLayout_43.addWidget(self.pushButton_5)
                self.label_38 = QtWidgets.QLabel(self.ContentOnFAQs)
                self.label_38.setStyleSheet(
                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                self.label_38.setObjectName("label_38")
                self.verticalLayout_43.addWidget(self.label_38)
                self.pushButton_6 = QtWidgets.QPushButton(self.ContentOnFAQs)
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(14)
                self.pushButton_6.setFont(font)
                self.pushButton_6.setStyleSheet("background-color:lightblue; \n"
                                                " border-bottom: 2px solid grey;\n"
                                                " padding:10px;")
                self.pushButton_6.setObjectName("pushButton_6")
                self.verticalLayout_43.addWidget(self.pushButton_6)
                self.label_39 = QtWidgets.QLabel(self.ContentOnFAQs)
                self.label_39.setStyleSheet(
                "background-color: lightgrey; border-radius: 15px; padding:10px;")
                self.label_39.setObjectName("label_39")
                self.verticalLayout_43.addWidget(self.label_39)
                spacerItem24 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_43.addItem(spacerItem24)
                self.verticalLayout_41.addWidget(self.ContentOnFAQs)
                self.RightForm.addWidget(self.FAQs)
                self.horizontalLayout.addWidget(self.RightForm)
                self.NotificationBoard = QtWidgets.QWidget(self.widget_2)
                self.NotificationBoard.setObjectName("NotificationBoard")
                self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.NotificationBoard)
                self.verticalLayout_35.setContentsMargins(9, 0, 0, 0)
                self.verticalLayout_35.setSpacing(0)
                self.verticalLayout_35.setObjectName("verticalLayout_35")
                self.widget_9 = QtWidgets.QWidget(self.NotificationBoard)
                self.widget_9.setMaximumSize(QtCore.QSize(0, 0))
                self.widget_9.setStyleSheet("background-color:lightgreen;")
                self.widget_9.setObjectName("widget_9")
                self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_9)
                self.verticalLayout_17.setObjectName("verticalLayout_17")
                self.label_45 = QtWidgets.QLabel(self.widget_9)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_45.setFont(font)
                self.label_45.setObjectName("label_45")
                self.verticalLayout_17.addWidget(
                self.label_45, 0, QtCore.Qt.AlignHCenter)
                self.widget_14 = QtWidgets.QWidget(self.widget_9)
                self.widget_14.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                self.widget_14.setObjectName("widget_14")
                self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_14)
                self.verticalLayout_18.setObjectName("verticalLayout_18")
                self.label_47 = QtWidgets.QLabel(self.widget_14)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_47.setFont(font)
                self.label_47.setStyleSheet("")
                self.label_47.setAlignment(QtCore.Qt.AlignCenter)
                self.label_47.setObjectName("label_47")
                self.verticalLayout_18.addWidget(self.label_47)
                self.widget_15 = QtWidgets.QWidget(self.widget_14)
                self.widget_15.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                self.widget_15.setObjectName("widget_15")
                self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_15)
                self.verticalLayout_19.setObjectName("verticalLayout_19")
                self.label_48 = QtWidgets.QLabel(self.widget_15)
                self.label_48.setObjectName("label_48")
                self.verticalLayout_19.addWidget(self.label_48)
                self.verticalLayout_18.addWidget(self.widget_15)
                self.verticalLayout_17.addWidget(self.widget_14)
                self.widget_17 = QtWidgets.QWidget(self.widget_9)
                self.widget_17.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                self.widget_17.setObjectName("widget_17")
                self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_17)
                self.verticalLayout_20.setObjectName("verticalLayout_20")
                self.label_49 = QtWidgets.QLabel(self.widget_17)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_49.setFont(font)
                self.label_49.setStyleSheet("")
                self.label_49.setAlignment(QtCore.Qt.AlignCenter)
                self.label_49.setObjectName("label_49")
                self.verticalLayout_20.addWidget(self.label_49)
                self.widget_18 = QtWidgets.QWidget(self.widget_17)
                self.widget_18.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                self.widget_18.setObjectName("widget_18")
                self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_18)
                self.verticalLayout_21.setObjectName("verticalLayout_21")
                self.label_50 = QtWidgets.QLabel(self.widget_18)
                self.label_50.setObjectName("label_50")
                self.verticalLayout_21.addWidget(
                self.label_50, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_20.addWidget(self.widget_18)
                self.verticalLayout_17.addWidget(self.widget_17)
                self.widget_27 = QtWidgets.QWidget(self.widget_9)
                self.widget_27.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                self.widget_27.setObjectName("widget_27")
                self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_27)
                self.verticalLayout_22.setObjectName("verticalLayout_22")
                self.label_51 = QtWidgets.QLabel(self.widget_27)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_51.setFont(font)
                self.label_51.setStyleSheet("")
                self.label_51.setAlignment(QtCore.Qt.AlignCenter)
                self.label_51.setObjectName("label_51")
                self.verticalLayout_22.addWidget(self.label_51)
                self.widget_28 = QtWidgets.QWidget(self.widget_27)
                self.widget_28.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                self.widget_28.setObjectName("widget_28")
                self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_28)
                self.verticalLayout_24.setObjectName("verticalLayout_24")
                self.label_52 = QtWidgets.QLabel(self.widget_28)
                self.label_52.setAlignment(QtCore.Qt.AlignCenter)
                self.label_52.setObjectName("label_52")
                self.verticalLayout_24.addWidget(self.label_52)
                self.verticalLayout_22.addWidget(self.widget_28)
                self.verticalLayout_17.addWidget(self.widget_27)
                self.widget_35 = QtWidgets.QWidget(self.widget_9)
                self.widget_35.setStyleSheet("background-color:lightgrey;\n"
                                        " padding:10px;")
                self.widget_35.setObjectName("widget_35")
                self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_35)
                self.verticalLayout_25.setObjectName("verticalLayout_25")
                self.label_53 = QtWidgets.QLabel(self.widget_35)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_53.setFont(font)
                self.label_53.setStyleSheet("")
                self.label_53.setAlignment(QtCore.Qt.AlignCenter)
                self.label_53.setObjectName("label_53")
                self.verticalLayout_25.addWidget(self.label_53)
                self.widget_36 = QtWidgets.QWidget(self.widget_35)
                self.widget_36.setStyleSheet("background-color:white; \n"
                                        " padding:10px;")
                self.widget_36.setObjectName("widget_36")
                self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.widget_36)
                self.verticalLayout_31.setObjectName("verticalLayout_31")
                self.label_54 = QtWidgets.QLabel(self.widget_36)
                self.label_54.setObjectName("label_54")
                self.verticalLayout_31.addWidget(self.label_54)
                self.verticalLayout_25.addWidget(self.widget_36)
                self.verticalLayout_17.addWidget(self.widget_35)
                spacerItem25 = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_17.addItem(spacerItem25)
                self.verticalLayout_35.addWidget(self.widget_9)
                self.horizontalLayout.addWidget(self.NotificationBoard)
                self.verticalLayout.addWidget(self.widget_2)
                self.label_37 = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.label_37.setFont(font)
                self.label_37.setStyleSheet("padding: 10px; color: lightblue")
                self.label_37.setAlignment(QtCore.Qt.AlignCenter)
                self.label_37.setObjectName("label_37")
                self.verticalLayout.addWidget(self.label_37)
                self.MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi()
                self.RightForm.setCurrentIndex(15)
                QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.MainWindow.setWindowTitle(_translate("self.MainWindow", "self.MainWindow"))
                self.LabelForMenu.setText(_translate("self.MainWindow", "MENU"))
                self.DashboardBtn.setText(_translate("self.MainWindow", "Dashboard"))
                self.UpdateRecievedTaskBtn.setText(
                _translate("self.MainWindow", "Recieved Task"))
                self.WriterProgressBtn.setText(_translate("self.MainWindow", "Team Report"))
                self.PermanentReportBtn.setText(
                _translate("self.MainWindow", "Permanent Report"))
                self.TaskApprovedBtn.setText(
                _translate("self.MainWindow", "Task Available"))
                self.TaskAssignedBtn.setText(_translate("self.MainWindow", "Task Assigned"))
                self.AssignTaskBtn.setText(_translate("self.MainWindow", "Assign Task"))
                self.WordCountReport.setText(_translate(
                "self.MainWindow", "Update Custom Task"))
                self.UpdateDesignationBtn.setText(
                _translate("self.MainWindow", "Update Designation"))
                self.ManageLeavesBtn.setText(_translate("self.MainWindow", "Manage Leaves"))
                self.ProfileBtn.setText(_translate("self.MainWindow", "Profile"))
                self.TDLBtn.setText(_translate("self.MainWindow", "TDL / Productivity"))
                self.ManageTeamLeavesBtn.setText(
                _translate("self.MainWindow", "Manage Team Leaves"))
                self.ManageExpensesBtn.setText(
                _translate("self.MainWindow", "Evaluation Form"))
                self.ContactUsBtn.setText(_translate("self.MainWindow", "Contact Us"))
                self.FAQsBtn.setText(_translate("self.MainWindow", "FAQs"))
                self.PageNameOnDashboard.setText(_translate("self.MainWindow", "Dashboard"))
                self.FeildForSearch.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.label_82.setText(_translate("self.MainWindow", "Message On Dashboard"))
                self.label_135.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_52.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_53.setText(_translate("self.MainWindow", "Log Out"))
                self.Card1ValueString.setText(_translate("self.MainWindow", "New Members"))
                self.Card1Value.setText(_translate(
                "self.MainWindow", "New Members Added Value here"))
                self.CardV2Value.setText(_translate(
                "self.MainWindow", "Total Assignments Completed"))
                self.Card2ValueString.setText(
                _translate("self.MainWindow", "Total Assignments"))
                self.label_40.setText(_translate(
                "self.MainWindow", "Evaluation Points gained:"))
                self.label_41.setText(_translate("self.MainWindow", "35.25"))
                self.label_42.setText(_translate("self.MainWindow", "/36"))
                self.label_44.setText(_translate("self.MainWindow", "Name:"))
                self.pushButton_12.setText(_translate("self.MainWindow", "Download Report"))
                self.label_10.setText(_translate("self.MainWindow", "Random Name"))
                self.label_9.setText(_translate("self.MainWindow", "Team Name:"))
                self.label_43.setText(_translate("self.MainWindow", "Team Name Here"))
                self.label_8.setText(_translate("self.MainWindow", "Your Team"))
                item = self.tableWidget_2.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Name"))
                item = self.tableWidget_2.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Jobe Role"))
                item = self.tableWidget_2.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Status"))
                self.PageNameOnDashboard_2.setText(
                _translate("self.MainWindow", "Team Report"))
                self.FeildForSearch_2.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.label_83.setText(_translate(
                "self.MainWindow", "Message On Team Report"))
                self.label_137.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_58.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_59.setText(_translate("self.MainWindow", "Log Out"))
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Name"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Total Word Count"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Weekly Word Count"))
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "Monthly Word Count"))
                item = self.tableWidget.horizontalHeaderItem(4)
                item.setText(_translate("self.MainWindow", "Evaluation Points"))
                self.LabelforMenuOnPermanencyReport.setText(
                _translate("self.MainWindow", "Permanency Report"))
                self.FeildForSearchOnPermanencyReport.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.label_84.setText(_translate(
                "self.MainWindow", "Message On Permanency Report"))
                self.label_138.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_61.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_62.setText(_translate("self.MainWindow", "Log Out"))
                self.ContentOnPermanencyReport.setSortingEnabled(True)
                item = self.ContentOnPermanencyReport.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Writer Name"))
                item = self.ContentOnPermanencyReport.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Joining Date"))
                item = self.ContentOnPermanencyReport.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Permanency Date"))
                self.LabelforMenuOnTaskAvailable.setText(
                _translate("self.MainWindow", "Task Available"))
                self.FeildForSearchOnTaskAvailable.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.label_85.setText(_translate(
                "self.MainWindow", "Message On Task Available"))
                self.label_139.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_64.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_65.setText(_translate("self.MainWindow", "Log Out"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Client ID"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Task ID"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Word Count"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "Dead Line"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(4)
                item.setText(_translate("self.MainWindow", "Date"))
                item = self.ContentOnTaskAvailable.horizontalHeaderItem(5)
                item.setText(_translate("self.MainWindow", "Topic"))
                self.LabelforMenuOnTaskAssignedReport.setText(
                _translate("self.MainWindow", "Task Assigning Report "))
                self.FeildForSearchOnTaskAssignedReport.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.label_86.setText(_translate(
                "self.MainWindow", "Message On Task Assigning Report"))
                self.label_141.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_70.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_71.setText(_translate("self.MainWindow", "Log Out"))
                item = self.ContentOnTaskAssignedReport.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Writer Name"))
                item = self.ContentOnTaskAssignedReport.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Task ID"))
                item = self.ContentOnTaskAssignedReport.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Word Count"))
                item = self.ContentOnTaskAssignedReport.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "Topic"))
                self.LabelforMenuOnAsiggningTask.setText(
                _translate("self.MainWindow", "Assign Task"))
                self.FeildForSearchOnAsiggningTask.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnAssigningTask.setText(
                _translate("self.MainWindow", "Message On Assign Task"))
                self.label_140.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_67.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_68.setText(_translate("self.MainWindow", "Log Out"))
                self.label_11.setText(_translate("self.MainWindow", "Task Topic:"))
                self.lineEdit_14.setPlaceholderText(
                _translate("self.MainWindow", "Topic Text here"))
                self.label_12.setText(_translate("self.MainWindow", "Select Team Member:"))
                self.comboBox_2.setItemText(0, _translate(
                "self.MainWindow", "Select Member To Assign"))
                self.label_13.setText(_translate("self.MainWindow", "Add Dead Line:"))
                self.label.setText(_translate("self.MainWindow", "Word Count:"))
                self.lineEdit_17.setPlaceholderText(_translate(
                "self.MainWindow", "Word Counts Required for Task"))
                self.pushButton_7.setText(_translate("self.MainWindow", "Upload File"))
                self.pushButton.setText(_translate("self.MainWindow", "Assign"))
                self.PageNameOnDashboard_4.setText(
                _translate("self.MainWindow", "Recieved Task"))
                self.FeildForSearch_4.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnRecievedTask.setText(_translate(
                "self.MainWindow", "Message On Recieved Task"))
                self.label_144.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_79.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_80.setText(_translate("self.MainWindow", "Log Out"))
                item = self.tableWidget_3.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Task ID"))
                item = self.tableWidget_3.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Required Word Count"))
                item = self.tableWidget_3.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Writer Name"))
                item = self.tableWidget_3.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "Recieved Word Count"))
                item = self.tableWidget_3.horizontalHeaderItem(4)
                item.setText(_translate("self.MainWindow", "Status"))
                self.label_72.setText(_translate("self.MainWindow", "Task Details:"))
                self.label_17.setText(_translate("self.MainWindow", "Task ID:"))
                self.label_18.setText(_translate(
                "self.MainWindow", "Selected Task ID here"))
                self.label_70.setText(_translate("self.MainWindow", "Task Topic:"))
                self.label_68.setText(_translate("self.MainWindow", "Task Topic here"))
                self.label_71.setText(_translate(
                "self.MainWindow", "To Download File Provided by Writer:"))
                self.pushButton_11.setText(_translate("self.MainWindow", "Download File"))
                self.label_69.setText(_translate("self.MainWindow", "Palagrism:"))
                self.pushButton_30.setText(_translate("self.MainWindow", "Update"))
                self.LabelforMenuOnUpdateWork.setText(
                _translate("self.MainWindow", "Update Work"))
                self.FeildForSearchOnUpdateWork.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnUpdateWork.setText(_translate(
                "self.MainWindow", "Message on Update Work"))
                self.label_142.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_73.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_74.setText(_translate("self.MainWindow", "Log Out"))
                self.label_14.setText(_translate("self.MainWindow", "Custom Task ID:"))
                self.label_16.setText(_translate("self.MainWindow", "Status"))
                self.comboBox_4.setItemText(0, _translate("self.MainWindow", "Confirmed"))
                self.comboBox_4.setItemText(1, _translate("self.MainWindow", "Delayed"))
                self.label_33.setText(_translate("self.MainWindow", "To"))
                self.pushButton_10.setText(_translate("self.MainWindow", "Submit"))
                self.LabelforMenuOnUpdateWork_3.setText(
                _translate("self.MainWindow", "Update Designation"))
                self.FeildForSearchOnUpdateWork_3.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnUpdateDesignation.setText(
                _translate("self.MainWindow", "Message on Update Work"))
                self.label_233.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_172.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_173.setText(_translate("self.MainWindow", "Log Out"))
                self.label_230.setText(_translate("self.MainWindow", "Member Name:"))
                self.label_231.setText(_translate("self.MainWindow", "Designation:"))
                self.label_232.setText(_translate("self.MainWindow", "Designation Title:"))
                self.pushButton_170.setText(_translate("self.MainWindow", "Submit"))
                self.PageNameOnDashboard_3.setText(
                _translate("self.MainWindow", "Manage Leaves"))
                self.FeildForSearch_3.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnManageLeaves.setText(_translate(
                "self.MainWindow", "Message On Manage Leaves"))
                self.label_150.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_97.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_98.setText(_translate("self.MainWindow", "Log Out"))
                self.pushButton_35.setText(_translate(
                "self.MainWindow", "Upload Piicture (If Any)"))
                self.label_4.setText(_translate("self.MainWindow", "Number of Leaves:"))
                self.label_35.setText(_translate("self.MainWindow", "Reason:"))
                self.label_73.setText(_translate("self.MainWindow", "From:"))
                self.label_81.setText(_translate("self.MainWindow", "To"))
                self.label_5.setText(_translate("self.MainWindow", "Deduction Type:"))
                self.comboBox_9.setItemText(0, _translate("self.MainWindow", "Annual"))
                self.comboBox_9.setItemText(1, _translate("self.MainWindow", "Monthly"))
                self.pushButton_8.setText(_translate("self.MainWindow", "Submit"))
                item = self.tableWidget_4.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Number of Leaves"))
                item = self.tableWidget_4.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Reason"))
                item = self.tableWidget_4.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "Deduction Type"))
                item = self.tableWidget_4.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "Date"))
                item = self.tableWidget_4.horizontalHeaderItem(4)
                item.setText(_translate("self.MainWindow", "Status"))
                self.LabelforMenuOnUserProfile.setText(
                _translate("self.MainWindow", "Profile"))
                self.FeildForSearchOnUserProfile.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnProfile.setText(
                _translate("self.MainWindow", "Message On Profile"))
                self.label_143.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_76.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_77.setText(_translate("self.MainWindow", "Log Out"))
                self.pushButton_34.setText(_translate(
                "self.MainWindow", "Change Profile Picture"))
                self.label_25.setText(_translate("self.MainWindow", "Biography"))
                self.label_28.setText(_translate("self.MainWindow", "Random Contact No."))
                self.label_26.setText(_translate("self.MainWindow", "Random Name"))
                self.label_27.setText(_translate("self.MainWindow", "Random Email"))
                self.label_29.setText(_translate("self.MainWindow", "Random Gender"))
                self.label_30.setText(_translate("self.MainWindow", "Random Age"))
                self.label_31.setText(_translate("self.MainWindow", "Random Biography"))
                self.label_32.setText(_translate("self.MainWindow", "Job Role"))
                self.label_20.setText(_translate("self.MainWindow", "Name:"))
                self.label_23.setText(_translate("self.MainWindow", "Gender:"))
                self.label_22.setText(_translate("self.MainWindow", "Contact:"))
                self.label_21.setText(_translate("self.MainWindow", "Email:"))
                self.label_24.setText(_translate("self.MainWindow", "Age:"))
                self.label_2.setText(_translate("self.MainWindow", "Team Leader"))
                self.pushButton_9.setText(_translate("self.MainWindow", "Generate Card"))
                self.LabelforMenuOnTDLProductivity.setText(
                _translate("self.MainWindow", "TDL Productivity"))
                self.FeildForSearchOnTDLProductivity.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnTDL.setText(_translate(
                "self.MainWindow", "Message on TDL Productivity"))
                self.label_145.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_82.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_83.setText(_translate("self.MainWindow", "Log Out"))
                self.label_36.setText(_translate("self.MainWindow", "Custom Task Title"))
                self.lineEdit.setPlaceholderText(_translate(
                "self.MainWindow", "Custom Task Title Here"))
                self.label_15.setText(_translate("self.MainWindow", "Time Duration"))
                self.pushButton_18.setText(_translate("self.MainWindow", "Add"))
                self.label_34.setText(_translate(
                "self.MainWindow", "Team Leader Name here"))
                self.pushButton_17.setText(_translate("self.MainWindow", "Add Custom Task"))
                item = self.tableWidget_5.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Task Name"))
                item = self.tableWidget_5.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Time Duration"))
                self.LabelforMenuOnTDLProductivity_3.setText(
                _translate("self.MainWindow", "Manage Team Leaves"))
                self.FeildForSearchOnTDLProductivity_3.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnManageTeamLeaves.setText(_translate(
                "self.MainWindow", "Message On Manage Team Leaves"))
                self.label_146.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_85.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_86.setText(_translate("self.MainWindow", "Log Out"))
                item = self.tableWidget_6.horizontalHeaderItem(0)
                item.setText(_translate("self.MainWindow", "Writer Name"))
                item = self.tableWidget_6.horizontalHeaderItem(1)
                item.setText(_translate("self.MainWindow", "Reason"))
                item = self.tableWidget_6.horizontalHeaderItem(2)
                item.setText(_translate("self.MainWindow", "From"))
                item = self.tableWidget_6.horizontalHeaderItem(3)
                item.setText(_translate("self.MainWindow", "To"))
                self.label_75.setText(_translate(
                "self.MainWindow", "Selected Writer Name here"))
                self.label_76.setText(_translate("self.MainWindow", "Reason:"))
                self.label_78.setText(_translate("self.MainWindow", "Range of Leaves:"))
                self.label_77.setText(_translate(
                "self.MainWindow", "Selected Leave Reason Here"))
                self.pushButton_33.setText(_translate("self.MainWindow", "Decline"))
                self.pushButton_32.setText(_translate("self.MainWindow", "Accept"))
                self.label_79.setText(_translate(
                "self.MainWindow", "Number of leaves here"))
                self.label_74.setText(_translate("self.MainWindow", "Writer Name:"))
                self.label_80.setText(_translate("self.MainWindow", " Leave Details"))
                self.LabelforMenuOnTDLProductivity_2.setText(
                _translate("self.MainWindow", "Evaluation Sheet"))
                self.FeildForSearchOnTDLProductivity_2.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnEvaluation.setText(_translate(
                "self.MainWindow", "Message On Evaluation Sheet"))
                self.label_97.setText(_translate(
                "self.MainWindow", "Select a person to evaluate:"))
                self.label_151.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_100.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_101.setText(_translate("self.MainWindow", "Log Out"))
                self.label_61.setText(_translate("self.MainWindow", "Attitude & Behaviour"))
                self.label_62.setText(_translate("self.MainWindow", "In & Out"))
                self.label_63.setText(_translate(
                "self.MainWindow", "Coordination & Followups"))
                self.label_64.setText(_translate(
                "self.MainWindow", "Focused to New Learnings"))
                self.label_58.setText(_translate("self.MainWindow", "Instructions"))
                self.label_60.setText(_translate("self.MainWindow", "Initiatives"))
                self.label_65.setText(_translate(
                "self.MainWindow", "Planning & Management"))
                self.label_66.setText(_translate("self.MainWindow", "Team Management"))
                self.label_67.setText(_translate("self.MainWindow", "Honesty & Empathy"))
                self.label_57.setText(_translate("self.MainWindow", "Team Spirit"))
                self.label_56.setText(_translate(
                "self.MainWindow", "Punctuality & Response Time"))
                self.pushButton_23.setText(_translate("self.MainWindow", "Evaluate"))
                self.LabelforMenuOnContactUs.setText(
                _translate("self.MainWindow", "Contact Us"))
                self.FeildForSearchOnContactUs.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnContactUs.setText(_translate(
                "self.MainWindow", "Message On Contact Us"))
                self.label_148.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_91.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_92.setText(_translate("self.MainWindow", "Log Out"))
                self.label_126.setText(_translate("self.MainWindow", "Address"))
                self.label_127.setText(_translate(
                "self.MainWindow", "Random Address, Random Street, Random Block, Random Neighbourhood etc."))
                self.label_125.setText(_translate("self.MainWindow", "Phone"))
                self.label_128.setText(_translate("self.MainWindow", "+92 300-0000000"))
                self.label_129.setText(_translate("self.MainWindow", "+92 300-0000000"))
                self.label_130.setText(_translate("self.MainWindow", "Email"))
                self.label_131.setText(_translate(
                "self.MainWindow", "info@fiestacontentsolution.com"))
                self.label_132.setText(_translate("self.MainWindow", "Send us a message"))
                self.label_133.setText(_translate(
                "self.MainWindow", "Have any queries realted to us? Let us know"))
                self.lineEdit_15.setPlaceholderText(
                _translate("self.MainWindow", "Your Name Here"))
                self.lineEdit_16.setPlaceholderText(
                _translate("self.MainWindow", "Your Email Here"))
                self.plainTextEdit.setPlaceholderText(
                _translate("self.MainWindow", "Your Message Here"))
                self.pushButton_44.setText(_translate("self.MainWindow", "Send now"))
                self.LabelforMenuOnFAQs.setText(_translate("self.MainWindow", "FAQs"))
                self.FeildForSearchOnFAQs.setPlaceholderText(
                _translate("self.MainWindow", "Search"))
                self.MessageOnFAQs.setText(_translate(
                "self.MainWindow", "Message On Frequently Asked Question"))
                self.label_149.setText(_translate("self.MainWindow", self.Writer_Name))
                self.pushButton_94.setText(_translate("self.MainWindow", "My Profile"))
                self.pushButton_95.setText(_translate("self.MainWindow", "Log Out"))
                self.pushButton_2.setText(_translate("self.MainWindow", "FAQ1 Question?"))
                self.label_3.setText(_translate("self.MainWindow", "FAQ1 Answer"))
                self.pushButton_3.setText(_translate("self.MainWindow", "FAQ2 Question?"))
                self.label_6.setText(_translate("self.MainWindow", "FAQ2 Answer"))
                self.pushButton_4.setText(_translate("self.MainWindow", "FAQ3 Question?"))
                self.label_7.setText(_translate("self.MainWindow", "FAQ3 Answer"))
                self.pushButton_5.setText(_translate("self.MainWindow", "FAQ4 Question?"))
                self.label_38.setText(_translate("self.MainWindow", "FAQ4 Answer"))
                self.pushButton_6.setText(_translate("self.MainWindow", "FAQ5 Question?"))
                self.label_39.setText(_translate("self.MainWindow", "FAQ5 Answer"))
                self.label_45.setText(_translate("self.MainWindow", "Notification Board"))
                self.label_47.setText(_translate("self.MainWindow", "Announcement"))
                self.label_48.setText(_translate("self.MainWindow", "Do consider Basic Ethics and Hygeine\n"
                                                "While you want to leave an impression"))
                self.label_49.setText(_translate("self.MainWindow", "Team of the Month"))
                self.label_50.setText(_translate("self.MainWindow", "Team Mutavir"))
                self.label_51.setText(_translate(
                "self.MainWindow", "Employee of the Month"))
                self.label_52.setText(_translate("self.MainWindow", "ANY ONE CAN ACHEIVE THIS PLACE.\n"
                                                "THIS PLACE IS FOR YOU BE\n"
                                                "MOTIVATED.\n"
                                                "DON\'T LOSE HOPE"))
                self.label_53.setText(_translate("self.MainWindow", "New Task"))
                self.label_54.setText(_translate("self.MainWindow", "Visit Dashboard to check if there are\n"
                                                "any new tasks."))
                self.label_37.setText(_translate(
                "self.MainWindow", "All Rights reserved. Developed by Team Mutavir."))
                self.label_43.setText(_translate("self.self.MainWindow", self.Team_Name))
                self.Card1Value.setText(_translate(
                "self.self.MainWindow", self.New_Members))
                self.CardV2Value.setText(_translate(
                "self.self.MainWindow", self.Total_Assignments))
                self.label_41.setText(_translate("self.self.MainWindow", self.Evaluation_points))
                self.label_135.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_10.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_137.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_138.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_139.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_141.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_140.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_142.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_150.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_143.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_26.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_145.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_34.setText(_translate(
                "self.self.MainWindow", "Welcome "+self.Writer_Name+"! to your very own TDL(To-do List). Let us know what you have in mind today"))
                self.label_151.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_148.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_149.setText(_translate("self.self.MainWindow", self.Writer_Name))
                self.label_27.setText(_translate("self.self.MainWindow", self.Writer_Email))
                self.label_28.setText(_translate("self.self.MainWindow", self.Writer_Contact_No))
                self.label_29.setText(_translate("self.self.MainWindow", self.Writer_Gender))
                self.label_30.setText(_translate("self.self.MainWindow", self.Writer_Age))
                self.label_31.setText(_translate("self.self.MainWindow", self.Writer_Biography))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GetData = DB_Data("abe.fiesta", "1")
    ui = TDL_UI(False, str(GetData.writer_team_name),"5", '15', str(GetData.writer_evaluation_points), str(GetData.writer_fullname),f"F:\\Visual Code Stuff\\Design_For_FCS_Portal\\Images\\writer_image.png",str(GetData.writer_email),str(GetData.writer_phone),str(GetData.writer_gender),'24',str(GetData.writer_description),str(GetData.writer_jobe_role), str(GetData.writer_team_leader))
    sys.exit(app.exec_())