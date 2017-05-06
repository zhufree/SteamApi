from flask import Flask
from flask import jsonify
from core import news
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_discount/')
def get_discount():
    pass

@app.route('/get_news/')
def get_news():
    return jsonify(news.get_index_news())

@app.route('/get_userinfo/')
def get_user_info():
    pass

@app.route('/get_appinfo/')
def get_app_info():
    pass

@app.route('/get_applist/')
def get_app_list():
    pass

