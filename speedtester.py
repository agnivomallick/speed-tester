import time

from PySide6.QtWidgets import *  # import QtWidgets from Pyside6
from PySide6.QtGui import QIcon  # for icon
from speedtest_ui import Ui_MainWindow  # main ui
import math  # for conversion of units
import speedtest  # for speed testing


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        try:
            # display window icon in taskbar also
            # ONLY WORKS IN WINDOWS
            from ctypes import windll
            appid = "mycompany.myproduct.subproduct.version"
            # specify dummy app id to trick windows to use the window icon.
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
            # setting it

        except ImportError:  # for other os where this is not present
            pass

        self.ui = Ui_MainWindow()  # import ui
        self.ui.setupUi(self)  # set up the ui

        self.ui.startSpeedTestBtn.clicked.connect(self.startSpeedTest)  # add event handler to the button on Click

    def startSpeedTest(self):

        # display the message box
        message_box = QMessageBox()
        message_box.setWindowTitle("Started speed test")
        icon = QIcon()  # initialise QIcon
        icon.addFile("speedtest_icon.png")  # add the icon file

        message_box.setWindowIcon(icon)  # setting the icon

        message_box.setText("""
        Speed test started. 
        This may take some time.
        """)  # set main body text

        message_box.setIcon(QMessageBox.Information)  # specifies the type of message box - here info

        message_box.exec()  # show message box

        self.ui.startSpeedTestBtn.setDisabled(True)  # disable the run speed test button

        time.sleep(0.01)  # wait for 0.01 seconds

        test = speedtest.Speedtest()  # initialise speedtest

        ping = str(test.results.ping) + " ms"  # latency in milliseconds
        down = str(math.ceil(test.download() / 1000000)) + " Mbps"

        # download speed is in bits /second. We have to convert it into Mega Bits / second.
        # so we divide by 1000000 ( 10 lakh or 1 million bits)

        # same for upload speed.

        upload = str(math.ceil(test.upload() / 1000000)) + " Mbps"

        self.ui.ping_speed.setText(ping)  # set ping value
        self.ui.download_speed.setText(down)   # set download value
        self.ui.upload_speed.setText(upload)   # set upload value
        self.ui.ping_speed.adjustSize()  # adjust the size of the ping speed label box
        self.ui.download_speed.adjustSize()  # adjust the size of the download speed label box
        self.ui.upload_speed.adjustSize()  # adjust the size of the upload speed label box

        self.ui.startSpeedTestBtn.setDisabled(False)  # enable the start speed test button

# specifies to run this app if it is run standalone, not if it is imported by other files / apps


if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()

    app.exec()
