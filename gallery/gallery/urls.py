
from django.conf.urls import url,include
from django.contrib import admin

#^$ regex pattern to portray a site root.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/',include('media.urls'))
]