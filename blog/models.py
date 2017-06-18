from django.db import models
from datetime import date

class Post(models.Model):
	title = models.CharField('title',max_length=100, blank=False)
	date = models.DateField('date published', default=date.today)
	main_body = models.TextField('body', blank=False)
	subtitle1 = models.CharField('subtitle 1', max_length=100, blank=True)
	subtitle2 = models.CharField('subtitle 2', max_length=100, blank=True)
	subtitle3 = models.CharField('subtitle 3', max_length=100, blank=True)
	subsection1 = models.TextField('section 1', blank=True)
	subsection2 = models.TextField('section 2', blank=True)
	subsection3 = models.TextField('section 3', blank=True)
	def __str__(self):
		return self.title
