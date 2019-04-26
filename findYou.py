#플라스크를 불러옵니다.
from flask import Flask
from flask import send_from_directory

#플라스크 앱을 생성합니다.
app = Flask(__name__, static_url_path="/template")

#편의를 위한 디버그 모드를 활성화합니다.
app.debug = True

#URL 경로에 따라 실행할 함수에 디코레이터를 사용합니다. 디코레이터의 파라미터는 URL 경로입니다.
@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory('template', path)

#앞 경로에 접근하면 실행할 함수합니다.
@app.route("/")
def hello():
    return "Hello FindYou!"

#이 파일을 바로 실행할 떄 함께 실행할 코드를 적습니다.
if __name__ == "__main__":
    app.run()
