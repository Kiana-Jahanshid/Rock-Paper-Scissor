# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rockpaperscissorqnVyQx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 635)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(70, 212, 0);\n"
"border-color: rgb(170, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.win_btn = QPushButton(self.centralwidget)
        self.win_btn.setObjectName(u"win_btn")
        self.win_btn.setGeometry(QRect(41, 221, 531, 51))
        self.win_btn.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(255, 255, 127);")
        self.rock_btn = QPushButton(self.centralwidget)
        self.rock_btn.setObjectName(u"rock_btn")
        self.rock_btn.setGeometry(QRect(60, 500, 151, 81))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.rock_btn.setFont(font1)
        self.rock_btn.setStyleSheet(u"border-radius: 20px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(255, 170, 127);")
        self.paper_btn = QPushButton(self.centralwidget)
        self.paper_btn.setObjectName(u"paper_btn")
        self.paper_btn.setGeometry(QRect(240, 500, 151, 81))
        font2 = QFont()
        font2.setPointSize(17)
        self.paper_btn.setFont(font2)
        self.paper_btn.setStyleSheet(u"border-radius: 20px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(255, 170, 127);")
        self.sci_btn = QPushButton(self.centralwidget)
        self.sci_btn.setObjectName(u"sci_btn")
        self.sci_btn.setGeometry(QRect(420, 500, 141, 81))
        self.sci_btn.setFont(font2)
        self.sci_btn.setStyleSheet(u"border-radius: 20px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(255, 170, 127);")
        self.player_score_btn = QPushButton(self.centralwidget)
        self.player_score_btn.setObjectName(u"player_score_btn")
        self.player_score_btn.setGeometry(QRect(191, 431, 211, 51))
        font3 = QFont()
        font3.setPointSize(15)
        self.player_score_btn.setFont(font3)
        self.player_score_btn.setStyleSheet(u"border-radius: 15px;")
        self.comp_score_btn = QPushButton(self.centralwidget)
        self.comp_score_btn.setObjectName(u"comp_score_btn")
        self.comp_score_btn.setGeometry(QRect(191, 11, 211, 51))
        self.comp_score_btn.setFont(font3)
        self.comp_score_btn.setStyleSheet(u"border-radius: 15px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 291, 171, 131))
        self.frame.setStyleSheet(u"border :2px solid black;\n"
"border-style : dashed")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.f1 = QPushButton(self.frame)
        self.f1.setObjectName(u"f1")
        self.f1.setGeometry(QRect(0, 0, 171, 131))
        font4 = QFont()
        font4.setPointSize(43)
        self.f1.setFont(font4)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 70, 171, 131))
        self.frame_2.setStyleSheet(u"border :2px solid black;\n"
"border-style : dashed")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.f2 = QPushButton(self.frame_2)
        self.f2.setObjectName(u"f2")
        self.f2.setGeometry(QRect(0, 0, 171, 131))
        self.f2.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rock_btn.setText(QCoreApplication.translate("MainWindow", u"✊🏻\n"
" ROCK ", None))
        self.paper_btn.setText(QCoreApplication.translate("MainWindow", u"✋🏻\n"
"PAPER", None))
        self.sci_btn.setText(QCoreApplication.translate("MainWindow", u"✌🏻\n"
"SCISSOR", None))
        self.player_score_btn.setText(QCoreApplication.translate("MainWindow", u"Player Score : ", None))
        self.comp_score_btn.setText(QCoreApplication.translate("MainWindow", u"Computer Score : ", None))
        self.f1.setText("")
        self.f2.setText("")
    # retranslateUi

