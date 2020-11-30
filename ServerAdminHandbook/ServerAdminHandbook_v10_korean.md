# I 기본 구성

---

## I.1 구성 파일
서버는 오로지 UTF16-LE 형식의 JSON 파일을 통해 구성됩니다. UTF8 파일 인코딩을 사용하는 것이 효과가 있는 것처럼 보일 수 있지만 잘못된 reading으로 이어질 수 있습니다. 일반적으로 JSON 구문에 사용되거나 [online syntax check](https://jsonformatter.curiousconcept.com/)을 통해 구성을 테스트할 수 있는 것이 좋습니다.
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
|lanDiscovery|서버가 LAN 검색 요청을 수신할지 여부를 정의하세요. Private Server는 이 옵션을 해체할 수 있습니다.|

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
|racecraftRatingRequirement|사용자가 이 서버에 들어올 수 있는 세이프티 레이팅(RC)을 정의합니다. (값 -1,0,..,99)|
|password|이 서버를 입력하는 데 필요한 비밀번호입니다. 비밀번호가 설정되면 서버는 "Private Multiplayer"로 선언됩니다.|
|spectatorPassword|서버를 관전자로써 들어가기 위한 비밀번호입니다. "password"와 같이 둘 다 설정된 경우 "password"랑 달라야 합니다.|
|maxCarSlots|"maxClientsOverride" 및 "spectatorSlots"를 대체합니다. 서버가 점유할 수 있는 차량 슬롯의 양을 규정합니다. this value is overridden if the pit count of the track is lower,Public Multiplayer의 경우 30개로 이 값이 덮어쓰여집니다.|
|dumpLeaderboards|1로 설정하면, 모든 세션의 결과 순위표를 "results" 폴더에 기록합니다 (수동으로 작성되야 합니다). 자세한 건 "Session results"를 참고하세요.|
|isRaceLocked|0으로 설정하면, 레이스 세션동안 누군가 들어오는 것을 허용합니다. 사용자-서버 매칭이 레이스 세션을 무시하므로 "Public Multiplayer"에서는 유용하지 않습니다.|
|randomizeTrackWhenEmpty|1로 설정하면, 마지막 드라이버가 떠날 때 서버가 임의의 트랙으로 변경됩니다(FP1으로 재설정됩니다) "track" 속성은 첫 번째 세션의 기본상태로 정의될 것입니다.|
|centralEntryListPath|다수의 ACC 서버가 있는 하드웨어가 같은 엔트리 목록(및 사용자 지정 차량 파일)을 사용할 수 있도록 기본 엔트리 목록 경로인 "cfg/entrylist.json"으로 덮어쓰기 할 수 있게 해줍니다. 엔트리 목록이 들어가 있는 "C:/customEntryListSeriesA/"와 같은 전체 경로를 설정할 경우 주의하세요: 경로 구분자는 슬래시(/)여야 하며, 백슬래시(\)는 작동하지 않습니다.|
|allowAutoDQ|0으로 설정하면 서버가 자동으로 드라이버가 실격되게 처리하지 않고 대신 Stop&Go(30초) 패널티를 나눠줍니다. 이렇게 하면 서버관리자/레이스 디렉터는 3바퀴를 보면서 검토하고, 그의 판단에 따라 /dq 혹은 /clear를 사용할 수 있습니다|
|shortFormationLap|숏 포메이션 혹은 롱 포메이션 랩을 토글합니다. 롱 포메이션 랩은 Private Server에서만 사용할 수 있습니다.|
|dumpEntryList|예선 세션이 끝나면 엔트리 목록을 저장합니다. 이것은 엔트리 목록을 작성하기 위한 출발점을 빠르게 정할 수 있는 방법이 될 수 있으며, 예선 세션과 미리 정의된 그리드 없이 경기를 실행하는 데 사용할 수 있는 defaultGridPositions을 저장하는 방법이 될 수 있습니다.|
|formationLapType|서버에서 영구적으로 사용되는 포메이션 랩 유형을 전환합니다:<br> 3 – 위치 제어 및 UI가 있는 기본 포메이션 랩<br> 0 – 구식 리미터 랩<br> 1 – free (대체/ 수동 시작), Private Server에서만 사용 가능합니다|

## I.1.3 event.json
서버에서 실행되는 Race Weekend를 정의하십시오. 이 구성 파일은 스왑이 가능하므로 다른 이벤트 템플릿의 이름을 바꾸거나 덮어쓰면 쉽게 전환할 수 있다.

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
|속성|비고|
|---|---|
|track|실행 중인 트랙은 "트랙 이름 목록"을 참조하십시오. 잘못된 값을 설정하면 로그에 사용 가능한 트랙 키도 출력됩니다. 이 트랙을 사용하면 그에 따라 BoP와 트랙 그립이 설정된다.|
|preRaceWaitingTimeSeconds|경기 전 준비 시간. 30초 이하일 수 없습니다.|
|sessionOverTimeSeconds|타이머가 0:00에 도달한 후 세션이 강제로 닫히는 시간. 예상 랩타임의 107%가 권장됩니다(주의: Spa 또는 Silverstone과 같은 트랙은 기본 2분으로 제대로 커버하지 못합니다).|
|ambientTemp|기준 외부 온도(°C) 설정("Race weekend simulation" 참조)|
|trackTemp|잉여옵션: 트랙 온도가 항상 주변 온도, 태양 각도, 구름 및 기타 측면에 기초하여 시뮬레이션됩니다.|
|cloudLevel|기본 구름 레벨(구름이 있는 정도)을 설정하세요. 자세한 건 "Race weekend simulation" 참조. 이 값은 구름 레벨에 큰 영향을 미치고 비가 올 가능성이 생깁니다. 값(0.0, 0.1, … 1.0) |
|rain|weather randomness가 꺼져 있는 경우 정적 강우량을 정의하세요. 동적인 날씨와 함께, weatherRandomneess 값 (0.0, 0.1, ..., 1.0)에 따라 예상 강수량이 정의됩니다.|
|weatherRandomness|동적 날씨 레벨을 설정하세요. 자세한 건 "Race weekend simulation"을 참조하세요.<br>0 = 정적 날씨;<br> 1-4 상당히 현실적인 날씨;<br> 5-7 과장된 날씨|
|postQualySeconds|Q 세션(예선)에서 마지막 드라이버가 종료(또는 sessionOverTimeSeconds가 경과한 후)와 경주가 시작되는 시간. 0으로 설정해서는 안 되며, 그렇지 않으면 그리드 스폰 기능이 안전하지 않습니다.|
|postRaceSeconds|모든 사람이 경주가 끝난 후, 다음 경주가 시작되기 전까지의 추가 시간.|
|sessions|세션 개체 목록, 다음 표를 참조하세요.|
|metaData|결과 출력으로 전송될 사용자 정의 문자열|
|simracerWeatherConditions|Experimental/not supported: 1로 설정하면 최대 비/습도가 최대 값의 약 2/3로 제한되어 중우와 강우 사이로 변환됩니다. 뇌우를 피하기 위해 매우 낮은 cloudLevel과 weatherRandomness 값을 실행해야 한다고 느끼는 경우 유용할 수 있지만, 높은 레벨(0.4+ clouds과 5+ randomness을 결합)은 여전히 심각한 상태를 초래할 수 있습니다.|
|isFixedConditionQualification|Experimental/not supported: 1로 설정하면 서버는 비, 구름, 온도, 빗줄기의 레벨을 그대로 사용하고 설정된 모든 것이 변하지 않도록 됩니다. 주간 전환은 여전히 시작적으로 발생하지만, 온도나 도로 습윤에는 영향을 미치지 않습니다. 또한 rubber/grip은 항상 동일합니다. 이것은 사설 리그 예선 서버에만 사용되도록 의도되었습니다.|
세션 개체는 다음 배열로 표현됩니다:
|Property|Remarks|
|--|--|
|hourOfDay|하루의 세션 시작 시간(값 0 - 23)|
|dayOfWeekend|경기일(1 = 금요일, 2 = 토요일, 3 = 일요일) – 그립 및 날씨 시뮬레이션과 관련이 있습니다.|
|timeMultiplier|세션 시간이 실시간으로 진행되는 속도 배율. 값 0, 1, … 24|
|sessionType|경기 타입: P, Q, R for (P)ractice, (Q)ualy, (R)ace|
|sessionDurationMinutes|세션 기간(분)|
비고:
1) 하나 이상의 비 레이스 세션을 설정해야 합니다
2) 불합리한 주간 및 시간 설정(시간 배율도 고려합니다!)은 잘못된 트랙 및 날씨 행동을 초래할 수 있습니다. 예: 토요일에서 금요일로 점프하지 않는 것

## I.1.4 eventRules.json
피트스톱 규칙을 규정합니다. Public Multiplayer 서버는 이 json 파일을 무시하고 기본값을 사용합니다.

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

|속성|비고|
|---|---|
|qualifyStandingType|1 = fastest lap, 2 = average lap (여러 예선 세션의 내구 레이스에서 실행). 1을 사용하세요. 평균 퀄리파잉은 공식적으로 지원되지 않습니다. |
|pitWindowLengthSec|레이스하는 도중 피트 윈도우를 정의합니다. 이것은 Sprint 시리즈 형식을 다룹니다. -1은 피트 윈도우를 비활성화시킵니다. 이 값은 mandatoryPitstopCount = 1과 함께 사용하세요.|
|driverStintTimeSec|드라이버가 패널티를 받지 않고 주행할 수 있는 최대 시간을 규정합니다. 내구 레이스에서 연료 효율이 높은 자동차의 균형을 맞추기 위해 사용될 수 있습니다. 피트레인의 고정 시간이 재설정되므로 실제 정지가 필요하지 않습니다. -1은 고정 시간을 비활성화합니다. driverStintTimeSec와 maxTotalDrivingTime은 상호의존적인 기능이며, 모두 설정되거나 해제되었는지 확인하십시오.|
|mandatoryPitstopCount|기본 필수 피트 스톱을 규정합니다. 값이 0보다 크면 의무적으로 피트스톱을 실행하지 않은 차량은 경주가 끝날 때 실격됩니다. 피트 스톱에 필요한 조치는 "isMandatoryPitstopXYRequired" 속성을 사용하여 추가로 구성할 수 있습니다. 값이 0이면 기능이 비활성화됩니다.|
|maxTotalDrivingTime|단일 드러바이버의 최대 운전 시간을 제한시킵니다. 이것은 드라이버를 스왑하는 상황에서만 유용하여 각 드라이버에 대해 최소 주행 시간을 강제할 수 있습니다(현실에서 이것은 프로/아마추어와 같은 혼합 팀이 느린 드라이버에게 공정성을 갖도록 하기 위해 사용됩니다) -1은 기능을 비활성화시킵니다. driverStintTimeSec과 maxTotalDrivingTime은 상호의존적인 기능이며, 두 가지 모두 설정 또는 해제되었는지 확인하십시오. "maxDriversCount"에 의해 정의된 팀 크기에 대한 최대 주행 시간을 설정하며, 항상 두 팀 모두 설정되었는지 확인하십시오.|
|maxDriversCount|드라이버 스왑 상황에서는 이 값을 차량의 최대 운전자 수로 설정하십시오. 항목이 maxDriversCount보다 적은 드라이버를 가진 경우, maxTotalDrivingTime은 자동으로 보정되며 "작은" 엔트리들도 레이스를 마칠 수 있습니다. 예: 3시간 레이스에서, driverStintTimeSec가 65분이고 maxTotalDrivingTime이 65분인 경우 각 엔트리들의 maxTotalDrivingTime은 각 3명의 엔트리들에게 maxTotalDrivingTime(최대주행시간)이 65분을, 2명의 엔트리들에겐 105분이란 결과를 가져옵니다.|
|isRefuellingAllowedInRace|레이스 피트 스톱 도중에 주유를 할 수 있는지의 여부를 규정합니다.|
|isRefuellingTimeFixed|true로 설정하면 모든 주유에 동일한 시간이 소요됩니다. false인 경우, 주유는 주유된 양에 선형적으로 시간이 소비됩니다. 특히 다른 특징과 결합할 경우, 연료 효율이 높은 자동차의 균형을 맞추기 위한 매우 유용한 설정입니다.|
|isMandatoryPitstopRefuellingRequired|의무 피트 스톱에 연료 주입이 필요한지 여부를 규정합니다.|
|isMandatoryPitstopTyreChangeRequired|의무 피트 스톱에 타이어 교체가 필요한지 여부를 규정합니다.|
|isMandatoryPitstopSwapDriverRequired|의무 피트 스톱에 드라이버 스왑이 필요한지 여부를 규정합니다. 드라이버 스왑 상황에서만 유효하며, mixed field에서 1인 1조로 편성된 차량에서는 생략합니다.|
|tyreSetCount|Experimental/not supported: 레이스 주간 내내 모든 차량 엔트리에서 타이어 세트의 양을 줄이는데 사용할 수 있습니다. 차량이 서버에 남게 하는 것을 강제할 필요가 있으며, 그렇지 않을경우 다이어 세트를 다시 맞추면 타이어 세트가 재설정되므로 타이어 세트를 대폭 줄여야 효과가 없다는 점에 유의하십시오.|

기본 피트스톱 기능은 비공식 레이스에서 많은 조합과 설정 가능한 측면을 제공합니다. 하지만 모든 조합이 말이 되는 것은 아니므로, 모든 조합은 당신의 책임이 달려있습니다. 드라이버들이 좋은 레이스를 할 수 있도록 규칙을 설정하세요.
단일 스프린트 시리즈 레이스 스타일은 물론 3 - 24시간 내구 레이스를 드라이버 스왑 있이/없이 가능해야 합니다. 물론 이것은 당신이 생각하는 시리즈와 특히 레이스 시간에 대해 제한하면 안되며, 가능한 연료 효율이 높은 자동차의 균형을 맞추기 위해 더 많은 공정성을 더하거나 특정 깊이있는 전략을 넣어주세요.
Stint에 관하여 추가 노트:
- Stint 타이머 (왼쪽 상단 모서리의 timing HUD)는 차량이 피트 엔트리를 지나 출발할 때 재설정 됩니다.
- 패널티가 주어질때, Stint 타이머가 멈추며 피트 아웃후 리셋하지 않고 카운트 됩니다.
- 선수의 남은 총 주행 시간이 현재 정지된 시간보다 적을 때, 총 주행 시간은 Stint 타이머에 덮여쓰여집니다 (!).
이 경우 Stint 타이머의 배경은 빨간색으로 바뀌어 드라이버의 최종 stint를 나타냅니다.
의무 피트 스톱이 있는 이벤트의 경우 driverStintTimeSec 및
maxTotalDrivingTime은 서로 설정하도록 요구하는데, 둘 중 하나가 설정되지 않은 경우 과도하게 안전한 값이 서버에 자동적으로 정해집니다.이벤트가 의도한 대로 실행되도록 하려면 driverStintTimeSec, maxTotalDrivingTime 및 maxDriversCount 값이 경기 길이와 추가 초과타임을 고려하여 모두 설정되었는지 확인하십시오.

## I.1.5 assistRules.json
이 서버에 연결된 모든 차량에 대한 특정 어시스트를 끄는 데 사용할 수 있다. Beware: disabling assists
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
