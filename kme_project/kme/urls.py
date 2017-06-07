from django.conf.urls import url
from kme import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vlagatelj_osnovni_podatki/$', views.vlagatelj_osnovni_podatki, name='vlagatelj_osnovni_podatki'),
    url(r'^raziskava/$', views.raziskava, name='raziskava'),
]
