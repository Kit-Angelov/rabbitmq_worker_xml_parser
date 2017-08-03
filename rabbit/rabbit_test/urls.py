from django.conf.urls import url, include
from . import views

app_name = 'rabbit_test'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success/$', views.success, name='success'),
    url(r'^sign_up/', views.register_user, name='register_user'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout')
]