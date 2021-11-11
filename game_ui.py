from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(888, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/rock-paper-scissors.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GameWindow.setWindowIcon(icon)
        GameWindow.setStyleSheet("background-color: #F0F5F9;")
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setObjectName("welcome_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.welcome_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.welcome_page)
        self.title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color:none;\n"
"color:#FF2E63;")
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.start_btn = QtWidgets.QPushButton(self.welcome_page)
        self.start_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.start_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("#start_btn{\n"
"background-color:#FF9A00;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#start_btn::hover{\n"
"color:#FF9A00;\n"
"background-color:white;\n"
"}\n"
"#start_btn::pressed{\n"
"border-radius:5px;\n"
"}")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 7, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.icon = QtWidgets.QLabel(self.welcome_page)
        self.icon.setStyleSheet("background-color:none;")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/rock-paper-scissors (2).png"))
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 3, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.welcome_page)
        self.round_page = QtWidgets.QWidget()
        self.round_page.setObjectName("round_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.round_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rounds_3_btn = QtWidgets.QPushButton(self.round_page)
        self.rounds_3_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.rounds_3_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.rounds_3_btn.setFont(font)
        self.rounds_3_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rounds_3_btn.setStyleSheet("#rounds_3_btn{\n"
"background-color:#8C82FC;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"#rounds_3_btn::hover{\n"
"color:#8C82FC;\n"
"background-color:white;\n"
"}\n"
"#rounds_3_btn::pressed{\n"
"border-radius:5px;\n"
"}")
        self.rounds_3_btn.setObjectName("rounds_3_btn")
        self.gridLayout_3.addWidget(self.rounds_3_btn, 1, 0, 1, 1)
        self.rounds_6_btn = QtWidgets.QPushButton(self.round_page)
        self.rounds_6_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.rounds_6_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.rounds_6_btn.setFont(font)
        self.rounds_6_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rounds_6_btn.setStyleSheet("#rounds_6_btn{\n"
"background-color:#B693FE;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"#rounds_6_btn::hover{\n"
"color:#B693FE;\n"
"background-color:white;\n"
"}\n"
"#rounds_6_btn::pressed{\n"
"border-radius:5px;\n"
"}")
        self.rounds_6_btn.setObjectName("rounds_6_btn")
        self.gridLayout_3.addWidget(self.rounds_6_btn, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rock_icon = QtWidgets.QLabel(self.round_page)
        self.rock_icon.setStyleSheet("background-color:none;")
        self.rock_icon.setText("")
        self.rock_icon.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/stone (2).png"))
        self.rock_icon.setScaledContents(False)
        self.rock_icon.setWordWrap(False)
        self.rock_icon.setObjectName("rock_icon")
        self.horizontalLayout.addWidget(self.rock_icon, 0, QtCore.Qt.AlignHCenter)
        self.paper_icon = QtWidgets.QLabel(self.round_page)
        self.paper_icon.setStyleSheet("background-color:none;")
        self.paper_icon.setText("")
        self.paper_icon.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/paper.png"))
        self.paper_icon.setObjectName("paper_icon")
        self.horizontalLayout.addWidget(self.paper_icon, 0, QtCore.Qt.AlignHCenter)
        self.scissors_icon = QtWidgets.QLabel(self.round_page)
        self.scissors_icon.setStyleSheet("background-color:none;")
        self.scissors_icon.setText("")
        self.scissors_icon.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/scissors.png"))
        self.scissors_icon.setObjectName("scissors_icon")
        self.horizontalLayout.addWidget(self.scissors_icon, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.raound_title = QtWidgets.QLabel(self.round_page)
        self.raound_title.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.raound_title.setFont(font)
        self.raound_title.setStyleSheet("background-color:none;\n"
"color:#F73859;\n"
"")
        self.raound_title.setObjectName("raound_title")
        self.verticalLayout_4.addWidget(self.raound_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.stackedWidget.addWidget(self.round_page)
        self.game_page = QtWidgets.QWidget()
        self.game_page.setObjectName("game_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.game_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.round_lbl = QtWidgets.QLabel(self.game_page)
        self.round_lbl.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.round_lbl.setFont(font)
        self.round_lbl.setStyleSheet("background-color:#E23E57;\n"
"color:white;\n"
"padding:5px 10px;")
        self.round_lbl.setObjectName("round_lbl")
        self.verticalLayout_7.addWidget(self.round_lbl)
        self.c_score = QtWidgets.QLabel(self.game_page)
        self.c_score.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.c_score.setFont(font)
        self.c_score.setStyleSheet("background-color:#E23E57;\n"
"color:white;\n"
"padding:5px 10px;")
        self.c_score.setObjectName("c_score")
        self.verticalLayout_7.addWidget(self.c_score)
        self.y_score = QtWidgets.QLabel(self.game_page)
        self.y_score.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.y_score.setFont(font)
        self.y_score.setStyleSheet("background-color:#E23E57;\n"
"color:white;\n"
"padding:5px 10px;")
        self.y_score.setObjectName("y_score")
        self.verticalLayout_7.addWidget(self.y_score)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.game_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#FF2E63;\n"
"background-color:none;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.game_page)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_5.setStyleSheet("border-radius:15px;\n"
"background-color:none")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/stone (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_6 = QtWidgets.QPushButton(self.game_page)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_6.setStyleSheet("border-radius:15px;\n"
"background-color:none")
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignVCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.game_page)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_4.setStyleSheet("border-radius:15px;\n"
"background-color:none")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/scissors.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.computer_choice = QtWidgets.QLabel(self.game_page)
        self.computer_choice.setStyleSheet("background-color:#C9D6DF;\n"
"border-radius:10px")
        self.computer_choice.setText("")
        self.computer_choice.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/stone (2).png"))
        self.computer_choice.setObjectName("computer_choice")
        self.verticalLayout_6.addWidget(self.computer_choice, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.your_choice = QtWidgets.QLabel(self.game_page)
        self.your_choice.setStyleSheet("background-color:#C9D6DF;\n"
"border-radius:10px;")
        self.your_choice.setText("")
        self.your_choice.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/stone (2).png"))
        self.your_choice.setObjectName("your_choice")
        self.verticalLayout_6.addWidget(self.your_choice, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.game_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FF2E63;\n"
"background-color:none;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.y_rock_btn = QtWidgets.QPushButton(self.game_page)
        self.y_rock_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_rock_btn.setStyleSheet("#y_rock_btn{\n"
"border-radius:15px;\n"
"background-color:none;\n"
"}\n"
"#y_rock_btn:pressed{\n"
"background-color:#52616B;\n"
"}")
        self.y_rock_btn.setText("")
        self.y_rock_btn.setIcon(icon1)
        self.y_rock_btn.setIconSize(QtCore.QSize(100, 100))
        self.y_rock_btn.setObjectName("y_rock_btn")
        self.horizontalLayout_2.addWidget(self.y_rock_btn, 0, QtCore.Qt.AlignHCenter)
        self.y_paper_btn = QtWidgets.QPushButton(self.game_page)
        self.y_paper_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_paper_btn.setStyleSheet("#y_paper_btn{\n"
"border-radius:15px;\n"
"background-color:none;\n"
"}\n"
"#y_paper_btn:pressed{\n"
"background-color:#FFDE7D;\n"
"}")
        self.y_paper_btn.setText("")
        self.y_paper_btn.setIcon(icon2)
        self.y_paper_btn.setIconSize(QtCore.QSize(100, 100))
        self.y_paper_btn.setObjectName("y_paper_btn")
        self.horizontalLayout_2.addWidget(self.y_paper_btn, 0, QtCore.Qt.AlignHCenter)
        self.y_scissors_btn = QtWidgets.QPushButton(self.game_page)
        self.y_scissors_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_scissors_btn.setStyleSheet("#y_scissors_btn{\n"
"border-radius:15px;\n"
"background-color:none;\n"
"}\n"
"#y_scissors_btn:pressed{\n"
"background-color:#CCA8E9;\n"
"}")
        self.y_scissors_btn.setText("")
        self.y_scissors_btn.setIcon(icon3)
        self.y_scissors_btn.setIconSize(QtCore.QSize(100, 100))
        self.y_scissors_btn.setObjectName("y_scissors_btn")
        self.horizontalLayout_2.addWidget(self.y_scissors_btn, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.stackedWidget.addWidget(self.game_page)
        self.finished_page = QtWidgets.QWidget()
        self.finished_page.setObjectName("finished_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.finished_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.king_icon = QtWidgets.QLabel(self.finished_page)
        self.king_icon.setStyleSheet("background-color:none;")
        self.king_icon.setText("")
        self.king_icon.setPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/king.png"))
        self.king_icon.setObjectName("king_icon")
        self.verticalLayout_8.addWidget(self.king_icon, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.title_2 = QtWidgets.QLabel(self.finished_page)
        font = QtGui.QFont()
        font.setPointSize(44)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("background-color:none;\n"
"color:#FF9A00")
        self.title_2.setObjectName("title_2")
        self.verticalLayout_8.addWidget(self.title_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.start_again_btn = QtWidgets.QPushButton(self.finished_page)
        self.start_again_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.start_again_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start_again_btn.setFont(font)
        self.start_again_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_again_btn.setStyleSheet("#start_again_btn{\n"
"background-color:#FF9A00;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#start_again_btn:hover{\n"
"background-color:white;\n"
"color:#FF9A00;\n"
"}")
        self.start_again_btn.setObjectName("start_again_btn")
        self.verticalLayout_8.addWidget(self.start_again_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout_8)
        self.stackedWidget.addWidget(self.finished_page)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        GameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "Rock Paper Scissors"))
        self.title.setText(_translate("GameWindow", "Rock,Paper,Scissors"))
        self.start_btn.setText(_translate("GameWindow", "Start Game"))
        self.rounds_3_btn.setText(_translate("GameWindow", "3"))
        self.rounds_6_btn.setText(_translate("GameWindow", "6"))
        self.raound_title.setText(_translate("GameWindow", "Choose Count Of Rounds"))
        self.round_lbl.setText(_translate("GameWindow", "Round:"))
        self.c_score.setText(_translate("GameWindow", "Computer Score:"))
        self.y_score.setText(_translate("GameWindow", "Your Score:"))
        self.label_2.setText(_translate("GameWindow", "Computer:"))
        self.label.setText(_translate("GameWindow", "You:"))
        self.title_2.setText(_translate("GameWindow", "You Won"))
        self.start_again_btn.setText(_translate("GameWindow", "Play Again"))


