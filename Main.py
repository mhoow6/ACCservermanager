from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import Ui_MainWindow
import sys, subprocess, os, json
from tkinter import messagebox as msg
from tkinter import Tk
from io import StringIO
from contextlib import suppress

# >pyuic5 -x E:\github\ACCservermanager\ACC_Dedicated_Server_GUI.ui -o E:\github\ACCservermanager\GUI.py
# pyinstaller -w -F --icon=E:\github\ACCservermanager\icon.ico E:\github\ACCservermanager\Main.py

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.fileCheck()

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
            self.spinBox_postQualySeconds.setToolTip(
                'Q 세션(예선)에서 마지막 드라이버가 종료 후 경주가 시작되는 시간.\n'
                '0으로 설정해서는 안 되며, 그렇지 않으면 그리드 스폰 기능이 안전하지 않습니다.'
            )
            self.spinBox_postRaceSeconds.setToolTip(
                '모든 사람이 경주가 끝난 후, 다음 경주가 시작되기 전까지의 추가 시간.'
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
                '레이스하는 도중 의무 피트할 수 있는 시간(피트 윈도우)을 정의합니다.\n'
                '이것은 Sprint 시리즈 형식을 다룹니다. -1은 피트 윈도우를\n'
                '비활성화시킵니다.이 값은 의무 피트스톱 횟수와 함께 사용하세요.\n'
                '-1 = 피트 윈도우 비활성화\n'
                '600 = 600초(10분) 동안에만 피트 윈도우 활성화'
            )
            self.spinBox_driverStintTimeSec.setToolTip(
                '드라이버가 패널티를 받지 않고 주행할 수 있는 최대 시간을 규정합니다.\n'
                '내구 레이스에서 연료 효율이 높은 자동차의 균형을 맞추기 위해 사용될 수\n'
                '있습니다. 피트레인의 고정 시간이 재설정되므로 실제 정지가 필요하지\n'
                '않습니다. -1은 고정 시간을 비활성화합니다. 스틴트 시간과 최대\n'
                '운전 시간은 상호의존적인 기능이며, 모두 설정되거나 해제되었는지\n'
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

        # settings.json
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
                with suppress(KeyError):
                    self.lineEdit_serverName.setText(self.settings['serverName'])
                with suppress(KeyError):
                    self.lineEdit_password.setText(self.settings['password'])
                with suppress(KeyError):
                    self.lineEdit_adminPassword.setText(self.settings['adminPassword'])
                with suppress(KeyError):
                    self.lineEdit_spectatorPassword.setText(self.settings['spectatorPassword'])
                with suppress(KeyError):
                    self.spinBox_maxCarSlots.setValue(self.settings['maxCarSlots'])
                with suppress(KeyError):
                    self.spinBox_trackMedalsRequirement.setValue(self.settings['trackMedalsRequirement'])
                with suppress(KeyError):
                    self.spinBox_safetyRatingRequirement.setValue(self.settings['safetyRatingRequirement'])
                with suppress(KeyError):
                    self.checkBox_dumpLeaderboards.setChecked(self.settings['dumpLeaderboards'])
                with suppress(KeyError):
                    self.checkBox_isRaceLocked.setChecked(self.settings['isRaceLocked'])
                with suppress(KeyError):
                    self.checkBox_allowAutoDQ.setChecked(self.settings['allowAutoDQ'])
                with suppress(KeyError):
                    self.comboBox_car.setCurrentText(self.settings['carGroup'])
                with suppress(KeyError):
                    self.checkBox_shortFormationLap.setChecked(self.settings['shortFormationLap'])
                with suppress(KeyError):
                    self.checkBox_dumpEntryList.setChecked(self.settings['dumpEntryList'])
                with suppress(KeyError):
                    self.checkBox_randomizeTrackWhenEmpty.setChecked(self.settings['randomizeTrackWhenEmpty'])

                # formationLapType Logic
                try:
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
                except KeyError:
                    pass

        except FileNotFoundError:
            with open("cfg/settings.json", 'w', encoding='UTF-16') as make_file:
                settings_init = {
                    "serverName": "",
                    "adminPassword": "",
                    "password": "",
                    "spectatorPassword": "",
                    "centralEntryListPath": "",
                    "carGroup": "FreeForAll",
                    "trackMedalsRequirement": 0,
                    "safetyRatingRequirement": -1,
                    "racecraftRatingRequirement": -1,
                    "maxCarSlots": 10,
                    "isRaceLocked": 0,
                    "isLockedPrepPhase": 0,
                    "shortFormationLap": 1,
                    "dumpLeaderboards": 0,
                    "dumpEntryList": 0,
                    "randomizeTrackWhenEmpty": 0,
                    "allowAutoDQ": 0,
                    "formationLapType": 3,
                    "configVersion": 1
                }
                json.dump(settings_init, make_file, indent="\t")

        # configuration.json
        try:
            with(open("cfg/configuration.json", encoding="UTF-16")) as configuration:
                # load json file
                self.configuration = json.load(configuration)

                # looking json file
                # io = StringIO()
                # json.dump(self.configuration, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                with suppress(KeyError): self.spinBox_maxConnections.setValue(self.configuration['maxConnections'])
                with suppress(KeyError): self.lcdNumber_tcpPort.display(self.configuration['tcpPort'])
                with suppress(KeyError): self.lcdNumber_udpPort.display(self.configuration['udpPort'])
                with suppress(KeyError): self.checkBox_registerToLobby.setChecked(self.configuration['registerToLobby'])
                with suppress(KeyError): self.checkBox_lanDiscovery.setChecked(self.configuration['lanDiscovery'])

        except FileNotFoundError:
            with open("cfg/configuration.json", 'w', encoding='UTF-16') as make_file:
                configuration_init = {
                    "udpPort": 9201,
                    "tcpPort": 9202,
                    "maxConnections": 30,
                    "lanDiscovery": 0,
                    "registerToLobby": 1,
                    "configVersion": 1
                }
                json.dump(configuration_init, make_file, indent="\t")

        # assistRules.json
        try:
            with open("cfg/assistRules.json", encoding='UTF-16') as assist:
                # load json file
                self.assist = json.load(assist)

                # looking json file
                # io = StringIO()
                # json.dump(self.assist, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                with suppress(KeyError): self.checkBox_disableIdealLine.setChecked(self.assist['disableIdealLine'])
                with suppress(KeyError): self.checkBox_disableAutosteer.setChecked(self.assist['disableAutosteer'])
                with suppress(KeyError): self.checkBox_disableAutoLights.setChecked(self.assist['disableAutoLights'])
                with suppress(KeyError): self.checkBox_disableAutoWiper.setChecked(self.assist['disableAutoWiper'])
                with suppress(KeyError): self.checkBox_disableAutoEngineStart.setChecked(
                    self.assist['disableAutoEngineStart'])
                with suppress(KeyError): self.checkBox_disableAutoPitLimiter.setChecked(
                    self.assist['disableAutoPitLimiter'])
                with suppress(KeyError): self.checkBox_disableAutoGear.setChecked(self.assist['disableAutoGear'])
                with suppress(KeyError): self.checkBox_disableAutoClutch.setChecked(self.assist['disableAutoClutch'])
                with suppress(KeyError): self.horizontalSlider_stabilityControlLevelMax.setValue(
                    self.assist['stabilityControlLevelMax'])

        except FileNotFoundError:
            with open("cfg/assistRules.json", 'w', encoding='UTF-16') as make_file:
                assistRules_init = {
                    "disableIdealLine": 0,
                    "disableAutosteer": 0,
                    "stabilityControlLevelMax": 100,
                    "disableAutoPitLimiter": 0,
                    "disableAutoGear": 0,
                    "disableAutoClutch": 0,
                    "disableAutoEngineStart": 0,
                    "disableAutoWiper": 0,
                    "disableAutoLights": 0
                }
                json.dump(assistRules_init, make_file, indent="\t")

        # event.json
        try:
            with open("cfg/event.json", encoding='UTF-16') as event:
                # load json file
                self.event = json.load(event)

                # looking json file
                # io = StringIO()
                # json.dump(self.event, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                with suppress(KeyError):
                    self.comboBox_track.setCurrentText(self.event['track'])
                with suppress(KeyError):
                    self.spinBox_preRaceWaitingTimeSeconds.setValue(self.event['preRaceWaitingTimeSeconds'])
                with suppress(KeyError):
                    self.spinBox_sessionOverTimeSeconds.setValue(self.event['sessionOverTimeSeconds'])
                with suppress(KeyError):
                    self.horizontalSlider_ambientTemp.setValue(self.event['ambientTemp'])
                with suppress(KeyError):
                    self.lcdNumber_ambientTemp.display(self.event['ambientTemp'])
                with suppress(KeyError):
                    self.horizontalSlider_weatherRandomness.setValue(self.event['weatherRandomness'])
                with suppress(KeyError):
                    self.lcdNumber_weatherRandomness.display(self.event['weatherRandomness'])
                with suppress(KeyError):
                    self.doubleSpinBox_cloudLevel.setValue(self.event['cloudLevel'])
                with suppress(KeyError):
                    self.doubleSpinBox_rain.setValue(self.event['rain'])
                with suppress(KeyError):
                    self.spinBox_postQualySeconds.setValue(self.event['postQualySeconds'])
                with suppress(KeyError):
                    self.spinBox_postRaceSeconds.setValue(self.event['postRaceSeconds'])

                # set value Session's value
                def initSessison(book, index):
                    if book['sessions'][index]['sessionType'] == "P":
                        self.groupBox_practice.setChecked(True)
                        self.spinBox_practice_hourOfDay.setValue(book['sessions'][index]['hourOfDay'])
                        self.spinBox_practice_timeMultiplier.setValue(
                            book['sessions'][index]['timeMultiplier'])
                        self.spinBox_practice_sessionDurationMinutes.setValue(
                            book['sessions'][index]['sessionDurationMinutes'])
                        if book['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_practice_friday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_practice_saturday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_practice_sunday.setChecked(True)

                    if book['sessions'][index]['sessionType'] == "Q":
                        self.groupBox_qualify.setChecked(True)
                        self.spinBox_qualify_hourOfDay.setValue(book['sessions'][index]['hourOfDay'])
                        self.spinBox_qualify_timeMultiplier.setValue(
                            book['sessions'][index]['timeMultiplier'])
                        self.spinBox_qualify_sessionDurationMinutes.setValue(
                            book['sessions'][index]['sessionDurationMinutes'])
                        if book['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_qualify_friday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_qualify_saturday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_qualify_sunday.setChecked(True)

                    if book['sessions'][index]['sessionType'] == "R":
                        self.groupBox_race.setChecked(True)
                        self.spinBox_race_hourOfDay.setValue(book['sessions'][index]['hourOfDay'])
                        self.spinBox_race_timeMultiplier.setValue(book['sessions'][index]['timeMultiplier'])
                        self.spinBox_race_sessionDurationMinutes.setValue(
                            book['sessions'][index]['sessionDurationMinutes'])
                        if book['sessions'][index]['dayOfWeekend'] == 1:
                            self.radioButton_race_friday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 2:
                            self.radioButton_race_saturday.setChecked(True)
                        elif book['sessions'][index]['dayOfWeekend'] == 3:
                            self.radioButton_race_sunday.setChecked(True)

                # set value by session type
                try:
                    if self.event['sessions'][0]['sessionType'] == "P":
                        initSessison(self.event, 0)
                        if self.event['sessions'][1]['sessionType'] == "Q":
                            initSessison(self.event, 1)
                            if len(self.event['sessions']) > 2:
                                initSessison(self.event, 2)
                        elif self.event['sessions'][1]['sessionType'] == "R":
                            initSessison(self.event, 1)
                    elif self.event['sessions'][0]['sessionType'] == "Q":
                        initSessison(self.event, 0)
                        if self.event['sessions'][1]['sessionType'] == "R":
                            initSessison(self.event, 1)
                except KeyError:
                    pass

        except FileNotFoundError:
            with open("cfg/event.json", 'w', encoding='UTF-16') as make_file:
                event_init = {
                    "track": "mount_panorama_2019",
                    "preRaceWaitingTimeSeconds": 80,
                    "sessionOverTimeSeconds": 120,
                    "ambientTemp": 22,
                    "cloudLevel": 0.1,
                    "rain": 0.0,
                    "weatherRandomness": 1,
                    "sessions": [
                        {
                            "hourOfDay": 6,
                            "dayOfWeekend": 2,
                            "timeMultiplier": 1,
                            "sessionType": "P",
                            "sessionDurationMinutes": 10
                        },
                        {
                            "hourOfDay": 12,
                            "dayOfWeekend": 2,
                            "timeMultiplier": 1,
                            "sessionType": "Q",
                            "sessionDurationMinutes": 10
                        },
                        {
                            "hourOfDay": 18,
                            "dayOfWeekend": 3,
                            "timeMultiplier": 2,
                            "sessionType": "R",
                            "sessionDurationMinutes": 20
                        }
                    ],
                    "configVersion": 1
                }
                json.dump(event_init, make_file, indent="\t")

        # eventRules.json
        try:
            with open("cfg/eventRules.json", encoding='UTF-16') as eventRules:
                # load json file
                self.eventRules = json.load(eventRules)

                # looking json file
                # io = StringIO()
                # json.dump(self.eventRules, io, indent="\t")
                # print(io.getvalue())

                # set value from json file
                with suppress(KeyError): self.spinBox_pitWindowLengthSec.setValue(self.eventRules["pitWindowLengthSec"])
                with suppress(KeyError): self.spinBox_driverStintTimeSec.setValue(self.eventRules["driverStintTimeSec"])
                with suppress(KeyError): self.spinBox_mandatoryPitstopCount.setValue(
                    self.eventRules["mandatoryPitstopCount"])
                with suppress(KeyError): self.spinBox_maxTotalDrivingTime.setValue(
                    self.eventRules["maxTotalDrivingTime"])
                with suppress(KeyError): self.spinBox_maxDriversCount.setValue(self.eventRules["maxDriversCount"])
                with suppress(KeyError): self.spinBox_tyreSetCount.setValue(self.eventRules["tyreSetCount"])
                with suppress(KeyError): self.checkBox_isRefuellingAllowedInRace.setChecked(
                    self.eventRules["isRefuellingAllowedInRace"])
                with suppress(KeyError): self.checkBox_isRefuellingTimeFixed.setChecked(
                    self.eventRules["isRefuellingTimeFixed"])
                with suppress(KeyError): self.checkBox_isMandatoryPitstopRefuellingRequired.setChecked(
                    self.eventRules["isMandatoryPitstopRefuellingRequired"])
                with suppress(KeyError): self.checkBox_isMandatoryPitstopTyreChangeRequired.setChecked(
                    self.eventRules["isMandatoryPitstopTyreChangeRequired"])
                with suppress(KeyError): self.checkBox_isMandatoryPitstopSwapDriverRequired.setChecked(
                    self.eventRules["isMandatoryPitstopSwapDriverRequired"])

        except FileNotFoundError:
            with open("cfg/eventRules.json", 'w', encoding='UTF-16') as make_file:
                eventRules_init = {
                    "qualifyStandingType": 1,
                    "pitWindowLengthSec": -1,
                    "driverStintTimeSec": -1,
                    "mandatoryPitstopCount": 0,
                    "maxTotalDrivingTime": -1,
                    "maxDriversCount": 1,
                    "tyreSetCount": 50,
                    "isRefuellingAllowedInRace": 0,
                    "isRefuellingTimeFixed": 0,
                    "isMandatoryPitstopRefuellingRequired": 0,
                    "isMandatoryPitstopTyreChangeRequired": 0,
                    "isMandatoryPitstopSwapDriverRequired": 0
                }
                json.dump(eventRules_init, make_file, indent="\t")

    # Necessary file check
    def fileCheck(self):
        root = Tk()
        root.withdraw()

        message = "accServer.exe를 찾을 수 없습니다. 프로그램을 \'Assetto Corsa Competizione Dedicated Server\server\' 경로에 넣어주세요."

        if not os.path.exists('./accServer.exe'):
            msg.showerror("accServer.exe is not found", message=message)
            sys.exit()

        if not os.path.isdir("./cfg"):
            os.mkdir("./cfg")

    # Click signals slot from PushButton_start
    def serverStart(self):
        # At least one non-race session must be set up
        if not self.groupBox_practice.isChecked() and not self.groupBox_qualify.isChecked():
            root = Tk()
            root.withdraw()

            message = "하나 이상의 비 레이스 세션을 설정해야 합니다."
            msg.showerror("Session Error", message=message)

        else:
            # 1. get value from GUI
            # settings.json
            settings_end = {"serverName": self.lineEdit_serverName.text(),
                            "password": self.lineEdit_password.text(),
                            "adminPassword": self.lineEdit_adminPassword.text(),
                            "spectatorPassword": self.lineEdit_spectatorPassword.text(),
                            "maxCarSlots": self.spinBox_maxCarSlots.value(),
                            "trackMedalsRequirement": self.spinBox_trackMedalsRequirement.value(),
                            "safetyRatingRequirement": self.spinBox_safetyRatingRequirement.value(),
                            "dumpLeaderboards": int(self.checkBox_dumpLeaderboards.isChecked()),
                            "isRaceLocked": int(self.checkBox_isRaceLocked.isChecked()),
                            "allowAutoDQ": int(self.checkBox_allowAutoDQ.isChecked()),
                            "carGroup": self.comboBox_car.currentText(),
                            'shortFormationLap': int(self.checkBox_shortFormationLap.isChecked()),
                            'dumpEntryList': int(self.checkBox_dumpEntryList.isChecked()),
                            'randomizeTrackWhenEmpty': int(self.checkBox_randomizeTrackWhenEmpty.isChecked())}

            # formationLapType logic
            if self.comboBox_formationLapType.currentText() == self.formationLapTypelist[2]:
                settings_end['formationLapType'] = 3
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[0]:
                settings_end['formationLapType'] = 0
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[1]:
                settings_end['formationLapType'] = 1
            elif self.comboBox_formationLapType.currentText() == self.formationLapTypelist[3]:
                settings_end['formationLapType'] = 4
            else:
                settings_end['formationLapType'] = 5

            # configuration.json
            configuration_end = {'maxConnections': self.spinBox_maxConnections.value(),
                                 'registerToLobby': int(self.checkBox_registerToLobby.isChecked()),
                                 'lanDiscovery': int(self.checkBox_lanDiscovery.isChecked())}

            # assistRules.json
            assist_end = {"disableIdealLine": int(self.checkBox_disableIdealLine.isChecked()),
                          "disableAutosteer": int(self.checkBox_disableAutosteer.isChecked()),
                          "disableAutoLights": int(self.checkBox_disableAutoLights.isChecked()),
                          "disableAutoWiper": int(self.checkBox_disableAutoWiper.isChecked()),
                          "disableAutoEngineStart": int(self.checkBox_disableAutoEngineStart.isChecked()),
                          "disableAutoPitLimiter": int(self.checkBox_disableAutoPitLimiter.isChecked()),
                          "disableAutoGear": int(self.checkBox_disableAutoGear.isChecked()),
                          "disableAutoClutch": int(self.checkBox_disableAutoClutch.isChecked()),
                          "stabilityControlLevelMax": self.horizontalSlider_stabilityControlLevelMax.value()}

            # event.json
            event_end = {"track": self.comboBox_track.currentText(),
                         "preRaceWaitingTimeSeconds": self.spinBox_preRaceWaitingTimeSeconds.value(),
                         "sessionOverTimeSeconds": self.spinBox_sessionOverTimeSeconds.value(),
                         "ambientTemp": self.horizontalSlider_ambientTemp.value(),
                         "weatherRandomness": self.horizontalSlider_weatherRandomness.value(),
                         "cloudLevel": self.doubleSpinBox_cloudLevel.value(),
                         "rain": self.doubleSpinBox_rain.value(),
                         "postQualySeconds": self.spinBox_postQualySeconds.value(),
                         "postRaceSeconds": self.spinBox_postRaceSeconds.value(),
                         "sessions": []}

            # event.json - Session
            if self.groupBox_practice.isChecked():
                if self.radioButton_practice_friday.isChecked():
                    dow = 1
                elif self.radioButton_practice_saturday.isChecked():
                    dow = 2
                elif self.radioButton_practice_sunday.isChecked():
                    dow = 3
                event_end["sessions"].append({
                    "sessionType": "P",
                    "hourOfDay": self.spinBox_practice_hourOfDay.value(),
                    "timeMultiplier": self.spinBox_practice_timeMultiplier.value(),
                    "sessionDurationMinutes": self.spinBox_practice_sessionDurationMinutes.value(),
                    "dayOfWeekend": dow
                })

            if self.groupBox_qualify.isChecked():
                if self.radioButton_qualify_friday.isChecked():
                    dow = 1
                elif self.radioButton_qualify_saturday.isChecked():
                    dow = 2
                elif self.radioButton_qualify_sunday.isChecked():
                    dow = 3
                event_end["sessions"].append({
                    "sessionType": "Q",
                    "hourOfDay": self.spinBox_qualify_hourOfDay.value(),
                    "timeMultiplier": self.spinBox_qualify_timeMultiplier.value(),
                    "sessionDurationMinutes": self.spinBox_qualify_sessionDurationMinutes.value(),
                    "dayOfWeekend": dow
                })
            if self.groupBox_race.isChecked():
                if self.radioButton_race_friday.isChecked():
                    dow = 1
                elif self.radioButton_race_saturday.isChecked():
                    dow = 2
                elif self.radioButton_race_sunday.isChecked():
                    dow = 3
                event_end["sessions"].append({
                    "sessionType": "R",
                    "hourOfDay": self.spinBox_race_hourOfDay.value(),
                    "timeMultiplier": self.spinBox_race_timeMultiplier.value(),
                    "sessionDurationMinutes": self.spinBox_race_sessionDurationMinutes.value(),
                    "dayOfWeekend": dow
                })

            # eventRules.json
            eventRules_end = {"pitWindowLengthSec": self.spinBox_pitWindowLengthSec.value(),
                              "driverStintTimeSec": self.spinBox_driverStintTimeSec.value(),
                              "mandatoryPitstopCount": self.spinBox_mandatoryPitstopCount.value(),
                              "maxTotalDrivingTime": self.spinBox_maxTotalDrivingTime.value(),
                              "maxDriversCount": self.spinBox_maxDriversCount.value(),
                              "tyreSetCount": self.spinBox_tyreSetCount.value(),
                              "isRefuellingAllowedInRace": self.checkBox_isRefuellingAllowedInRace.isChecked(),
                              "isRefuellingTimeFixed": self.checkBox_isRefuellingTimeFixed.isChecked(),
                              "isMandatoryPitstopRefuellingRequired": self.checkBox_isMandatoryPitstopRefuellingRequired.isChecked(),
                              "isMandatoryPitstopTyreChangeRequired": self.checkBox_isMandatoryPitstopTyreChangeRequired.isChecked(),
                              "isMandatoryPitstopSwapDriverRequired": self.checkBox_isMandatoryPitstopSwapDriverRequired.isChecked()}

            # 2. Save json file
            with open('cfg/configuration.json', 'w', encoding='utf-16') as make_file:
                json.dump(configuration_end, make_file, indent="\t")

            with open('cfg/settings.json', 'w', encoding='utf-16') as make_file:
                json.dump(settings_end, make_file, indent="\t")

            with open('cfg/assistRules.json', 'w', encoding='utf-16') as make_file:
                json.dump(assist_end, make_file, indent="\t")

            with open('cfg/event.json', 'w', encoding='utf-16') as make_file:
                json.dump(event_end, make_file, indent="\t")

            with open('cfg/eventRules.json', 'w', encoding='utf-16') as make_file:
                json.dump(eventRules_end, make_file, indent="\t")

            # 3. Start server with accServer.exe
            subprocess.Popen('accServer.exe', close_fds=True)

            # 4. enable and disable
            self.pushButton_exit.setEnabled(True)
            self.pushButton_start.setEnabled(False)

    # Click signal slot from PushButton_exit
    def serverStop(self):
        # 1. kill accServer.exe
        subprocess.Popen('taskkill /f /im accServer.exe', close_fds=True)

        # 2. enable and disable
        self.pushButton_exit.setEnabled(False)
        self.pushButton_start.setEnabled(True)

    # When you clicked "X" button
    def closeEvent(self, QCloseEvent) -> None:
        # kill the accServer.exe also
        subprocess.Popen('taskkill /f /im accServer.exe', close_fds=True)


if __name__ == '__main__':
    app = QApplication([])
    ex = Main()
    sys.exit(app.exec_())
