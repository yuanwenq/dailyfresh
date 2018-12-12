# Python-Django-天天生鲜项目(编写中...)

初学django框架时按照传智播客python教程所学习的项目,该项目包含了实际开发中的电商项目中大部分的功能开发和知识点实践。

功能:用户注册，用户登录，购物车，用户中心，首页，订单系统，地址信息管理，商品列表，商品详情，支付功能等等，是一个完整的电商项目流程

__注:此项目纯属个人学习项目__

## 技术栈
python + django + mysql + redis + FastDFS(分布式图片服务器) + nginx

## 目标功能:
- [x] 用户注册 -- 完成
- [x] 用户登录 -- 完成
- [x] 用户中心 -- 完成
- [x] 地址信息 -- 完成
- [X] 首页静态访问化 -- 完成
- [x] 商品列表页 -- 完成
- [x] 商品详情页 -- 完成
- [x] 全文检索引擎(搜索引擎) -- 完成
- [x] 购物车实现增删改查 -- 完成
- [x] 创建订单页 -- 完成
- [x] 订单提交功能 -- 完成

## 运行环境

[配置环境文件](https://github.com/yuanwenq/dailyfresh/blob/dev/dailyfresh/settings.py)

[虚拟环境安装和启动方式]()

[celery分布式任务队列启动方式]()

[FastDFS安装和配置,注意存放目录](https://blog.csdn.net/MissEel/article/details/80856194)

[Nginx及fastdfs-nginx-module安装]()

[全文检索引擎-生成jieba分词引擎步骤]()

[支付宝支付接口配置]()
```
# 项目包安装
pip install -r requirements.txt

# 使用的数据库
mysql - database: dailyfresh

# 启动celery分布式任务队列
celery -A celery_tasks.tasks worker -l info

# redis服务端启动
sudo redis-server /etc/redis/redis.conf

# FastDFS服务启动
# 启动Trackerd服务
sudo /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf start

# 启动storge服务
sudo /usr/bin/fdfs_storaged /etc/fdfs/storage.conf start

# 启动nginx
sudo /usr/local/nginx/sbin/nginx
# 重启nginx
sudo /usr/local/nginx/sbin/nginx -s reload

# 建立索引文件--搜索引擎
# 新环境需要配置jieba分词,生成whoose_cn_backend文件
python manage.py rebuild_index

# 每个环境下修改fdfs服务器指向IP
/utils/fdfs/client.conf
/dailyfresh/settings.py

# mysql事务隔离级别设置
sudo vim /etc/mysql/mysql.conf.d/mysql.cnf
transaction-isolation = READ-COMMITTED (读已提交)

# 支付宝支付接口配置
```
## 项目包介绍
```
pass 待续
```
## 注意点
pip install fdfs_client-py-master 存在bug，需要下载特定版本地址  
redis版本需要2.10.6 否则会报错,因为使用django的版本问题  
乐观锁,mysql事务的隔离级别设置

## 效果演示

## 总结

## 项目布局
```
pass 待续
```