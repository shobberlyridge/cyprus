from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


#def index(request):
#    # return HttpResponse("This is the todo Index page.")
#	latest_todo_list = Todo.objects.order_by('creation_date')[:20]
#	output = '/n'.join([t.title for t in latest_todo_list])
#	#output = ("Testing")
#	return HttpResponse(output)


def index(request):
	latest_todo_list = Todo.objects.order_by('creation_date')[:20]
	context_dict = {'todos': latest_todo_list}
	response = render(request, 'todo/index.html', context_dict)
	# Call function to handle the cookies
	#visitor_cookie_handler(request, response)
	# Return response back to the user, updating any cookies that need changed.
	return response

def show_todo(request, slug):
	#output = "Show todo request"
	return HttpResponse("Item %s." % slug)
