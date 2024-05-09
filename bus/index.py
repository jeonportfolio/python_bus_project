from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0 #정적파일캐싱 방지
app.config["TEMPLATES_AUTO_RELOAD"] = True #flask 서버에서는 바로 업데이트가 안되기 때문에 자동 업데이트 설정 

@app.route("/")
def home():
    return render_template("index.html")

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