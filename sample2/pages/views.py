#from django.shortcuts import render

# Create your views here.



# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, This is Rutik Chaudhari from T1 batch and my PRN is 1841010')