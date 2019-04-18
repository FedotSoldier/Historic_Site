from django.shortcuts import render
from .models import Page


def main_page(request):
	pages = Page.objects.order_by('sort')
	curr_page = pages[0]

	return page_detail(request, curr_page.pk)


def page_detail(request, pk):
	curr_page = Page.objects.get(pk=pk)
	if curr_page.is_usual:
		# Если `curr_page.is_usual`, то объект этой страницы должна иметь поле `urlpattern`(см. ниже)
		return usual_page_detail(request, pk)
	return card_page_detail(request, pk)


def usual_page_detail(request, pk):
	pages = Page.objects.order_by('sort')
	curr_page = Page.objects.get(pk=pk)

	indexes = get_prev_and_next_indexes(pages, curr_page)
	prev_page_pk = list(pages)[indexes[0]].pk
	next_page_pk = list(pages)[indexes[1]].pk

	return render(
		request,
		'main/{}'.format(curr_page.urlpattern),
		{
			'pages': pages,
			'curr_page': curr_page,
			'prev_page_pk': prev_page_pk,
			'next_page_pk': next_page_pk
		}
	)


def card_page_detail(request, pk):
	pages = Page.objects.order_by('sort')
	curr_page = Page.objects.get(pk=pk)

	indexes = get_prev_and_next_indexes(pages, curr_page)
	prev_page_pk = list(pages)[indexes[0]].pk
	next_page_pk = list(pages)[indexes[1]].pk

	return render(
		request,
		'main/Card.html',
		{
			'pages': pages,
			'curr_page': curr_page,
			'prev_page_pk': prev_page_pk,
			'next_page_pk': next_page_pk
		}
	)


def get_prev_and_next_indexes(query, curr_obj):
	curr_index = list(query).index(curr_obj)
	next_index = (curr_index + 1) % len(query)
	prev_index = curr_index - 1 if len(query) > 1 else next_index
	return prev_index, next_index
