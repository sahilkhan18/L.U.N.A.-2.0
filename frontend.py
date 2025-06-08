# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.9



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 901))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 580, 361, 311))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color : rgb(255, 255, 255)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/start_stop.jpeg.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 790, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 650, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 255, 0)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 251, 421))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/T8bahf1.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-40, 430, 411, 491))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/codes.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 10, 251, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/T8bahf.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(920, 10, 191, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:\LUNA 2.0/ai.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 10, 161, 51))
        self.textBrowser.setStyleSheet("font: 75 14pt \"MS Serif\";\n"
"background: transparent;\n"
"color:white;\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(760, 10, 161, 51))
        self.textBrowser_2.setStyleSheet("font: 75 14pt \"MS Serif\";\n"
"background: transparent;\n"
"color:white;\n"
"border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(470, 810, 191, 41))
        self.textBrowser_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_3.setStyleSheet("font: 48pt \"MV Boli\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">This GUI is designed by Sahil and Satyendra</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
