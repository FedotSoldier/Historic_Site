from django.urls import include, path
from . import views
from django.urls import path

urlpatterns = [
	path('', views.main_page),
    path('page/0', views.main_page, name='main_page'),
    path('page/1', views.test_page, name='test_page'),
]

'''
mysite - historicsite
blog - main
Post - Page
'''
# номер должен совпадать с полем sort
# у соответствующего поста в бд
