from django.urls import include, path, re_path
from . import views

urlpatterns = [
	path('', views.main_page),
	re_path('page/(?P<pk>\d+)/', views.page_detail, name='page_detail'),
]
