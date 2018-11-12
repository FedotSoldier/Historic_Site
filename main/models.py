from django.db import models

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=200)
	urlpattern_name = models.CharField(max_length=100)
	sort = models.IntegerField()

	def __str__(self):
		return self.title
