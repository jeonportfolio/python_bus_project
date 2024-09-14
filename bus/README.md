파이썬 이용 api  실시간 버스정보 조회 서비스

공공데이터 포털에서 공개 api 사용 -> 서울 정류장 정보 조회 

flask서버 설치 후 flask서버에서 구동 

카카오맵 연동 -> Place Service 활용 (장소 입력 검색, 장소 결과 추출)

## 가상서버 작동
 ->cd python_bus_projects
 ->cd bus(가상폴더)
 ->cd Scripts
 ->activate 실행 후 ../로 다시 bus 폴더로 이동 
 -> flask --app index run --port 80 로 flask 가상서버 실행
 -> 주소창에 localhost 입력

 ## 서비스 구조 

 -> 공공데이터포털 API -> index.py(서버) -> index.html (프론트)
 -> html 에서는 ajax로 python 서버의 정보를 받는다 

 ## 공공데이터 포털 API 사용 
 -> getBusPosByRtidList 

 ->서울특별시_정류소정보조회 서비스 -> getStationByUidItem -> 현재 정류장의 실시간 버스 도착 예정시간 -> arrmsg1 첫번째도착 정보 버스 메세지 




 ## 현재위치 표시 
 -> 현재 위도와 경도를 받아 지도에 kakao 마커를 이용해서 표시

 ## 도착지 설정 

 

 
