from django.conf.urls import url

from web import views


urlpatterns = [
    url(r'^$', views.index, name='web_index'),
    url(r'^charity/$', views.charity, name='web_charity'),

]
