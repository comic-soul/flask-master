#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: 人海中的海盗
import os

from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1130221300@qq.com'
app.config['MAIL_PASSWORD'] = 'iflthvxkjsjzgdji'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/hello_world')
def hello_world():
    return "hello world！！！"

@app.route('/send_mail')
def send_mail():
    msg = Message('Hello', sender='1130221300@qq.com', recipients=['yushangyong520@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>')
def redirect_url(name):
    if name == 'hello':
        return redirect(url_for('hello_world'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)

        # 拼接完整的保存路径
        file_path = os.path.join('uploads', secure_filename(f.filename))

        # 保存文件
        f.save(file_path)
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
