from django.shortcuts import render
from django.shortcuts import HttpResponse

'''def about(request):
    return HttpResponse('hi there! Im hello world')
def home(request):
    return HttpResponse('home')'''
def about(request):
    return render(request,'About.html')
def home(request):
    return render(request,'Home.html')