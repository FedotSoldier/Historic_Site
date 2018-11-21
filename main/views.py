from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page_detail(request, pattern):
	# Все нащи страницы - записи в бд Pages
	pages = Page.objects.order_by('sort')
	#page = get_object_or_404(Page, urlpattern_name=pattern)
	#return render(request, 'main/page_detail.html', {'page':page})
	return render(request, 'main/{}.html'.format(pattern), {'pages':pages})
