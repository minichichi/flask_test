from flask import Flask
import random

app  = Flask(__name__)


@app.route('/')
def index():
    return 'random : <strong>'+str(random.random())+'<strong>' # 랜덤한 값 출력

app.run(debug=True) ##debug 모드로 플라스크 실행(플라스크가 꺼졌다가 바로 실행) --> 실제 서비스일 땐 X