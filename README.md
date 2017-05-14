# SteamApi
A flask app to get and transform data for an other app

>数据来源：
http://store.steampowered.com
https://steamdb.info

## 新闻（news）
>没有现成接口，直接从Steam网站新闻业页抓取


- `/get_index_news/`：`GET`方法，返回首页最新新闻数据，10条；
- `/get_some_news/`：`GET`方法，可以带两个参数，第一个是新闻条数（不填则默认为10），第二个是时间戳（UTC时间，不填默认为当前时间），检索从该时间往前的数条新闻；

## 折扣（sales）
> 数据来自steamdb

- `/get_all_sales/`：`GET`方法，获取当日全部打折信息，数据较多（几百条），响应速度会比较慢；
- `/get_some_sales/`：`GET`方法，参数有两个：`count`为数目，默认为全部，`orderby`为按照什么排序，可选值有`discount`折扣度从高到底，`rating`游戏的好评率从高到底，`price`打折后的价格从低到高。


测试地址:
http://api.zhufree.info/