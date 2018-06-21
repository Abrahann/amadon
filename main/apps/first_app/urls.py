from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy$', views.index),
    url(r'^process', views.process),
    url(r'^checkout', views.checkout),
    url(r'^reset', views.reset)
]