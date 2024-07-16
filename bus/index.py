from flask import Flask, render_template, request, send_from_directory
import requests, os


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0 #정적파일캐싱 방지
app.config["TEMPLATES_AUTO_RELOAD"] = True #flask 서버에서는 바로 업데이트가 안되기 때문에 자동 업데이트 설정 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/templates/<path:filename>")
def template_files(filename):
    # templates 디렉토리 안의 파일을 안전하게 서비스
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/getStationByPos", methods=['POST'])
def get_station_by_pos():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    tmX = data['tmX']
    tmY = data['tmY']

    # 외부 API로부터 데이터 가져오기
    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos"
    params = {
        'serviceKey': "nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==",
        'tmX': tmX,
        'tmY': tmY,
        'radius': "500"  #반경 (단위: 미터)
    }

    response = requests.get(url, params=params)
    return response.content, response.status_code   

@app.route("/getRouteByStation", methods=['POST'])
def get_route_by_station():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    arsId = data['arsId']
    # 외부 API로부터 데이터 가져오기
    url = " http://ws.bus.go.kr/api/rest/stationinfo/getRouteByStation"
    params = {
        'serviceKey': "nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==",
        'arsId': arsId,
        'radius': "500"  #반경 (단위: 미터)
    }

    response = requests.get(url, params=params)
    return response.content, response.status_code  


@app.route("/getRoutePath", methods=['POST'])
def get_route_path():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    busRouteId = data['busRouteId']

    # 외부 API로부터 데이터 가져오기
    url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getRoutePath"
    params = {
        'serviceKey': "nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==",
        'busRouteId': busRouteId,
        'radius': "500"  #반경 (단위: 미터)
    }

    response = requests.get(url, params=params)
    return response.content, response.status_code      


@app.route("/getBusPosByRtid", methods=['POST'])
def get_bus_pos_rtid():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    busRouteId = data['busRouteId']

    # 외부 API로부터 데이터 가져오기
    url = "http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid"
    params = {
        'serviceKey': "nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==",
        'busRouteId': busRouteId,
    }

    response = requests.get(url, params=params)
    return response.content, response.status_code          