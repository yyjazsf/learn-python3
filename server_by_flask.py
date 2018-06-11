from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 需要从request对象读取表单内容：
        form = request.form
        success = form['username'] == 'admin' and form['password'] == 'admin'
        if success:
            return render_template('index.html', message="登录成功", username=form['username'])
        else:
            return render_template('login.html', message="账号密码错误", username=form['username'])


if __name__ == '__main__':
    app.run()
