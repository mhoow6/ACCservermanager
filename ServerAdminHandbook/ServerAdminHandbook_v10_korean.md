# I 기본 구성

---

## I.1 구성 파일
서버는 오로지 UTF16-LE 형식의 JSON 파일을 통해 구성됩니다. UTF8 파일 인코딩을 사용하는 것이 효과가 있는 것처럼 보일 수 있지만 잘못된 reading으로 이어질 수 있습니다. 일반적으로 JSON 구문에 사용되거나 [online syntax check](https://jsonformatter.curiousconcept.com/)을 통해 당신의 구성을 테스트할 수 있는 것은 좋은 생각입니다.
깨끗하게 새로 시작하려면 .json 파일을 제거하고 서버를 한 번 시작하면 현재 기본값으로 자동 생성됩니다. 또한, 새 속성을 생성하기 위한 각 파일의 configVersion을 줄일 수 있습니다 (모든 구성에서 해당됩니다). 특정 "고급" 세팅은 프로세스가 실행중일때 configVersion 값이 기본 값으로 설정되는 동안 숨겨집니다.
The configuration is split into different files, which represent different levels of what you would possibly like to keep or change frequently:

---

## I.1.1 configuration.json
서버 "아이덴티티"를 절대 변경하지 않는 기술적 설정을 정의합니다.

```python
{
 "udpPort": 9201,
 "tcpPort": 9201,
 "maxConnections": 85,
 "lanDiscovery": 1,
 "registerToLobby": 1,
 "configVersion": 1
}
```
가장 중요하게 알아야 될 것은 두 포트 모두 시스템에서 특별해야합니다, 방화벽은 연결을 허용해야 하고 포트들을 인터넷으로부터 접근 가능하게 해야 합니다.
주의사항: 개인 PC에서 서버를 실행하는 것은 권장되지 않습니다. 개인 시스템에 포트를 열고 전달해야하므로, 임의의 혹은 악의적인 인터넷 트래픽에 취약합니다. 또한 개인 ISP 대역폭은 업로드에서 비대칭적으로 제한되는 경우가 많은데, 이것은 서버 성능을 안 좋게 유도할 수 있고 그 결과 안 좋은 멀티플레이어 경험을 모든 사람들에게 가져다 줄 수 있습니다.

|속성|비고|
|---|---|
|tcpPort|ACC 클라이언트는 서버에 대한 연결을 설정하기 위해 이 포트를 사용합니다.|
|udpPort|연결된 클라이언트는 이 포트를 사용하여 차랑 위치를 스트리밍하고 핑 테스트를 위해 사용합니다. 서버가 ping 값을 얻지 못하는 경우, 이것은 udpPort에 액세스할 수 없음을 나타냅니다.|
|registerToLobby|0 이 되면, 이 서버는 백엔드에 등록되지 않습니다. 이것은 LAN 세션에서 유용합니다. 만약 0이 될 경우, 이 서버는 Private Multiplayer로 선언됩니다.|
|maxConnections|"maxClients"를 대체합니다. 서버가 한 번에 허용할 최대 연결 수를 의미합니다. 만약 하드웨어 서버를 소유하고 있다면, 원하는 숫자를 설정하기만 하면 됩니다. 만약 16 또는 24개의 슬롯 서버를 대여한 경우, 호스트 공급자가 이 구성 파일에 대한 액세스 권한을 부여하지 않을 수도 있습니다.|
|lanDiscovery|서버가 LAN 검색 요청을 수신할지 여부를 정의하세요. 전용 서버가 이 옵션을 해체할 수 있습니다.|

## I.1.2 settings.json
이 설정은 때때로 변경될 수 있는 당신의 개인 서버 설정을 정의하며, 서버 자체도 정의합니다.

```python
{
 "serverName": "Kunos Test Server #03",
 "adminPassword": " adminPw123",
 "carGroup": "GT4",
 "trackMedalsRequirement": 3,
 "safetyRatingRequirement": 49,
 "racecraftRatingRequirement": -1,
 "password": "accessPw123",
"spectatorPassword": "spectPw432",
 "maxCarSlots": 30,
 "dumpLeaderboards": 0,
 "isRaceLocked": 1,
 "randomizeTrackWhenEmpty": 0,
 "centralEntryListPath": "",
 "allowAutoDQ": 1,
 "shortFormationLap": 0,
 "dumpEntryList": 0,
 "formationLapType": 3
}
```
|속성|비고|
|---|---|
|serverName|ACC UI 페이지에 표시되는 서버 이름|
|adminPassword|"서버 관리자 명령"에 승격되기 위한 비밀번호|
|carGroup|이 서버의 차량 그룹을 정의하십시오. 가능한 값은 "FreeForAll", "GT3", "GT4", "Cup", "ST" 이며, "FreeForAll"은 드라이버가 어떤 차량이든 탈 수 있게 합니다 (자신이 직접 고른 차량을 말합니다). GT3, GT4은 차량을 GT3, GT4 클래스로 제한시키며, Cup은 포르쉐 컵카로, ST는 람보르기니 슈퍼트로페오로 제한시킵니다.|
|trackMedalsRequirement|사용자가 해당 트랙에 대해 보유해야 하는 트랙 메달의 양 (값 0, 1, 2, 3)을 정의합니다.|
|safetyRatingRequirement|사용자가 이 서버에 들어올 수 있는 세이프티 레이팅(SA)을 정의합니다. (값 -1,0,..,99)|
|racecraftRatingRequirement|사용자가 이 서버에 들어올 수 있는 세이프티 레이팅(RC))을 정의합니다. (값 -1,0,..,99)|
|password|이 서버를 입력하는 데 필요한 비밀번호입니다. 비밀번호가 설정되면 서버는 "Private Multiplayer"로 선언됩니다.|
|spectatorPassword|서버를 관전자로써 들어가기 위한 비밀번호입니다. "password"와 같이 둘 다 설정된 경우 "password"랑 달라야 합니다.|
|maxCarSlots|"maxClientsOverride" 및 "spectatorSlots"를 대체합니다. 서버가 점유할 수 있는 차량 슬롯의 양을 규정합니다. this value is overridden if the pit count of the track is lower,Public Multiplayer의 경우 30개로 이 값이 덮어쓰여집니다.|
|dumpLeaderboards|1로 설정하면, 모든 세션의 결과 순위표를 "resuluts" 폴더에 기록합니다 (수동으로 작성되야 합니다). 자세한 건 "Session results"를 참고하세요.|
|isRaceLocked|0으로 설정하면, 레이스 세션동안 누군가 들어오는 것을 허용합니다. 사용자-서버 매칭이 레이스 세션을 무시하므로 "Public Multiplayer"에서는 유용하지 않습니다.|
|randomizeTrackWhenEmpty|1로 설정하면, 마지막 드라이버가 떠날 때 서버가 임의의 트랙으로 변경됩니다(FP1으로 재설정됩니다) "track" 속성은 첫 번째 세션의 기본상태로 정의될 것입니다.|
|centralEntryListPath|다수의 ACC 서버가 있는 하드웨어가 같은 엔트리 목록(및 사용자 지정 차량 파일)을 사용할 수 있도록 기본 엔트리 목록 경로인 "cfg/entrylist.json"으로 덮어쓰기 할 수 있게 해줍니다. 엔트리 목록이 들어가 있는 "C:/customEntryListSeriesA/"와 같은 전체 경로를 설정할 경우 주의하세요: 경로 구분자는 슬래시(/)여야 하며, 백슬래시(\)는 작동하지 않습니다.|
|allowAutoDQ|0으로 설정하면 서버가 자동으로 드라이버가 실격되게 처리하지 않고 대신 Stop&Go(30초) 패널티를 나눠줍니다. 이렇게 하면 서버관리자/레이스 디렉터는 3바퀴를 보면서 검토하고, 그의 판단에 따라 /dq 혹은 /clear를 사용할 수 있습니다|
|shortFormationLap|숏 포메이션 혹은 롱 포메이션 랩을 토글합니다. 롱 포메이션 랩은 Private Server에서만 사용할 수 있습니다.|
|dumpEntryList|예선 세션이 끝나면 엔트리 목록을 저장합니다. 이것은 엔트리 목록을 작성하기 위한 출발점을 빠르게 정할 수 있는 방법이 될 수 있으며, 예선 세션과 미리 정의된 그리드 없이 경기를 실행하는 데 사용할 수 있는 defaultGridPositions을 저장하는 방법이 될 수 있습니다.|
|formationLapType|서버에서 영구적으로 사용되는 포메이션 랩 유형을 전환합니다:<br> 3 – 위치 제어 및 UI가 있는 기본 포메이션 랩<br> 0 – 구식 리미터 랩<br> 1 – free (대체/ 수동 시작), Private Server에서만 사용 가능합니다|

## I.1.3 event.json
Defines the race weekend the server runs. This configuration file is meant to be swappable, so you
can easily switch between different event templates by renaming/overwriting them.

```python
{
 "track": "spa",
 "preRaceWaitingTimeSeconds": 60,
 "sessionOverTimeSeconds": 120,
 "ambientTemp": 26,
 "cloudLevel": 0.3,
 "rain": 0.0,
 "weatherRandomness": 3,
 "configVersion": 1,
 "sessions": [
 {
 "hourOfDay": 10,
 "dayOfWeekend": 1,
 "timeMultiplier": 1,
 "sessionType": "P",
 "sessionDurationMinutes": 20
 },
 {
 "hourOfDay": 17,
 "dayOfWeekend": 2,
 "timeMultiplier": 8,
 "sessionType": "Q",
 "sessionDurationMinutes": 10
 },
 {
 "hourOfDay": 16,
 "dayOfWeekend": 3,
 "timeMultiplier": 3,
 "sessionType": "Q",
 "sessionDurationMinutes": 20
 }
 ]
}
```
|Property|Remarks|
|---|---|
|track|The track we run, see “Track name list”. Setting a wrong value will also print out the available track keys in the log. With the 1.1 update containing the 2019 season content, each track has a _2019 variant. Using this track will set the BoP and track grip correspondingly.|
|preRaceWaitingTimeSeconds|Preparation time before a race. Cannot be less than 30s.|
|sessionOverTimeSeconds|Time after that a session is forcibly closing after the timer reached 0:00. Something like 107% of the expected laptime is recommended (careful: default 2 minutes does not properly cover tracks like Spa or Silverstone).|
|ambientTemp|Sets the baseline ambient temperature in °C, see “Race weekend simulation”|
|trackTemp|Obsolete: Track temperatures are always simulated based on ambient temperature, sun angle, clouds and other aspects.|
|cloudLevel|Sets the baseline cloud level, see “Race weekend simulation”. Has large impact on the cloud levels and rain chances. Values (0.0, 0.1, …. 1.0)|
|rain|If weather randomness is off, defines the static rain level. With dynamic weather, it defines the expected rain level, dependent on weatherRandomness Values (0.0, 0.1, …. 1.0)|
|weatherRandomness|Sets the dynamic weather level, see “Race weekend simulation”.<br>0 = static weather;<br> 1-4 fairly realistic weather;<br> 5-7 more sensational|
|postQualySeconds|The time after the last driver is finished (or the sessionOverTimeSeconds passed) in Q sessions and the race start. Should not be set to 0, otherwise grid spawning is not secure.|
|postRaceSeconds|Additional time after the race ended for everyone, before the next race weekend starts.|
|sessions|A list of session objects, see the next table|
|metaData|A user defined string that will be transferred to the result outputs.|
|simracerWeatherConditions|Experimental/not supported: if set to 1, this will limit the maximum rain/wetness to roughly 2/3 of the maximum values, translating to something between medium and heavy rain. It may be useful if you feel forced to run very low cloudLevel and weatherRandomness values just to avoid thunderstorm; however high levels (0.4+ clouds combined with 5+ randomness) will still result in quite serious conditions.|
|isFixedConditionQualification|Experimental/not supported: if set to 1, the server will take the rain, cloud, temperature, rain levels literally and make sure whatever is set up never changes. Daytime transitions still happen visually, but do not affect the temperatures or road wetness. Also rubber/grip is always the same. This is intended  to be used for private league qualification servers only.|

Sessions are expressed as an array of:
|Property|Remarks|
|--|--|
|hourOfDay|Session starting hour of the day (values 0 - 23)|
|dayOfWeekend|Race day (1 = Friday, 2 = Saturday, 3 = Sunday) – relevant to the grip and weather simulation.|
|timeMultiplier|Rate at which the session time advances in realtime.Values 0, 1, … 24|
|sessionType|Race session type: P, Q, R for (P)ractice, (Q)ualy, (R)ace|
|sessionDurationMinutes|Session duration in minutes|

Remarks:
1) At least one non-race session must be set up
2) Setting up unreasonable day and hours (also consider time multipliers!) can lead to wrong
track and weather behaviour, e.g. avoid jumping from Saturday to Friday

## I.1.4 eventRules.json
Defines the pitstop rules. Public MP servers will ignore this json file and use default values

```python
{
 "qualifyStandingType": 1,
 "pitWindowLengthSec": -1,
 "driverStintTimeSec": -1,
 "mandatoryPitstopCount": 0,
 "maxTotalDrivingTime": -1,
 "maxDriversCount": 1,
 "isRefuellingAllowedInRace": true,
 "isRefuellingTimeFixed": false,
 "isMandatoryPitstopRefuellingRequired": false,
 "isMandatoryPitstopTyreChangeRequired": false,
 "isMandatoryPitstopSwapDriverRequired": false,
 "tyreSetCount": 50
}
```

|Property|Remarks|
|---|---|
|qualifyStandingType|1 = fastest lap, 2 = average lap (running Endurance mode for multiple Q sessions). Use 1, averaging Qualy is not yet officially supported.|
|pitWindowLengthSec|Defines a pit window at the middle of the race. Obviously covers the Sprint series format. -1 will disable the pit window. Use this combined with a mandatoryPitstopCount = 1.|
|driverStintTimeSec|Defines the maximum time a driver can stay out without getting a penalty. Can be used to balance fuel efficient cars in endurance races. The stint time resets in the pitlane, no real stop is required. -1 will disable the stint times. driverStintTimeSec and maxTotalDrivingTime are interdependent features, make sure both are set or off.|
|mandatoryPitstopCount|Defines the basic mandatory pit stops. If the value is greater zero, any car that did not execute the mandatory pitstops will be disqualified at the end of the race. The necessary actions can be further configured using the “isMandatoryPitstopXYRequired” properties. A value of zero disables the feature.|
|maxTotalDrivingTime|Restricts the maximum driving time for a single driver. Is only useful for driver swap situations and allows to enforce a minimum driving time for each driver (IRL this is used to make sure mixed teams like Pro/Am have a fair distributions of the slower drivers). -1 disables the feature. driverStintTimeSec and maxTotalDrivingTime are interdependent features, make sure both are set or off. Will set the maximum driving time for the team size defined by “maxDriversCount”, always make sure both are set.|
|maxDriversCount|In driver swap situations, set this to the maximum number of drivers on a car. When an entry has fewer drivers than maxDriversCount maxTotalDrivingTime is automatically compensated so that those "smaller" entries are also able to complete the race Example: 3H race length, 65 minutes driverStintTimeSec and 65 minutes maxTotalDrivingTime will result in 65 minutes of maxTotalDrivingTime for entries of 3 and 105 (!) minutes for entries of 2.|
|isRefuellingAllowedInRace|Defines if refuelling is allowed during the race pitstops.|
|isRefuellingTimeFixed|If set to true, any refuelling will take the same amount of time. If turned off, refuelling will consume time linear to the amount refuelled. Very useful setting to balance fuel efficient cars, especially if combined with other features.|
|isMandatoryPitstopRefuellingRequired|Defines if a mandatory pitstop requires refuelling.|
|isMandatoryPitstopTyreChangeRequired|Defines if a mandatory pitstop requires changing tyres.|
|isMandatoryPitstopSwapDriverRequired|Defines if a mandatory pitstop requires a driver swap. Will only be effective for cars in driver swap situations; even in a mixed field this will be skipped for cars with a team size of 1 driver.|
|tyreSetCount|Experimental/not supported: Can be used to reduce the amount of tyre sets any car entry has for the entire weekend. Please note that it is necessary to force cars to remain in the server, or drastically reduced tyre sets will be ineffective, as rejoining will reset the tyre sets.|

The basic pitstop features offer a huge array of combinations and different aspects you can set up
your non-public races. Not every combination does make sense though, so it’s your responsibility to
setup the rules so drivers have a good experience.
It should be entirely possible to create a race in the style of a single Sprint series race as well as a 3-
24h endurance race with or without driver swaps. Of course this shouldn’t limit you to think about
your series and especially race event durations, and possibly add more fairness to balance fuel
efficient cars – or allow a certain depth of tactics.
Additional notes regarding stints:
- Stint timer (top left corner in the timing HUD) is reset when the car crosses the pit entry and starts
counting down again when crossing the pit exit.
- When serving a penalty, the stint timer will freeze and continue counting down after pit exit
without resetting.
- When a player's total remaining driving time is less than his current stint time, the total driving
time will override the stint timer (!).
When this happens, the stint timer's background turns red, indicating the final stint of the active
driver.
For events with mandatory pitstop rules, the features of driverStintTimeSec and
maxTotalDrivingTime require each other to be set, if one of them is not set, an excessive safe value
is set by the server automatically. In order to make sure your event runs as intended, ensure that driverStintTimeSec, maxTotalDrivingTime, and maxDriversCount values are all set respecting the
race length and any additional overtime.

## I.1.5 assistRules.json
Can be used to turn off certain assists for any car connected to this server. Beware: disabling assists
will effectively remove the effect, but there is no special handling how the assists look like in the
menu. Without instructions, users will be surprised and confused – up to a point where they become
a risk for other drivers. Whenever you think about disabling something, please be sure this is really
necessary and a risk in terms of fairness. It is out of question that the (quite strong) driving aids
“Stability Control” and “Autosteer” may be candidates for league racing, but just turning off the
ideal line will not improve anything for anyone (except that the one driver using it may become less
safe and ruins the race of others). Even innocent elements like auto-engine start and pit limiter may
just force users to re-map their wheels, and for example lose the ability to use their indicators in
lapping traffic – again nobody is winning in this scenario.
For (very) obvious reasons, public MP servers will ignore this json file and allow everything.

```python
{
 "stabilityControlLevelMax": 25,
 "disableAutosteer": 1,
 "disableAutoLights": 0,
 "disableAutoWiper": 0,
 "disableAutoEngineStart": 0,
 "disableAutoPitLimiter": 0,
 "disableAutoGear": 0,
 "disableAutoClutch": 0,
 "disableIdealLine": 0
}
```

|Property|Remarks|
|---|---|
|stabilityControlLevelMax|Set’s the maximum % of SC that can be used. In case a client has a higher SC set than allowed by the server, he will only run what is allowed (25%in this example). Obviously setting this property to 0 removes all SC, including mouse and keyboard users. The Stability Control is an artificial driving aid that allows the car to act out of the physics boundaries, and highly recommended to overcome input methods like Keyboards, Gamepads and Mouse steering. However, there is a built-in effect that makes the SC performance inferior, so in theory using (and relying) on SC is already more than enough penalty, and the way to improve performance is to practice driving without. Default: 100|
|disableAutosteer|Disables the steering aid that is only available for gamepad controllers. Unlike SC, this works inside the physics and does not allow unrealistic driving behaviour – except that this is a very strong aid with superhuman feeling for grip and high reaction speed. There is a built-in penalty that should balance the driving performance in most cases, and give an incentive to learn not to use the driving aid. Default: 0|
|disableAutoLights|Forces the equivalent assist option to “off”|
|disableAutoWiper|Forces the equivalent assist option to “off”|
|disableAutoEngineStart|Forces the equivalent assist option to “off”|
|disableAutoPitLimiter|Forces the equivalent assist option to “off”|
|disableAutoGear|Forces the equivalent assist option to “off”|
|disableAutoClutch|Forces the equivalent assist option to “off”|
|disableIdealLine|Forces the equivalent assist option to “off”|
---
# II Appendix
---
## II.1 Track name list with slots
Note: Public MP is limited to unique pit box OR 30 at max.
|Value|Unique pit boxes|Private server slots|
|---|---|---|
|monza|29|60|
|zolder|34|50|
|brands_hatch|32|50|
|sliverstone|36|50|
|paul_ricard|33|60|
|misano|30|50|
|spa|82|82|
|nurburgring|30|50|
|barcelona|29|50|
|hungaroring|27|50|
|zandvoort|25|50|
|monza_2019|29|60|
|zolder_2019|34|50|
|brands_hatch_2019|32|50|
|silverstone_2019|36|50|
|paul_ricard_2019|33|60|
|misano_2019|30|50|
|spa_2019|82|82|
|nurburgring_2019|30|50|
|barcelona_2019|29|50|
|hungaroring_2019|27|50|
|zandvoort_2019|25|50|
|kyalami_2019|40|50|
|mount_panorama_2019|36|50|
|suzuka_2019|51|105|
|laguna_seca_2019|30|50|
|monza_2020|29|60|
|zolder_2020|34|50|
|brands_hatch_2020|32|50|
|silverstone_2020|36|50|
|paul_ricard_2020|33|60|
|misano_2020|30|50|
|spa_2020|82|82|
|nurburgring_2020|30|50|
|barcelona_2020|29|50|
|hungaroring_2020|27|50|
|zandvoort_2020|25|50|
|imola_2020|30|50|
---
## II.1 Car model list
|Value|Car model|
|---|---|
|0|Porsche 991 GT3 R|
|1|Mercedes-AMG GT3|
|2|Ferrari 488 GT3|
|3|Audi R8 LMS|
|4|Lamborghini Huracan GT3|
|5|McLaren 650S GT3|
|6|Nissan GT-R Nismo GT3 2018|
|7|BMW M6 GT3|
|8|Bentley Continental GT3 2018|
|9|Porsche 991II GT3 Cup|
|10|Nissan GT-R Nismo GT3 2017|
|11|Bentley Continental GT3 2016|
|12|Aston Martin V12 Vantage GT3|
|13|Lamborghini Gallardo R-EX|
|14|Jaguar G3|
|15|Lexus RC F GT3|
|16|Lamborghini Huracan Evo (2019)|
|17|Honda NSX GT3|
|18|Lamborghini Huracan SuperTrofeo|
|19|Audi R8 LMS Evo (2019)|
|20|AMR V8 Vantage (2019)|
|21|Honda NSX Evo (2019)|
|22|McLaren 720S GT3 (2019)|
|23|Porsche 911II GT3 R (2019)|
|24|Ferrari 488 GT3 Evo 2020|
|25|Mercedes-AMG GT3 2020|
|50|Alpine A110 GT4|
|51|AMR V8 Vantage GT4|
|52|Audi R8 LMS GT4|
|53|BMW M4 GT4|
|55|Chevrolet Camaro GT4|
|56|Ginetta G55 GT4|
|57|KTM X-Bow GT4|
|58|Maserati MC GT4|
|59|McLaren 570S GT4|
|60|Mercedes-AMG GT4|
|61|Porsche 718 Cayman GT4|
---
# III. Session results
---
## III.1 Result files
Using the “dumpLeaderboards”: 1 option, any session that is finished will write the final standing
into a .json file in the “results” folder. Those files are generated with a filename in the pattern of
“190806_193009_R.json”, including date, time and session type (P, Q, R).

```python
{
   "sessionType":"R",
   "trackName":"silverstone",
   "sessionIndex":1,
   "sessionResult":{
      "bestlap":117915,
      "bestSplits":[
         34770,
         49359,
         33258
      ],
      "isWetSession":0,
      "type":1,
      "leaderBoardLines":[
         {
            "car":{
               "carId":1073,
               "raceNumber":912,
               "carModel":0,
               "cupCategory":0,
               "teamName":"",
               "drivers":[
                  {
                     "firstName":"Somebody",
                     "lastName":"Else",
                     "shortName":"SOE",
                     "playerId":"S76561191111111111"
                  }
               ]
            },
            "currentDriver":{
               "firstName":"Somebody",
               "lastName":"Else",
               "shortName":"SOE",
               "playerId":"S76561191111111111"
            },
            "currentDriverIndex":0,
            "timing":{
               "lastLap":119223,
               "lastSplits":[
                  35286,
                  50178,
                  33759
               ],
               "bestLap":118404,
               "bestSplits":[
                  35265,
                  49659,
                  33438
               ],
               "totalTime":719894,
               "lapCount":6,
               "lastSplitId":0
            },
            "missingMandatoryPitstop":0,
            "driverTotalTimes":[
               0.0
            ]
         },
         "..."
      ]
   },
   "laps":[
      {
         "carId":1073,
         "driverIndex":0,
         "laptime":125511,
         "isValidForBest":true,
         "splits":[
            40197,
            51537,
            33777
         ]
      },
      "..."
   ],
   "penalties":[
      {
         "carId":1079,
         "driverIndex":0,
         "reason":"Cutting",
         "penalty":"DriveThrough",
         "penaltyValue":3,
         "violationInLap":0,
         "clearedInLap":1
      },
      {
         "carId":1081,
         "driverIndex":0,
         "reason":"PitSpeeding",
         "penalty":"StopAndGo_20",
         "penaltyValue":20,
         "violationInLap":4,
         "clearedInLap":5
      }
   ]
}
```
---
# IV Server admin commands

While connected to a server (both as driver and spectator), users can elevate to “server admins” if
they are aware of the password. That allows them to use a few special commands. Version 1.0 start
with a limited set, which is expected to be extended in future versions.
To elevate to admin, hit “enter” to use the chat and type
**/admin adminPw123**
A notification will tell you if successful. Additionally, you can setup an “Entry lists” entry for the
admin(s) steamids.

Once elevated, you can use several commands:
|Command|Parameters|Remarks|
|---|---|---|
|/next||Skips the current session|
|/restart||Restarts the current session. Do not use this during the preparation phase|
|/kick|car race<br>number|Kicks a user from the server, preventing him to join again until the race weekend restarts|
