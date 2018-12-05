from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^$', views.indexView, name='index'), # 首页
]