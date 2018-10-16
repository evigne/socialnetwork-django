from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Home Page')
def home(request):
	numbers=[1,2,3,4,5]
	name='Vigneshwaran'
	args = {'myName':name, 'numbers':numbers}
	return render(request,'accounts/home.html',args)
