from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/',views.search, name='search'),
    url(r'^today/',views.today, name='today'),
    url(r'^(?P<student_id>[0-9]+)/', views.detail, name='look up'),
]
