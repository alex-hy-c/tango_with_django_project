from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	#Construct dictionary
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {}
	context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
	context_dict['categories'] = category_list
	# Render the response and send it back!
	return render(request, 'rango/index.html', context=context_dict)

