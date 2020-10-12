from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.media_of_day,name='mediaToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_media,name = 'pastMedia'),
]