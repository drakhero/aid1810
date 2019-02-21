from django.conf.urls import url
from . import views

urlpatterns = [
    #判断请求路径是否为show01
    url(r'^show01/$', views.show01),
    url(r'^$', views.index)
]