from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^basicview/', include('article.urls')),
    url(r'^', include('article.urls')),
]
