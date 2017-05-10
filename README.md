# SteamApi
A flask app to get and transform data for an other app

>已实现的接口：

## 新闻（news）
>没有现成接口，直接从Steam网站新闻业页抓取


- `/get_index_news/`：`GET`方法，返回首页最新新闻数据，10条；
- `/get_some_news/`：`GET`方法，可以带两个参数，第一个是新闻条数（不填则默认为10），第二个是时间戳（UTC时间，不填默认为当前时间），检索从该时间往前的数条新闻；

测试地址:
http://api.zhufree.info/