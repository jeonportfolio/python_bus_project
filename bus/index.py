from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0 #정적파일캐싱 방지
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/busstationservice", methods=['POST'])
def get_station_by_pos():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    x = data['x']
    y = data['y']

    # 외부 API로부터 데이터 가져오기
    url = " http://apis.data.go.kr/6410000/busstationservice"
    params = {
        'serviceKey': "nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==",
        'x': x,
        'y': y,
        'radius': "500"  #반경 (단위: 미터)
    }

    response = requests.get(url, params=params)
    return response.content, response.status_code   