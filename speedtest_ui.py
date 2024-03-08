from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 463)
        MainWindow.setWindowTitle(u"Internet Speed Tester")
        icon = QIcon()
        icon.addFile(u"speedtest_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appTitle = QLabel(self.centralwidget)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(170, 20, 339, 46))
        self.appTitle.setStyleSheet(u"text-align:center;\n"
"color: rgb(0, 255, 127);\n"
"font-weight: bold;\n"
"font-size: 34px;")
        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(170, 100, 322, 30))
        self.description.setStyleSheet(u"color: gold;\n"
"font-size: 22px;\n"
"font-weight: 500")
        self.ping_header = QLabel(self.centralwidget)
        self.ping_header.setObjectName(u"ping_header")
        self.ping_header.setGeometry(QRect(80, 170, 36, 22))
        self.ping_header.setStyleSheet(u"color: lightblue;\n"
"font-weight: bold;\n"
"font-size: 17px;")
        self.download_header = QLabel(self.centralwidget)
        self.download_header.setObjectName(u"download_header")
        self.download_header.setGeometry(QRect(280, 170, 82, 22))
        self.download_header.setStyleSheet(u"color: lightblue;\n"
"font-weight: bold;\n"
"font-size: 17px;")
        self.upload_header = QLabel(self.centralwidget)
        self.upload_header.setObjectName(u"upload_header")
        self.upload_header.setGeometry(QRect(490, 170, 58, 22))
        self.upload_header.setStyleSheet(u"color: lightblue;\n"
"font-weight: bold;\n"
"font-size: 17px;")
        self.startSpeedTestBtn = QPushButton(self.centralwidget)
        self.startSpeedTestBtn.setObjectName(u"startSpeedTestBtn")
        self.startSpeedTestBtn.setGeometry(QRect(260, 350, 123, 29))
        self.startSpeedTestBtn.setStyleSheet(u"background-color: firebrick;\n"
"color: lightseagreen;\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.ping_speed = QLabel(self.centralwidget)
        self.ping_speed.setObjectName(u"ping_speed")
        self.ping_speed.setGeometry(QRect(70, 240, 49, 16))
        self.ping_speed.setStyleSheet(u"font-size: 13px;color: orange;")
        self.download_speed = QLabel(self.centralwidget)
        self.download_speed.setObjectName(u"download_speed")
        self.download_speed.setGeometry(QRect(300, 240, 49, 16))
        self.download_speed.setStyleSheet(u"color: orange;\n"
"font-size: 13px;")
        self.upload_speed = QLabel(self.centralwidget)
        self.upload_speed.setObjectName(u"upload_speed")
        self.upload_speed.setGeometry(QRect(500, 240, 49, 16))
        self.upload_speed.setStyleSheet(u"color: orange;\n"
"font-size: 13px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"Internet Speed Tester", None))
        self.appTitle.adjustSize()
        self.description.setText(QCoreApplication.translate("MainWindow", u"SpeedTest right on your desktop!", None))
        self.ping_header.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.download_header.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.upload_header.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.startSpeedTestBtn.setText(QCoreApplication.translate("MainWindow", u"Run Speed Test", None))
        self.ping_speed.setText("")
        self.download_speed.setText("")
        self.upload_speed.setText("")
        pass
    # retranslateUi

