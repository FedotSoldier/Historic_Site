from django.shortcuts import render
from .models import Page

# Create your views here.

# Все нащи страницы - записи в бд Pages
pages = Page.objects.order_by('sort')

def main_page(request):
	return render(request, 'main/main_page.html', {'pages':pages})

def test_page(request):
	return render(request, 'main/test_page.html', {'pages':pages})
