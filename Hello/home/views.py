from django.shortcuts import render,HttpResponse   #import HttpResponse from django.shortcuts

# Create your views here.
def index(request):
    return HttpResponse("This is the homepage")    #return HttpResponse with the message "This is the homepage"