from django.conf.urls import url, include, patterns
from django.contrib import admin
import article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^basicview/', include(article.urls)),
]
