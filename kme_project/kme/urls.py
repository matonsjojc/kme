from django.conf.urls import url
from kme import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nova_vloga/$', views.nova_vloga, name='nova_vloga'),
]
