from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	#Construct dictionary
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	#return rendered
	return render(request, 'rango/index.html', context=context_dict)

