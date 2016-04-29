from django.conf.urls import url
from article import views

urlpatterns = [

    url(r'^1/', views.basic_one),
    url(r'^2/', views.template_two),
    url(r'^3/', views.template_three_simple),
]
