from flask import Flask, request
from flask import jsonify
from core.news import SteamNews
from core.sales import SteamSales

steamapp = Flask(__name__)
sn = SteamNews()
ss = SteamSales()

@steamapp.route('/')
def hello_world():
    return 'Hello, World!'

@steamapp.route('/get_all_sales/')
def get_all_sales():
    return jsonify(ss.get_all_sales(100))

@steamapp.route('/get_some_sales/')
def get_some_sales():
    args_c = request.args.get('count')
    args_o = request.args.get('orderby')
    count =  int(args_c) if args_c else None
    orderby =  args_o if args_o else 'discount'
    if orderby == 'discount':
        return jsonify(ss.get_all_sales(count))
    elif orderby == 'rating':
        return jsonify(ss.get_sales_by_rating(count))
    elif orderby == 'price':
        return jsonify(ss.get_sales_by_price(count))


@steamapp.route('/get_index_news/')
def get_news():
    return jsonify(sn.get_index_news())

@steamapp.route('/get_some_news/')
def get_some_news():
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

