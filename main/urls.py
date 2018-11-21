from django.urls import include, path
from . import views
from django.urls import path

urlpatterns = [
	path('', views.page_detail, {'pattern':'main_page'}),
	path('page/<slug:pattern>/', views.page_detail, name='page_detail'),
]

'''
mysite - historicsite
blog - main
Post - Page
'''
