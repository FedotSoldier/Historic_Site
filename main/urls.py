from django.urls import include, path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('test', views.test_page, name='test_page'),
]
