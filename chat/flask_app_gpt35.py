# -*- coding: utf-8 -*-
import json
import sys
import os
import openai
sys.path.append(os.path.dirname(os.getcwd()))
from flask import Flask, render_template, request, jsonify
import time
import threading
openai.api_key = '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'

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0.4,
            presence_penalty=0.3,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0].text

"""
定义心跳检测函数
"""

def heartbeat():
    print(time.strftime('%Y-%m-%d %H:%M:%S - heartbeat', time.localtime(time.time())))
    timer = threading.Timer(60, heartbeat)
    timer.start()


timer = threading.Timer(60, heartbeat)
timer.start()

"""
ElementTree在 Python 标准库中有两种实现。
一种是纯 Python 实现例如 xml.etree.ElementTree ，
另外一种是速度快一点的 xml.etree.cElementTree 。
 尽量使用 C 语言实现的那种，因为它速度更快，而且消耗的内存更少
"""

app = Flask(__name__, static_url_path="/static")


@app.route('/message', methods=['POST'])
# """定义应答函数，用于获取输入信息并返回相应的答案"""
def reply():
    # 从请求中获取输入信息
    req_msg = request.form['msg']

    # 调用decode_line对生成回答信息
    res_msg = generate_response(req_msg)


    return jsonify({'text': res_msg})

"""
jsonify:是用于处理序列化json数据的函数，就是将数据组装成json格式返回

http://flask.pocoo.org/docs/0.12/api/#module-flask.json
"""


@app.route("/")
def index():
    return render_template("index.html")

'''
'''
# 启动APP
if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8808)

