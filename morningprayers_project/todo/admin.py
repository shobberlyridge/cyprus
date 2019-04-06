from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'description', 'creation_date', 'completed']
	readonly_fields=('slug',)



admin.site.register(Todo, TodoAdmin)
