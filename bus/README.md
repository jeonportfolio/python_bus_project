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