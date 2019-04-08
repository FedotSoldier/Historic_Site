from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from .models import Page

# Create your views here.

def page_detail(request, pattern):
	# Все наши страницы - записи в бд Pages
	pages = Page.objects.order_by('sort')

	# page = get_object_or_404(Page, urlpattern_name=pattern)
	# return render(request, 'main/page_detail.html', {'page':page})

	# Получаем объекты текущего, следующего и предыдущего постов

	# Получаем объект текущей страницы
	curr_page = Page.objects.get(urlpattern_name=pattern)
	
	# Получаем индекс элемента данного поста в queryset
	index = list(pages).index(curr_page)

	# Получаем индекс следующего элемента
	# (для кнопок следующей и предыдущей страниц)
	index = (index + 1) % len(pages)

	# Следующий пост
	next_page = list(pages)[index].urlpattern_name

	# Предыдущий пост
	# Если на сайте всего одна страница:
	if len(pages) == 1:
		prev_page = next_page
	else:
		prev_page = list(pages)[index - 2].urlpattern_name

	return render(
		request,
		'main/{}.html'.format(pattern),
		{'pages': pages,
		'curr_page': curr_page,
		'prev_page': prev_page,
		'next_page': next_page}
	)
