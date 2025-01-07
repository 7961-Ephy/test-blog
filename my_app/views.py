from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# def helloWorld(request):
#     return HttpResponse("Hello, world!")

# def about(request):
#     return HttpResponse("About Page")

def index(request):
    return render(request, 'index.html')

def about(request):
    context = {
        'message': 'Hello Everyone'
    }
    return render(request, 'about.html', context)
