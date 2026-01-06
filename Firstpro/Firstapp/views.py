from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Index(request):
	print('Hello')
    st='<h1>Welcome to our first Application</h1>'
    return HttpResponse(st)