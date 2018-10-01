from django.conf.urls import url

from tour import views


urlpatterns = [
    url(r'^$', views.index, name='tour_index'),

]
