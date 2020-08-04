from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^form/', views.emp_detail, name = 'form'),
    url(r'^bootstrap/', views.form_template, name = 'form_bootstrap'),
    url(r'^detail/', views.detail_fetch, name = 'detail'),
]