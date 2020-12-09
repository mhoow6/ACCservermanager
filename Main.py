from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import Ui_MainWindow
import sys, os, json
from tkinter import messagebox as msg
from tkinter import Tk
from io import StringIO

# ui -> py
# >pyuic5 -x E:\github\ACCservermanager\ACC_Dedicated_Server_GUI.ui -o E:\github\ACCservermanager\GUI.py


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.setupUi(self)

        self.accServerCheck()

        self.initUI()

        self.show()

    # Initalize the Graphic Interface
    def initUI(self):

        try:
            with open("cfg/settings.json", encoding='UTF-16') as settings:
                # load json file
                settings = json.load(settings)

                # looking json file
                io = StringIO()
                json.dump(settings, io, indent="\t")
                print(io.getvalue())

                # setText from json file
                self.lineEdit_serverName.setText(settings['serverName'])
                self.lineEdit_password.setText(settings['password'])
                self.lineEdit_adminPassword.setText(settings['adminPassword'])
                self.spinBox_maxCarSlots.setValue(settings['maxCarSlots'])
                self.spinBox_trackMedalsRequirement.setValue(settings['trackMedalsRequirement'])
                self.spinBox_safetyRatingRequirement.setValue(settings['safetyRatingRequirement'])
                self.checkBox_dumpLeaderboards.setChecked(settings['dumpLeaderboards'])
                self.checkBox_isRaceLocked.setChecked(settings['isRaceLocked'])
                self.checkBox_allowAutoDQ.setChecked(settings['allowAutoDQ'])

        except FileNotFoundError:
            print("cfg/settings.json is not found")

        try:
            with(open("cfg/configuration.json", encoding="UTF-16")) as configuration:
                # load json file
                configuration = json.load(configuration)

                # looking json file
                io = StringIO()
                json.dump(configuration, io, indent="\t")
                print(io.getvalue())

                # setText from json file
                self.spinBox_maxConnections.setValue(configuration['maxConnections'])

        except FileNotFoundError:
            print("cfg/configuration.json is not found")

        try:
            with open("cfg/assistRules.json", encoding='UTF-16') as assist:
                # load json file
                assist = json.load(assist)

                # looking json file
                io = StringIO()
                json.dump(assist, io, indent="\t")
                print(io.getvalue())

                # setText from json file
                self.checkBox_disableIdealLine.setChecked(assist['disableIdealLine'])
                self.checkBox_disableAutosteer.setChecked(assist['disableAutosteer'])
                self.checkBox_disableAutoLights.setChecked(assist['disableAutoLights'])
                self.checkBox_disableAutoWiper.setChecked(assist['disableAutoWiper'])
                self.checkBox_disableAutoEngineStart.setChecked(assist['disableAutoEngineStart'])
                self.checkBox_disableAutoPitLimiter.setChecked(assist['disableAutoPitLimiter'])
                self.checkBox_disableAutoGear.setChecked(assist['disableAutoGear'])
                self.checkBox_disableAutoClutch.setChecked(assist['disableAutoClutch'])
                self.horizontalSlider_stabilityControlLevelMax.setValue(assist['stabilityControlLevelMax'])

        except FileNotFoundError:
            print("cfg/assistRules.json is not found")



    # Is accServer.exe in directory?
    def accServerCheck(self):
        root = Tk()
        root.withdraw()

        message = "accServer.exe를 찾을 수 없습니다. 프로그램을 \'Assetto Corsa Competizione Dedicated Server\server\' 경로에 넣어주세요."

        if not os.path.exists('./accServer.exe'):
            msg.showerror("accServer.exe is not found", message=message)
            raise Exception("accServer.exe is not found")



if __name__ == '__main__':
    app = QApplication([])
    ex = Main()
    sys.exit(app.exec_())