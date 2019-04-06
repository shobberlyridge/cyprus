from django.db import models
from autoslug import AutoSlugField

class Todo(models.Model):
	title = models.CharField(max_length=25)
	description = models.CharField(max_length=100)
	creation_date = models.DateField()
	target_completion_date = models.DateField(blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	completed = models.BooleanField(default = False)
	completed_date = models.DateField(blank=True, null=True)
	slug = AutoSlugField(populate_from='title', unique = True)

	
	def __str__(self):
		return self.title
