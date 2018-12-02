# Python-Django-天天生鲜项目(持续编写中...)

初学django框架时按照传智播客python教程所学习的项目,该项目包含了实际开发中的电商项目中大部分的功能开发和知识点实践。

功能:用户注册，用户登录，购物车，用户中心，首页，订单系统，地址信息管理，商品列表，商品详情，支付功能等等，是一个完整的电商项目流程

__注:此项目纯属个人学习项目__

## 技术栈
python + django + django-tinymce(富文本编辑器) + mysql + redis

## 目标功能:
- [x] 用户注册 -- 完成
- [x] 用户登录 -- 完成
- [x] 用户中心 -- 完成
- [x] 地址信息 -- 完成

## 运行环境

[配置环境文件](https://github.com/yuanwenq/dailyfresh/blob/dev/dailyfresh/settings.py)

[虚拟环境安装和启动方式]()

[celery分布式任务队列启动方式]()
```
# 项目包安装
pip install -r requirements.txt

mysql - database: dailyfresh

# 启动celery分布式任务队列
# redis版本需要2.10.6 否则会报错
celery -A celery_tasks.tasks worker -l info

# redis服务端启动
sudo redis-server /etc/redis/redis.conf 指定加载的配置文件

```
## 项目相关包
```

```

## 效果演示

## 总结

## 项目布局
