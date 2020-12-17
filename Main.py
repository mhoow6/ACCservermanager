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

        self.accServerCheck()

        self.setupUi(self)

        self.initUI()

        self.show()

    # Initalize the Graphic User Interface
    def initUI(self):

        def initTooltip(self):
            self.lineEdit_password.setToolTip(
                '이 서버를 입력하는 데 필요한 비밀번호입니다.\n'
                '비밀번호가 설정되면 서버는 "Private Multiplayer"로\n'
                '선언됩니다.'
            )
            self.lineEdit_spectatorPassword.setToolTip(
                '서버를 관전자로써 들어가기 위한 비밀번호입니다.\n'
                '비밀번호와 같이 둘 다 설정된 경우 비밀번호랑\n'
                '달라야 합니다.'
            )
            self.spinBox_maxConnections.setToolTip(
                '"maxClients"를 대체합니다. 서버가 한 번에 허용할\n'
                '최대 연결 수를 의미합니다. 만약 하드웨어 서버를\n'
                '소유하고 있다면, 원하는 숫자를 설정하기만\n'
                '하면 됩니다. 만약 16 또는 24개의 슬롯 서버를\n'
                '대여한 경우, 호스트 공급자가 이 구성 파일에 대한\n'
                '액세스 권한을 부여하지 않을 수도 있습니다.'
            )
            self.spinBox_maxCarSlots.setToolTip(
                '"maxClientsOverride" 및 "spectatorSlots"를\n'
                '대체합니다. 서버가 점유할 수 있는 차량 슬롯의\n'
                '양을규정합니다. this value is overridden if the\n'
                'pit count of the track is lower, Public\n'
                'Multiplayer의 경우 30개로 이 값이 덮어쓰여집니다.'
            )
            self.checkBox_dumpLeaderboards.setToolTip(
                '체크를 하게되면, 모든 세션의 결과 순위표를\n'
                '"results" 폴더에 기록합니다.'
            )
            self.checkBox_dumpEntryList.setToolTip(
                '1로 설정하면, 모든 세션의 결과 순위표를 "results"\n'
                '폴더에 기록합니다 (수동으로 작성되야 합니다).'
            )
            self.checkBox_allowAutoDQ.setToolTip(
                '체크를 해제하면 서버가 자동으로 드라이버가\n'
                '실격되게 처리하지 않고 대신 Stop&Go(30초)\n'
                '패널티를 나눠줍니다. 이렇게 하면 서버관리자/레이스\n'
                '디렉터는 3바퀴를 보면서 검토하고, 그의 판단에 따라\n'
                '/dq 혹은 /clear를 사용할 수 있습니다'
            )
            self.checkBox_registerToLobby.setToolTip(
                '체크를 안 하면, 이 서버는 백엔드에 등록되지 않습니다.\n'
                '백엔드에 등록을 안 할 경우 LAN으로 연결되지 않는\n'
                '네트워크에서는 서버가 보이지 않습니다. 이 옵션에 대해서\n'
                '이해가 안 가시면 그냥 체크를 하시면 됩니다.\n'
                '이것은 LAN 세션에서만 유용한 옵션입니다. 만약 0이 될 경우,\n'
                '이 서버는 Private Multiplayer로 선언됩니다.'
            )
            self.checkBox_lanDiscovery.setToolTip(
                '서버가 LAN 검색 요청을 수신할지 여부를 정의하세요.\n'
                'Private Server는 이 옵션을 해체할 수 있습니다.'
            )
            self.checkBox_randomizeTrackWhenEmpty.setToolTip(
                '체크하면, 마지막 드라이버가 떠날 때 서버가 임의의 트랙으로\n'
                '변경됩니다(FP1으로 재설정됩니다)\n'
                '"track" 속성은 첫 번째 세션의 기본상태로 정의될 것입니다.'
            )
            self.checkBox_shortFormationLap.setToolTip(
                '숏 포메이션 혹은 롱 포메이션 랩을 토글합니다.\n'
                '롱 포메이션 랩은 Private Server에서만 사용할\n'
                '수 있습니다.'
            )
            self.comboBox_formationLapType.setToolTip(
                '서버에서 영구적으로 사용되는 포메이션 랩 유형을 전환합니다:\n'
                '3 – 위치 제어 및 UI가 있는 기본 포메이션 랩\n'
                '0 – 구식 리미터랩\n'
                '1 – free (대체/ 수동 시작), Private Server에서만 사용 가능합니다'
            )
            self.spinBox_preRaceWaitingTimeSeconds.setToolTip(
                '경기 전 준비 시간. 30초 이하일 수 없습니다.'
            )
            self.spinBox_sessionOverTimeSeconds.setToolTip(
                '타이머가 0:00에 도달한 후 세션이 강제로 닫히는 시간(초).\n'
                '예상 랩타임의 107%가 권장됩니다(주의: Spa 또는 Silver\n'
                'stone과 같은 트랙은 기본 2분으로 제대로 커버하지 못합니다).'
            )
            self.horizontalSlider_weatherRandomness.setToolTip(
                '동적 날씨 레벨을 설정하세요.\n'
                '0 = 정적 날씨\n'
                '1-4 상당히 현실적인 날씨\n'
                '5-7 과장된 날씨'
            )
            self.doubleSpinBox_cloudLevel.setToolTip(
                '기본 구름 레벨(구름이 있는 정도)을 설정하세요.\n'
                '이 값은 구름이 있는 정도에 큰 영향을 미치고 비가\n'
                '올 가능성이 생기게 합니다.'
            )
            self.doubleSpinBox_rain.setToolTip(
                '날씨 변동성이 꺼져 있는 경우 정적 강우량을 정의하세요.\n'
                '동적인 날씨와 함께, 날씨 변동성 값에 따라 예상 강수량이\n'
                '정의됩니다.'
            )
            self.spinBox_practice_hourOfDay.setToolTip(
                '하루의 세션 시작 시간(시)'
            )
            self.spinBox_practice_timeMultiplier.setToolTip(
                '세션 시간이 실시간으로 진행되는 속도 배율.'
            )
            self.spinBox_practice_sessionDurationMinutes.setToolTip(
                '세션 기간(분)'
            )
            self.groupBox_practice.setToolTip(
                '불합리한 주간 및 시간 설정은 잘못된 트랙 및 날씨 행동을\n'
                '초래할 수 있습니다. 예: 토요일에서 금요일로 점프하는 것'
            )
            self.spinBox_qualify_hourOfDay.setToolTip(
                '하루의 세션 시작 시간(시)'
            )
            self.spinBox_qualify_timeMultiplier.setToolTip(
                '세션 시간이 실시간으로 진행되는 속도 배율.'
            )
            self.spinBox_qualify_sessionDurationMinutes.setToolTip(
                '세션 기간(분)'
            )
            self.groupBox_qualify.setToolTip(
                '불합리한 주간 및 시간 설정은 잘못된 트랙 및 날씨 행동을\n'
                '초래할 수 있습니다. 예: 토요일에서 금요일로 점프하는 것'
            )
            self.spinBox_race_hourOfDay.setToolTip(
                '하루의 세션 시작 시간(시)'
            )
            self.spinBox_race_timeMultiplier.setToolTip(
                '세션 시간이 실시간으로 진행되는 속도 배율.'
            )
            self.spinBox_race_sessionDurationMinutes.setToolTip(
                '세션 기간(분)'
            )
            self.groupBox_race.setToolTip(
                '불합리한 주간 및 시간 설정은 잘못된 트랙 및 날씨 행동을\n'
                '초래할 수 있습니다. 예: 토요일에서 금요일로 점프하는 것'
            )
            self.spinBox_mandatoryPitstopCount.setToolTip(
                '기본 필수 피트 스톱 횟수를 규정합니다. 값이 0보다 크면\n'
                '의무적으로 피트스톱을 실행하지 않은 차량은 경주가 끝날 때\n'
                '실격됩니다. 값이 0이면 기능이 비활성화됩니다.'
            )
            self.spinBox_pitWindowLengthSec.setToolTip(
                '레이스하는 도중 피트 시간을 정의합니다. 이것은 Sprint\n'
                '시리즈 형식을 다룹니다. -1은 피트 윈도우를 비활성화시킵니다.\n'
                '이 값은 의무 피트스톱 횟수와 함께 사용하세요.'
            )
            self.spinBox_driverStintTimeSec.setToolTip(
                '드라이버가 패널티를 받지 않고 주행할 수 있는 최대 시간을 규정합니다.\n'
                '내구 레이스에서 연료 효율이 높은 자동차의 균형을 맞추기 위해 사용될 수\n'
                '있습니다. 피트레인의 고정 시간이 재설정되므로 실제 정지가 필요하지\n'
                '않습니다. -1은 고정 시간을 비활성화합니다. 최소 스틴트 시간과 최대\n'
                '스틴트 시간은 상호의존적인 기능이며, 모두 설정되거나 해제되었는지\n'
                '확인하십시오.'
            )
            self.spinBox_maxTotalDrivingTime.setToolTip(
                '단일 차량의 최대 운전 시간을 제한시킵니다. 이것은 드라이버를 스왑하는\n'
                '상황에서만 유용하여 각 드라이버에 대해 최소 주행 시간을 강제할 수\n'
                '있습니다(현실에서 이것은 프로/아마추어와 같은 혼합 팀이 느린 드라이버에게\n'
                '공정성을 갖도록 하기 위해 사용됩니다) -1은 기능을 비활성화시킵니다.\n'
                '최소 스틴트 시간과 최대 스틴트 시간은 상호의존적인 기능이며, 두 가지 모두\n'
                '설정 또는 해제되었는지 확인하십시오. "스틴트 운전자 수"에 의해 정의된\n'
                '팀 크기에 대한 최대 주행 시간을 설정하며, 항상 두 팀 모두 설정되었는지\n'
                '확인하십시오.'
            )
            self.spinBox_maxDriversCount.setToolTip(
                '드라이버 스왑 상황에서는 이 값을 차량의 최대 운전자 수로 설정하십시오.\n'
                '항목이 스틴트 운전자 수보다 적은 드라이버를 가진 경우, 최대 스틴트 시간은\n'
                '자동으로 보정되며 "작은" 엔트리들도 레이스를 마칠 수 있습니다.\n'
                '예: 3시간 레이스에서, 최소 스틴트 시간이 65분이고 최대 스틴트 시간이\n'
                '65분인 경우 각 3명의 엔트리들에게 최대 스틴트 시간 65분을, 2명의\n'
                '엔트리들에겐 105분이란 결과를 가져옵니다.'
            )
            self.spinBox_tyreSetCount.setToolTip(
                'Experimental/not supported: 레이스 주간 내내 모든 차량 엔트리에서\n'
                '타이어 세트의 양을 줄이는데 사용할 수 있습니다. 차량이 서버에 남게 하는 것을\n'
                '강제할 필요가 있으며, 그렇지 않을경우 다이어 세트를 다시 맞추면 타이어 세트가\n'
                '재설정되므로 타이어 세트를 대폭 줄여야 효과가 없다는 점에 유의하십시오.'
            )
            self.horizontalSlider_stabilityControlLevelMax.setToolTip(
                '사용할 수 있는 안정성 컨트롤의 최대 % 설정. 클라이언트가\n'
                '서버에서 허용하는 것보다 더 높은 안정성 컨트롤 세트를 가지고 있는 경우,\n'
                '서버에서 "최대 안정성 컨트롤"이 지정된 값만큼 됩니다.\n'
                '이 속성을 0으로 설정하면 마우스와 키보드 사용자를 포함해서 모든 안정성 컨트롤이\n'
                '제거가 됩니다. 안정성 컨트롤은 자동차가 물리학적 경계를 벗어나 동작할 수 있도록\n'
                '하는 인공 운전 보조 장치로, 키보드, 게임패드, 마우스 조향 등의 입력방식을 하는\n'
                '유저들이 도움을 받을 수 있도록하는 것이 적극 권장됩니다. 그러나 (자신이 하는)안정성\n'
                '컨트롤 퍼포먼스를 저하시킬 수 있는 간접 효과가 있기 때문에 이론상으로는 안정성 컨트롤에\n'
                '의존하는 것은 이미 충분한 패널티보다 더하고, 퍼포먼스를 향상시키는 방법은 안정성 컨트롤\n'
                '없이 운전을 연습하는 것입니다. 기본값: 100'
            )


        initTooltip(self)

        tracklist = [
            'monza', 'zolder', 'brands_hatch', 'sliverstone', 'paul_ricard', 'misano', 'spa', 'nurburgring',
            'barcelona', 'hungaroring', 'zandvoort', 'monza_2019', 'zolder_2019', 'brands_hatch_2019',
            'silverstone_2019', 'paul_ricard_2019', 'misano_2019', 'spa_2019', 'nurburgring_2019', 'barcelona_2019',
            'hungaroring_2019', 'zandvoort_2019', 'kyalami_2019', 'mount_panorama_2019', 'suzuka_2019',
            'laguna_seca_2019', 'monza_2020', 'zolder_2020', 'brands_hatch_2020', 'silverstone_2020',
            'paul_ricard_2020', 'misano_2020', 'spa_2020', 'nurburgring_2020', 'barcelona_2020',
            'hungaroring_2020', 'zandvoort_2020', 'imola_2020'
        ]

        carlist = ["FreeForAll", "GT3", "GT4", "Cup", "ST"]

        self.formationLapTypelist = ['구식', '수동', '기본', '수동 + 고스트 1랩', '기본 + 고스트1랩']

        self.comboBox_track.addItems(tracklist)
        self.comboBox_car.addItems(carlist)
        self.comboBox_formationLapType.addItems(self.formationLapTypelist)

        try:
            with open("cfg/settings.json", encoding='UTF-16') as settings:
                # load json file
                self.settings = json.load(settings)

                # looking json file
                # io = StringIO()
                # json.dump(self.settings, io, indent="\t")
                # print(io.getvalue())
                # print(type(settings))

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
                self.checkBox_dumpEntryList.setChecked(self.settings['dumpEntryList'])
                self.checkBox_randomizeTrackWhenEmpty.setChecked(self.settings['randomizeTrackWhenEmpty'])

                # formationLapType Logic
                if self.settings['formationLapType'] == 3:
                    self.comboBox_formationLapType.setCurrentText(self.formationLapTypelist[2])
                elif self.settings['formationLapType'] == 0:
                    self.comboBox_formationLapType.setCurrentText(self.formationLapTypelist[0])
                elif self.settings['formationLapType'] == 1:
                    self.comboBox_formationLapType.setCurrentText(self.formationLapTypelist[1])
                elif self.settings['formationLapType'] == 4:
                    self.comboBox_formationLapType.setCurrentText(self.formationLapTypelist[3])
                else:
                    self.comboBox_formationLapType.setCurrentText(self.formationLapTypelist[4])

        except FileNotFoundError:
            print("cfg/settings.json is not found")

        try:
            with(open("cfg/configuration.json", encoding="UTF-16")) as configuration:
                # load json file
                self.configuration = json.load(configuration)

                # looking json file
                # io = StringIO()
                # json.dump(self.configuration, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                self.spinBox_maxConnections.setValue(self.configuration['maxConnections'])
                self.lcdNumber_tcpPort.display(self.configuration['tcpPort'])
                self.lcdNumber_udpPort.display(self.configuration['udpPort'])
                self.checkBox_registerToLobby.setChecked(self.configuration['registerToLobby'])
                self.checkBox_lanDiscovery.setChecked(self.configuration['lanDiscovery'])

        except FileNotFoundError:
            print("cfg/configuration.json is not found")

        try:
            with open("cfg/assistRules.json", encoding='UTF-16') as assist:
                # load json file
                self.assist = json.load(assist)

                # looking json file
                # io = StringIO()
                # json.dump(self.assist, io, indent="\t")
                # print(io.getvalue())

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
                # io = StringIO()
                # json.dump(self.event, io, indent="\t")
                # print(io.getvalue())

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

        try:
            with open("cfg/eventRules.json", encoding='UTF-16') as eventRules:
                # load json file
                self.eventRules = json.load(eventRules)

                # looking json file
                # io = StringIO()
                # json.dump(self.eventRules, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                self.spinBox_pitWindowLengthSec.setValue(self.eventRules["pitWindowLengthSec"])
                self.spinBox_driverStintTimeSec.setValue(self.eventRules["driverStintTimeSec"])
                self.spinBox_mandatoryPitstopCount.setValue(self.eventRules["mandatoryPitstopCount"])
                self.spinBox_maxTotalDrivingTime.setValue(self.eventRules["maxTotalDrivingTime"])
                self.spinBox_maxDriversCount.setValue(self.eventRules["maxDriversCount"])
                self.spinBox_tyreSetCount.setValue(self.eventRules["tyreSetCount"])
                self.checkBox_isRefuellingAllowedInRace.setChecked(self.eventRules["isRefuellingAllowedInRace"])
                self.checkBox_isRefuellingTimeFixed.setChecked(self.eventRules["isRefuellingTimeFixed"])
                self.checkBox_isMandatoryPitstopRefuellingRequired.setChecked(
                    self.eventRules["isMandatoryPitstopRefuellingRequired"])
                self.checkBox_isMandatoryPitstopTyreChangeRequired.setChecked(
                    self.eventRules["isMandatoryPitstopTyreChangeRequired"])
                self.checkBox_isMandatoryPitstopSwapDriverRequired.setChecked(
                    self.eventRules["isMandatoryPitstopSwapDriverRequired"])

        except FileNotFoundError:
            print("cfg/eventRules.json is not found")

    # Is accServer.exe in directory?
    def accServerCheck(self):
        root = Tk()
        root.withdraw()

        message = "accServer.exe를 찾을 수 없습니다. 프로그램을 \'Assetto Corsa Competizione Dedicated Server\server\' 경로에 넣어주세요."

        if not os.path.exists('./accServer.exe'):
            msg.showerror("accServer.exe is not found", message=message)
            raise Exception("accServer.exe is not found")

    # Slot corresponding to click signals from PushButton_start
    def serverStart(self):
        # print("Server Start!")
        # At least one non-race session must be set up
        if not self.groupBox_practice.isChecked() and not self.groupBox_qualify.isChecked():
            root = Tk()
            root.withdraw()

            message = "하나 이상의 비 레이스 세션을 설정해야 합니다."
            msg.showerror("Session Error", message=message)

        else:
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
            self.settings['dumpEntryList'] = self.checkBox_dumpEntryList.isChecked()
            self.settings['randomizeTrackWhenEmpty'] = self.checkBox_randomizeTrackWhenEmpty.isChecked()

            # formationLapType logic
            if self.comboBox_formationLapType.currentText() == self.formationLapTypelist[2]:
                self.settings['formationLapType'] = 3
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[0]:
                self.settings['formationLapType'] = 0
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[1]:
                self.settings['formationLapType'] = 1
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[3]:
                self.settings['formationLapType'] = 4
            else:
                self.settings['formationLapType'] = 5

            # configuration.json
            self.configuration["maxConnections"] = self.spinBox_maxConnections.value()
            self.settings['registerToLobby'] = self.checkBox_registerToLobby.isChecked()
            self.settings['lanDiscovery'] = self.checkBox_lanDiscovery.isChecked()

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
            # if loaded event['sessions'] is short when P,Q,R checked
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

            # eventRules.json
            self.eventRules["pitWindowLengthSec"] = self.spinBox_pitWindowLengthSec.value()
            self.eventRules["driverStintTimeSec"] = self.spinBox_driverStintTimeSec.value()
            self.eventRules["mandatoryPitstopCount"] = self.spinBox_mandatoryPitstopCount.value()
            self.eventRules["maxTotalDrivingTime"] = self.spinBox_maxTotalDrivingTime.value()
            self.eventRules["maxDriversCount"] = self.spinBox_maxDriversCount.value()
            self.eventRules["tyreSetCount"] = self.spinBox_tyreSetCount.value()
            self.eventRules["isRefuellingAllowedInRace"] = self.checkBox_isRefuellingAllowedInRace.isChecked()
            self.eventRules["isRefuellingTimeFixed"] = self.checkBox_isRefuellingTimeFixed.isChecked()
            self.eventRules[
                "isMandatoryPitstopRefuellingRequired"] = self.checkBox_isMandatoryPitstopRefuellingRequired.isChecked()
            self.eventRules[
                "isMandatoryPitstopTyreChangeRequired"] = self.checkBox_isMandatoryPitstopTyreChangeRequired.isChecked()
            self.eventRules[
                "isMandatoryPitstopSwapDriverRequired"] = self.checkBox_isMandatoryPitstopSwapDriverRequired.isChecked()

            # 2. Save json file
            with open('cfg/configuration.json', 'w', encoding='utf-16') as make_file:
                json.dump(self.configuration, make_file, indent="\t")

            with open('cfg/settings.json', 'w', encoding='utf-16') as make_file:
                json.dump(self.settings, make_file, indent="\t")

            with open('cfg/assistRules.json', 'w', encoding='utf-16') as make_file:
                json.dump(self.assist, make_file, indent="\t")

            with open('cfg/event.json', 'w', encoding='utf-16') as make_file:
                json.dump(self.event, make_file, indent="\t")

            with open('cfg/eventRules.json', 'w', encoding='utf-16') as make_file:
                json.dump(self.eventRules, make_file, indent="\t")

            # 3. Start server with accServer.exe
            os.popen('accServer.exe')

            # 4. enable and disable
            self.pushButton_exit.setEnabled(True)
            self.pushButton_start.setEnabled(False)

    # Slot corresponding to click signals from PushButton_exit
    def serverStop(self):
        # 1. kill accServer.exe
        # print(os.system('tasklist'))
        os.system('taskkill /f /im accServer.exe')
        # print(os.system('tasklist'))

        # 2. enable and disable
        self.pushButton_exit.setEnabled(False)
        self.pushButton_start.setEnabled(True)

    # when you clicked "X" button
    def closeEvent(self, QCloseEvent) -> None:
        # kill the accServer.exe also
        os.system('taskkill /f /im accServer.exe')


if __name__ == '__main__':
    app = QApplication([])
    ex = Main()
    sys.exit(app.exec_())
