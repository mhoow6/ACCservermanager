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

    # Initalize the Graphic User Interface
    def initUI(self):
        self.tracklist = [
            'monza', 'zolder', 'brands_hatch', 'sliverstone', 'paul_ricard', 'misano', 'spa', 'nurburgring',
            'barcelona', 'hungaroring', 'zandvoort', 'monza_2019', 'zolder_2019', 'brands_hatch_2019',
            'silverstone_2019', 'paul_ricard_2019', 'misano_2019', 'spa_2019', 'nurburgring_2019', 'barcelona_2019',
            'hungaroring_2019', 'zandvoort_2019', 'kyalami_2019', 'mount_panorama_2019', 'suzuka_2019',
            'laguna_seca_2019',
            'monza_2020', 'zolder_2020', 'brands_hatch_2020', 'silverstone_2020', 'paul_ricard_2020', 'misano_2020',
            'spa_2020',
            'nurburgring_2020', 'barcelona_2020', 'hungaroring_2020', 'zandvoort_2020', 'imola_2020'
        ]
        self.carlist = ["FreeForAll", "GT3", "GT4", "Cup", "ST"]

        self.comboBox_track.addItems(self.tracklist)
        self.comboBox_car.addItems(self.carlist)

        try:
            with open("cfg/settings.json", encoding='UTF-16') as settings:
                # load json file
                settings = json.load(settings)

                # looking json file
                io = StringIO()
                json.dump(settings, io, indent="\t")
                print(io.getvalue())

                # set value from json file
                self.lineEdit_serverName.setText(settings['serverName'])
                self.lineEdit_password.setText(settings['password'])
                self.lineEdit_adminPassword.setText(settings['adminPassword'])
                self.spinBox_maxCarSlots.setValue(settings['maxCarSlots'])
                self.spinBox_trackMedalsRequirement.setValue(settings['trackMedalsRequirement'])
                self.spinBox_safetyRatingRequirement.setValue(settings['safetyRatingRequirement'])
                self.checkBox_dumpLeaderboards.setChecked(settings['dumpLeaderboards'])
                self.checkBox_isRaceLocked.setChecked(settings['isRaceLocked'])
                self.checkBox_allowAutoDQ.setChecked(settings['allowAutoDQ'])
                self.comboBox_car.setCurrentText(settings['carGroup'])


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

                # set value from json file
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

                # set value from json file
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

        try:
            with open("cfg/event.json", encoding='UTF-16') as event:
                # load json file
                event = json.load(event)

                # looking json file
                io = StringIO()
                json.dump(event, io, indent="\t")
                print(io.getvalue())

                # set value from json file
                self.comboBox_track.setCurrentText(event['track'])
                self.spinBox_preRaceWaitingTimeSeconds.setValue(event['preRaceWaitingTimeSeconds'])
                self.spinBox_sessionOverTimeSeconds.setValue(event['sessionOverTimeSeconds'])
                self.horizontalSlider_ambientTemp.setValue(event['ambientTemp'])
                self.lcdNumber_ambientTemp.display(event['ambientTemp'])
                self.doubleSpinBox_cloudLevel.setValue(event['cloudLevel'])
                self.doubleSpinBox_rain.setValue(event['rain'])

                # set value Session's value
                def initSessison(index):
                    if event['sessions'][index]['sessionType'] == "P":
                        self.groupBox_practice.setChecked(True)
                        self.spinBox_practice_hourOfDay.setValue(event['sessions'][index]['hourOfDay'])
                        self.spinBox_practice_timeMultiplier.setValue(event['sessions'][index]['timeMultiplier'])
                        self.spinBox_practice_sessionDurationMinutes.setValue(
                            event['sessions'][index]['sessionDurationMinutes'])
                        if event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_practice_friday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_practice_saturday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_practice_sunday.setChecked(True)

                    if event['sessions'][index]['sessionType'] == "Q":
                        self.groupBox_qualify.setChecked(True)
                        self.spinBox_qualify_hourOfDay.setValue(event['sessions'][index]['hourOfDay'])
                        self.spinBox_qualify_timeMultiplier.setValue(event['sessions'][index]['timeMultiplier'])
                        self.spinBox_qualify_sessionDurationMinutes.setValue(
                            event['sessions'][index]['sessionDurationMinutes'])
                        if event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_qualify_friday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_qualify_saturday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_qualify_sunday.setChecked(True)

                    if event['sessions'][index]['sessionType'] == "R":
                        self.groupBox_race.setChecked(True)
                        self.spinBox_race_hourOfDay.setValue(event['sessions'][index]['hourOfDay'])
                        self.spinBox_race_timeMultiplier.setValue(event['sessions'][index]['timeMultiplier'])
                        self.spinBox_race_sessionDurationMinutes.setValue(
                            event['sessions'][index]['sessionDurationMinutes'])
                        if event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_race_friday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_race_saturday.setChecked(True)
                        elif event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_race_sunday.setChecked(True)

                # set value by session type
                if event['sessions'][0]['sessionType'] == "P":
                    initSessison(0)
                    if event['sessions'][1]['sessionType'] == "Q":
                        initSessison(1)
                    elif event['sessions'][1]['sessionType'] == "R":
                        initSessison(1)
                        if len(event['sessions']) > 2:
                            if event['sessions'][2]['sessionType'] == "R":
                                initSessison(2)
                elif event['sessions'][0]['sessionType'] == "Q":
                    initSessison(0)
                    if event['sessions'][1]['sessionType'] == "R":
                        initSessison(1)

        except FileNotFoundError:
            print("cfg/event.json is not found")



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