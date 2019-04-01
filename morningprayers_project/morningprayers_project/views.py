from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the morningprayers Index page.")
