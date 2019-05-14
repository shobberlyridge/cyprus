from django import forms
from todo.models import Todo
from autoslug import AutoSlugField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class TodoForm(forms.ModelForm):
	title = forms.CharField(max_length=25, help_text="Enter title of item.")
	description = forms.CharField(max_length=100, help_text="Description")
	#creation_date = forms.DateField(disabled=True, widget = forms.SelectDateWidget, required=False)
	target_completion_date = forms.DateField(required = False, widget = forms.SelectDateWidget, help_text="Target Completion Date")
	start_date = forms.DateField(required = False, widget = forms.SelectDateWidget, help_text="Start Date")
	#completed = forms.BooleanField(default = False)
	#completed_date = forms.DateField(required = False)
	#slug = AutoSlugField() (required=False)
	
	class Meta:
		model = Todo
		fields = ('title','description', 'target_completion_date', 'start_date',)
