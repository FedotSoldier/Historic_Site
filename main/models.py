import datetime
from django.db import models

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=200, blank=False)
	subtitle = models.CharField(default="", max_length=100, blank=True)
	content = models.TextField(default="", max_length=10000, blank=True)
	card_link = models.CharField(default="", max_length=2000, blank=True)
	card_description = models.TextField(default="", max_length=8000, blank=True)
	card_source = models.CharField(default="", max_length=2000, blank=True)
	is_usual = models.BooleanField(default=False, blank=False)
	urlpattern = models.CharField(default="", max_length=100, blank=True)
	created_date = models.DateField(default=datetime.date(2000, 1, 1))
	sort = models.IntegerField(blank=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-sort',)
