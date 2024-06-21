from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")

def hellowithname(request, name):
    return HttpResponse("Hello %s!" % name)

def main_page(request):
    context = {}
    context['hello'] = "Hello World!"  # key hello correponse to hello in template
    return render(request, "main_page.html", context)

def main_page1(request):
    context = {}
    context['hello'] = ["Hello World!", "ld"]  # key hello correponse to hello in template
    return render(request, "main_page1.html", context)

def main_page2(request):
    context = {}
    context['hello'] = {"text":"Hello World!", "name":"ld"}  # key hello correponse to hello in template
    return render(request, "main_page2.html", context)

def index(request):
    # context = {}
    # context['hello'] = {"text":"Hello World!", "name":"ld"}  # key hello correponse to hello in template
    return render(request, "index.html")