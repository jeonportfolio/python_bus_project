# 사회적 약자를 위한 버스 예약 사이트

★파이썬 이용 api  실시간 버스정보 조회 서비스 <br/>
★공공데이터 포털에서 공개 api 사용 -> 서울 정류장 정보 조회 <br/>
★flask서버 설치 후 flask서버에서 구동 (테스트) `pip install flask` -> index.py에서 구동<br/>
★카카오맵 연동 -> Place Service 활용 (장소 입력 검색, 장소 결과 추출)<br/>
★ JQUERY cdn 사용 <br/>

## 가상서버 작동
 ★ cd python_bus_projects<br/>
 ★ cd bus(가상폴더)<br/>
 ★ cd Scripts<br/>
 ★ activate 실행 후 ../로 다시 bus 폴더로 이동 <br/>
 ★  flask --app index run --port 80 로 flask 가상서버 실행<br/>
 ★  주소창에 localhost 입력<br/>

 ## 서비스 구조 

 ★ 공공데이터포털 API -> index.py(서버) -> index.html (프론트)<br/>
 ★ html 에서는 ajax로 python 서버의 정보를 받는다 (json형태로 받아야 함) <br/>
 ★ 동기요청으로 받음 

 ## 공공데이터 포털 API 사용 
 ★ getBusPosByRtidList <br/>
 ★서울특별시_정류소정보조회 서비스 -> getStationByUidItem -> 현재 정류장의 실시간 버스 도착 예정시간 -> arrmsg1 첫번째도착 정보 버스 메세지 <br/>
 ★ center 함수를 통해 xml형식으로 위도와 경도 좌표 받아오기 -> parser<br/>
 ★ getRouteByStationList -> 정류소 고유번호 노선목록 조회<br/>
 ★ getRoutePathList -> 노선의 지도상 경로를 리턴한다 <br/>
 ★ getBusPosByRtidList -> 노선ID로 차량들의 위치 정보를 조회한다.(경도, 위도, 차량번호,차량ID)<br/>
 ★ getStationByUiditem -> 정류소고유번호를 입력받아 버스도착 정보를 조회한다.(도착정보, 노선 ID)<br/>
 ★ getStationsByRouteList -> 노선별 경유 정류소 조회 서비스 <br/>

## 카카오 map API 사용 
★`https://apis.map.kakao.com/ios_v2/`<br/>
★ 키워드로 장소검색하고 목록으로 표출하기  -> kakao.maps.services.Places()<br/>
★ api 키 뒤에 &libraries=services 추가 <br/>
★ displayPlaces(data) 좌표찍기  <br/>

 ## 마커 표시 <br/>
 ★ addMarker 함수 사용<br/>
 ★ 현재 위도와 경도를 받아 지도에 kakao 마커를 이용해서 표시<br/>
 ★ 마커 정보 보기창 (즉시 실행 함수) 사용 <br/>


 ## 팝업 띄우기 & 탭 <br/>

 ★ `bPopup cdn` 제이쿼리 사용<br/>
 ★ marker에 'arsId, lat, lnt' 저장해서 속성전달<br/>
 ★ for 문을 활용하여 각각의 아이템 출력<br/>
 ★ `jqueryui/tabs`로 탭창 설정 -> 탭 클릭으로 두번째 탭 설정 가능<br/>

 ## 버스 정보 띄우기 

 ★ kakao.maps.customoverlay를 활용 <br/>
 ★ 현재 정류소 순번 파악, 구간 ID 에서의 현재 버스 순번, 남은 구간 계산 <br/>
 ★ 버스 노선별 정보 확인 API 활용

 

 
