from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import Ui_MainWindow
import sys, os, json
from tkinter import messagebox as msg
from tkinter import Tk
from io import StringIO

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
            'laguna_seca_2019', 'monza_2020', 'zolder_2020', 'brands_hatch_2020', 'silverstone_2020',
            'paul_ricard_2020', 'misano_2020', 'spa_2020', 'nurburgring_2020', 'barcelona_2020',
            'hungaroring_2020', 'zandvoort_2020', 'imola_2020'
        ]

        self.carlist = ["FreeForAll", "GT3", "GT4", "Cup", "ST"]

        self.comboBox_track.addItems(self.tracklist)
        self.comboBox_car.addItems(self.carlist)

        try:
            with open("cfg/settings.json", encoding='UTF-16') as settings:
                # load json file
                self.settings = json.load(settings)

                # looking json file
                io = StringIO()
                json.dump(self.settings, io, indent="\t")
                print(io.getvalue())
                print(type(settings))

                # set value from json file
                self.lineEdit_serverName.setText(self.settings['serverName'])
                self.lineEdit_password.setText(self.settings['password'])
                self.lineEdit_adminPassword.setText(self.settings['adminPassword'])
                self.spinBox_maxCarSlots.setValue(self.settings['maxCarSlots'])
                self.spinBox_trackMedalsRequirement.setValue(self.settings['trackMedalsRequirement'])
                self.spinBox_safetyRatingRequirement.setValue(self.settings['safetyRatingRequirement'])
                self.checkBox_dumpLeaderboards.setChecked(self.settings['dumpLeaderboards'])
                self.checkBox_isRaceLocked.setChecked(self.settings['isRaceLocked'])
                self.checkBox_allowAutoDQ.setChecked(self.settings['allowAutoDQ'])
                self.comboBox_car.setCurrentText(self.settings['carGroup'])
                self.checkBox_shortFormationLap.setChecked(self.settings['shortFormationLap'])

        except FileNotFoundError:
            print("cfg/settings.json is not found")

        try:
            with(open("cfg/configuration.json", encoding="UTF-16")) as configuration:
                # load json file
                self.configuration = json.load(configuration)

                # looking json file
                io = StringIO()
                json.dump(self.configuration, io, indent="\t")
                print(io.getvalue())

                # set value from json file
                self.spinBox_maxConnections.setValue(self.configuration['maxConnections'])

        except FileNotFoundError:
            print("cfg/configuration.json is not found")

        try:
            with open("cfg/assistRules.json", encoding='UTF-16') as assist:
                # load json file
                self.assist = json.load(assist)

                # looking json file
                io = StringIO()
                json.dump(self.assist, io, indent="\t")
                print(io.getvalue())

                # set value from json file
                self.checkBox_disableIdealLine.setChecked(self.assist['disableIdealLine'])
                self.checkBox_disableAutosteer.setChecked(self.assist['disableAutosteer'])
                self.checkBox_disableAutoLights.setChecked(self.assist['disableAutoLights'])
                self.checkBox_disableAutoWiper.setChecked(self.assist['disableAutoWiper'])
                self.checkBox_disableAutoEngineStart.setChecked(self.assist['disableAutoEngineStart'])
                self.checkBox_disableAutoPitLimiter.setChecked(self.assist['disableAutoPitLimiter'])
                self.checkBox_disableAutoGear.setChecked(self.assist['disableAutoGear'])
                self.checkBox_disableAutoClutch.setChecked(self.assist['disableAutoClutch'])
                self.horizontalSlider_stabilityControlLevelMax.setValue(self.assist['stabilityControlLevelMax'])

        except FileNotFoundError:
            print("cfg/assistRules.json is not found")

        try:
            with open("cfg/event.json", encoding='UTF-16') as event:
                # load json file
                self.event = json.load(event)

                # looking json file
                io = StringIO()
                json.dump(self.event, io, indent="\t")
                print(io.getvalue())

                # set value from json file
                self.comboBox_track.setCurrentText(self.event['track'])
                self.spinBox_preRaceWaitingTimeSeconds.setValue(self.event['preRaceWaitingTimeSeconds'])
                self.spinBox_sessionOverTimeSeconds.setValue(self.event['sessionOverTimeSeconds'])
                self.horizontalSlider_ambientTemp.setValue(self.event['ambientTemp'])
                self.lcdNumber_ambientTemp.display(self.event['ambientTemp'])
                self.horizontalSlider_weatherRandomness.setValue(self.event['weatherRandomness'])
                self.lcdNumber_weatherRandomness.display(self.event['weatherRandomness'])
                self.doubleSpinBox_cloudLevel.setValue(self.event['cloudLevel'])
                self.doubleSpinBox_rain.setValue(self.event['rain'])

                # set value Session's value
                def initSessison(index):
                    if self.event['sessions'][index]['sessionType'] == "P":
                        self.groupBox_practice.setChecked(True)
                        self.spinBox_practice_hourOfDay.setValue(self.event['sessions'][index]['hourOfDay'])
                        self.spinBox_practice_timeMultiplier.setValue(self.event['sessions'][index]['timeMultiplier'])
                        self.spinBox_practice_sessionDurationMinutes.setValue(
                            self.event['sessions'][index]['sessionDurationMinutes'])
                        if self.event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_practice_friday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_practice_saturday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_practice_sunday.setChecked(True)

                    if self.event['sessions'][index]['sessionType'] == "Q":
                        self.groupBox_qualify.setChecked(True)
                        self.spinBox_qualify_hourOfDay.setValue(self.event['sessions'][index]['hourOfDay'])
                        self.spinBox_qualify_timeMultiplier.setValue(self.event['sessions'][index]['timeMultiplier'])
                        self.spinBox_qualify_sessionDurationMinutes.setValue(
                            self.event['sessions'][index]['sessionDurationMinutes'])
                        if self.event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_qualify_friday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_qualify_saturday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_qualify_sunday.setChecked(True)

                    if self.event['sessions'][index]['sessionType'] == "R":
                        self.groupBox_race.setChecked(True)
                        self.spinBox_race_hourOfDay.setValue(self.event['sessions'][index]['hourOfDay'])
                        self.spinBox_race_timeMultiplier.setValue(self.event['sessions'][index]['timeMultiplier'])
                        self.spinBox_race_sessionDurationMinutes.setValue(
                            self.event['sessions'][index]['sessionDurationMinutes'])
                        if self.event['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_race_friday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_race_saturday.setChecked(True)
                        elif self.event['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_race_sunday.setChecked(True)

                # set value by session type
                if self.event['sessions'][0]['sessionType'] == "P":
                    initSessison(0)
                    if self.event['sessions'][1]['sessionType'] == "Q":
                        initSessison(1)
                        if len(self.event['sessions']) > 2:
                            initSessison(2)
                    elif self.event['sessions'][1]['sessionType'] == "R":
                        initSessison(1)
                elif self.event['sessions'][0]['sessionType'] == "Q":
                    initSessison(0)
                    if self.event['sessions'][1]['sessionType'] == "R":
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

    # save & start
    # slot which PushButton_start clicked signal
    def serverStart(self):
        # 1. get value from GUI
        # settings.json
        self.settings["serverName"] = self.lineEdit_serverName.text()
        self.settings["password"] = self.lineEdit_password.text()
        self.settings["adminPassword"] = self.lineEdit_adminPassword.text()
        self.settings["spectatorPassword"] = self.lineEdit_spectatorPassword.text()
        self.settings["maxCarSlots"] = self.spinBox_maxCarSlots.value()
        self.settings["trackMedalsRequirement"] = self.spinBox_trackMedalsRequirement.value()
        self.settings["safetyRatingRequirement"] = self.spinBox_safetyRatingRequirement.value()
        self.settings["dumpLeaderboards"] = self.checkBox_dumpLeaderboards.isChecked()
        self.settings["isRaceLocked"] = self.checkBox_isRaceLocked.isChecked()
        self.settings["allowAutoDQ"] = self.checkBox_allowAutoDQ.isChecked()
        self.settings["carGroup"] = self.comboBox_car.currentText()
        self.settings['shortFormationLap'] = self.checkBox_shortFormationLap.isChecked()

        # configuration.json
        self.configuration["maxConnections"] = self.spinBox_maxConnections.value()

        # assistRules.json
        self.assist["disableIdealLine"] = self.checkBox_disableIdealLine.isChecked()
        self.assist["disableAutosteer"] = self.checkBox_disableAutosteer.isChecked()
        self.assist["disableAutoLights"] = self.checkBox_disableAutoLights.isChecked()
        self.assist["disableAutoWiper"] = self.checkBox_disableAutoWiper.isChecked()
        self.assist["disableAutoEngineStart"] = self.checkBox_disableAutoEngineStart.isChecked()
        self.assist["disableAutoPitLimiter"] = self.checkBox_disableAutoPitLimiter.isChecked()
        self.assist["disableAutoGear"] = self.checkBox_disableAutoGear.isChecked()
        self.assist["disableAutoClutch"] = self.checkBox_disableAutoClutch.isChecked()
        self.assist["stabilityControlLevelMax"] = self.horizontalSlider_stabilityControlLevelMax.value()

        # event.json
        self.event["track"] = self.comboBox_track.currentText()
        self.event["preRaceWaitingTimeSeconds"] = self.spinBox_preRaceWaitingTimeSeconds.value()
        self.event["sessionOverTimeSeconds"] = self.spinBox_sessionOverTimeSeconds.value()
        self.event["ambientTemp"] = self.horizontalSlider_ambientTemp.value()
        self.event["weatherRandomness"] = self.horizontalSlider_weatherRandomness.value()
        self.event["cloudLevel"] = self.doubleSpinBox_cloudLevel.value()
        self.event["rain"] = self.doubleSpinBox_rain.value()


        # event.json - Session
        # if loaded event['sessions'] is short and P,Q,R checked
        # add the list to avoid Preventing access to missing list
        if len(self.event['sessions']) < 3:
            if self.groupBox_practice.isChecked():
                if self.groupBox_qualify.isChecked():
                    if self.groupBox_race.isChecked():
                        self.event['sessions'] = self.event['sessions'] + [{
                            "sessionType": "",
                            "hourOfDay": 0,
                            "dayOfWeekend": 0,
                            "timeMultiplier": 0,
                            "sessionDurationMinutes": 0
                        }]



        # avoid the duplication code
        def Practice(index):
            self.event["sessions"][index]["sessionType"] = "P"
            self.event["sessions"][index]["hourOfDay"] = self.spinBox_practice_hourOfDay.value()

            # dayOfWeekend
            if self.radioButton_practice_friday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 1
            elif self.radioButton_practice_saturday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 2
            else:
                self.event["sessions"][index]["dayOfWeekend"] = 3

            self.event["sessions"][index]["timeMultiplier"] = self.spinBox_practice_timeMultiplier.value()
            self.event["sessions"][index][
                "sessionDurationMinutes"] = self.spinBox_practice_sessionDurationMinutes.value()

        def Qualify(index):
            self.event["sessions"][index]["sessionType"] = "Q"
            self.event["sessions"][index]["hourOfDay"] = self.spinBox_qualify_hourOfDay.value()

            # dayOfWeekend
            if self.radioButton_qualify_friday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 1
            elif self.radioButton_qualify_saturday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 2
            else:
                self.event["sessions"][index]["dayOfWeekend"] = 3

            self.event["sessions"][index]["timeMultiplier"] = self.spinBox_qualify_timeMultiplier.value()
            self.event["sessions"][index][
                "sessionDurationMinutes"] = self.spinBox_qualify_sessionDurationMinutes.value()

        def Race(index):
            self.event["sessions"][index]["sessionType"] = "R"
            self.event["sessions"][index]["hourOfDay"] = self.spinBox_race_hourOfDay.value()

            # dayOfWeekend
            if self.radioButton_race_friday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 1
            elif self.radioButton_race_saturday.isChecked():
                self.event["sessions"][index]["dayOfWeekend"] = 2
            else:
                self.event["sessions"][index]["dayOfWeekend"] = 3

            self.event["sessions"][index]["timeMultiplier"] = self.spinBox_race_timeMultiplier.value()
            self.event["sessions"][index][
                "sessionDurationMinutes"] = self.spinBox_race_sessionDurationMinutes.value()

        # if P, Q checked
        if self.groupBox_practice.isChecked():
            if self.groupBox_qualify.isChecked():
                # -- Practice --
                Practice(0)
                # -- Qualify --
                Qualify(1)

        # if P, R checked
        if self.groupBox_practice.isChecked():
            if self.groupBox_qualify.isChecked():
                # -- Practice --
                Practice(0)
                # -- Race --
                Race(1)

        # if Q, R checked
        if self.groupBox_qualify.isChecked():
            if self.groupBox_race.isChecked():
                # -- Qualify --
                Qualify(0)
                # -- Race --
                Race(1)

        # if P, Q, R checked
        if self.groupBox_practice.isChecked():
            if self.groupBox_qualify.isChecked():
                if self.groupBox_race.isChecked():
                    # -- Practice --
                    Practice(0)
                    # -- Qualify --
                    Qualify(1)
                    # -- Race --
                    Race(2)

        # 2. Save json file
        with open('cfg/configuration.json', 'w', encoding='utf-16') as make_file:
            json.dump(self.configuration, make_file, indent="\t")

        with open('cfg/settings.json', 'w', encoding='utf-16') as make_file:
            json.dump(self.settings, make_file, indent="\t")

        with open('cfg/assistRules.json', 'w', encoding='utf-16') as make_file:
            json.dump(self.assist, make_file, indent="\t")

        with open('cfg/event.json', 'w', encoding='utf-16') as make_file:
            json.dump(self.event, make_file, indent="\t")

        # 3. Start server with accServer.exe
        os.system("accServer.exe")


if __name__ == '__main__':
    app = QApplication([])
    ex = Main()
    sys.exit(app.exec_())
