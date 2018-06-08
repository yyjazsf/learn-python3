from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open('data/index.html', 'r') as f:
        content = f.read()
        return content


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # need try
        with open('data/login.html', 'r') as f:
            content = f.read()
            return content
    else:
        # 需要从request对象读取表单内容：
        form = request.form
        success = form['username'] == 'admin' and form['password'] == 'admin'
        return str({
            "success": str(success).lower(),
            "username": request.form['username']
        })


if __name__ == '__main__':
    app.run()
