from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # 首页
]