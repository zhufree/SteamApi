from flask import Flask, request
from flask import jsonify
from core.news import SteamNews
steamapp = Flask(__name__)
sn = SteamNews()

@steamapp.route('/')
def hello_world():
    return 'Hello, World!'

@steamapp.route('/get_discount/')
def get_discount():
    pass

@steamapp.route('/get_index_news/')
def get_news():
    return jsonify(sn.get_index_news())

@steamapp.route('/get_some_news/')
def get_more_news():
	args_c = request.args.get('count')
	args_d = request.args.get('enddate')
	count =  args_c if args_c else '10'
	enddate =  args_d if args_d else '0'
	return jsonify(sn.get_some_news(count, enddate))

@steamapp.route('/get_userinfo/')
def get_user_info():
    pass

@steamapp.route('/get_appinfo/')
def get_app_info():
    pass

@steamapp.route('/get_applist/')
def get_app_list():
    pass

