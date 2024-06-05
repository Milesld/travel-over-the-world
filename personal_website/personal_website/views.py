from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

def hellowithname(request, name):
    return HttpResponse("Hello %s!" % name)