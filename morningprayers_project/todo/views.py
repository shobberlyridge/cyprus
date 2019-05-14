from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from todo.forms import TodoForm
from autoslug import AutoSlugField


#def index(request):
#    # return HttpResponse("This is the todo Index page.")
#	latest_todo_list = Todo.objects.order_by('creation_date')[:20]
#	output = '/n'.join([t.title for t in latest_todo_list])
#	#output = ("Testing")
#	return HttpResponse(output)


def index(request):
	latest_todo_list = Todo.objects.order_by('creation_date')[:25]
	context_dict = {'todos': latest_todo_list}
	response = render(request, 'todo/index.html', context_dict)
	# Call function to handle the cookies
	#visitor_cookie_handler(request, response)
	# Return response back to the user, updating any cookies that need changed.
	return response

def show_todo(request, slug):
	#output = "Show todo request"
	#return HttpResponse("Item %s." % slug)
	todo_item = Todo.objects.get(slug = slug)
	context_dict = {'todo_item': todo_item}
	response = render(request,  'todo/show_todo.html', context_dict)
	#return HttpResponse("Item %s." % slug)
	return response



def add_todo(request):
	form = TodoForm()
	if request.method == 'POST':
		print("Post")
		form = TodoForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			print(form.is_valid())
			# Save the new item to the database.
			form.save(commit=True)
			print("balh")
			# Now that the category is saved
			# We could give a confirmation message
			# But since the most recent category added is on the index page
			# Then we can direct the user back to the index page.
			return index(request)
		else:
			# The supplied form contained errors -
			# just print them to the terminal.
			print(form.errors)
			# Will handle the bad form, new form, or no form supplied cases.
		# Render the form with error messages (if any).
	return render(request, 'todo/add_todo.html', {'form': form})
