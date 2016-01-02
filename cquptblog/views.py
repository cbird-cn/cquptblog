from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>hello cqupt</h1>")

def index(request):
    return render_to_response('index.html',locals())