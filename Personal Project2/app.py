from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/codes', methods=['POST'])
def write_codes():
    title_receive = request.form['title_give']
    code_receive = request.form['code_give']
    trouble_receive = request.form['trouble_give']
    date_receive = request.form['date_give']

    code = {
       'title': title_receive,
       'code': code_receive,
       'trouble': trouble_receive,
       'date': date_receive
    }

    db.codes.insert_one(code)
    return jsonify({'result': 'success', 'msg': 'Code Saved'})


@app.route('/codes', methods=['GET'])
def read_codes():
    codes = list(db.codes.find({},{'_id':0}))
    return jsonify({'result': 'success', 'codes': codes})


if __name__ == '__main__':
    app.run('localhost', port=8000, debug=True)