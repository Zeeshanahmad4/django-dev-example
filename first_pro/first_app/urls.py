from django.conf.urls import url
from first_app import views


app_name = 'first_app'

urlpatterns = [
url(r'^relatives/$',views.rel,name = 'relatives'),
url(r'^other/$', views.other, name='other')
]
