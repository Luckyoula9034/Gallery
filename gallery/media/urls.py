from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
     url('^today/$',views.media_of_day,name='mediaToday')
]