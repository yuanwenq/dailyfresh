# Python-Django-天天生鲜项目

初学django框架时按照传智播客python教程所学习的项目,该项目包含了实际开发中的电商项目中大部分的功能开发和知识点实践。

功能:用户注册，用户登录，购物车，用户中心，首页，订单系统，地址信息管理，商品列表，商品详情，支付功能等等，是一个完整的电商项目流程

__注:此项目纯属个人学习项目__

## 技术栈
python + django + mysql + redis + FastDFS(分布式图片服务器) + nginx

## 目标功能:
- [x] 功能模块
    - [x] 用户模块
        - [x] 注册
        - [x] 登录
        - [x] 激活(celery)
        - [x] 退出
        - [x] 个人中心
        - [x] 地址管理
    - [x] 商品模块
        - [x] 首页(celery)
        - [x] 商品详情
        - [x] 商品列表
        - [x] 搜索功能(haystack+whoose)
    - [x] 购物车模块(redis)
        - [x] 增加
        - [x] 删除
        - [x] 修改
        - [x] 查询
    - [x] 订单模块
        - [x] 确认订单页面
        - [x] 订单创建
        - [x] 请求支付(支付宝)
        - [x] 查询支付结果
        - [x] 评论

## 运行环境

[配置环境文件](https://github.com/yuanwenq/dailyfresh/blob/dev/dailyfresh/settings.py)

[虚拟环境安装和启动方式]()

[celery分布式任务队列启动方式]()

[FastDFS安装和配置,注意存放目录](https://blog.csdn.net/MissEel/article/details/80856194)

[Nginx及fastdfs-nginx-module安装]()

[全文检索引擎-生成jieba分词引擎步骤]()

[支付宝支付接口配置]()

[软件安装-云盘]()
  
- 项目启动：  
    - **注意: 项目启动前请先查看项目[配置环境文件](https://github.com/yuanwenq/dailyfresh/blob/dev/dailyfresh/settings.py),配置你相应的设置**
```
    项目包安装
    pip install -r requirements.txt
    
    Django启动命令
    python manage.py runserver 
```    
- uwsgi web服务器启动：  
```    
    启动: uwsgi --ini 配置文件路径 / uwsgi --ini uwsgi.ini
    停止: uwsgi --stop uwsgi.pid路径 / uwsgi --stop uwsgi.pid
    
    注意：uwsgi开启需要修改dailyfresh/settings中的DEBUG和ALLOWED_HOSTS
```
- celery分布式任务队列启动  
```
    celery -A celery_tasks.tasks worker -l info
```
- redis服务端启动
```
    sudo redis-server /etc/redis/redis.conf
```
- FastDFS服务启动
```    
    Trackerd服务
    sudo /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf start

    storge服务
    sudo /usr/bin/fdfs_storaged /etc/fdfs/storage.conf start
```
- nginx
```
    启动nginx
    sudo /usr/local/nginx/sbin/nginx
    重启nginx
    sudo /usr/local/nginx/sbin/nginx -s reload
```
    # 建立索引文件--搜索引擎
    # 新环境需要配置jieba分词,生成whoose_cn_backend文件
    python manage.py rebuild_index

    # mysql事务隔离级别设置
    sudo vim /etc/mysql/mysql.conf.d/mysql.cnf
    transaction-isolation = READ-COMMITTED (读已提交)

## 项目包介绍
```
amqp==2.3.2
asn1crypto==0.24.0
billiard==3.5.0.4
celery==4.2.1
certifi==2018.11.29
cffi==1.11.5
chardet==3.0.4
configparser==3.5.0
cryptography==2.4.1
Django==1.8.2
django-haystack==2.8.1
django-redis==4.10.0
django-redis-sessions==0.5.6
django-tinymce==2.6.0
fdfs-client-py==1.2.6
idna==2.7
itsdangerous==1.1.0   # 身份信息加密
jieba==0.39           
kombu==4.2.1
mutagen==1.41.1
Pillow==5.3.0
pycparser==2.19
pycryptodomex==3.7.2
PyMySQL==0.9.2
python-alipay-sdk==1.8.0
pytz==2018.7
redis==2.10.6
requests==2.20.1
rerequests==1.0.0b0
six==1.11.0
urllib3==1.24.1
uWSGI==2.0.17.1
vine==1.1.4
Whoosh==2.7.4
```
## 注意点
pip install fdfs_client-py-master 存在bug，需要[下载特定版本]()  
redis版本需要2.10.6 否则会报错,因为使用django的版本过低问题  
如果使用乐观锁,需要修改mysql事务的隔离级别设置

## 效果演示

## 总结
用户验证使用Django默认的认证系统AbstractUser  
发送邮件避免让用户等待时间过长,使用了celery任务队列(中间人)  