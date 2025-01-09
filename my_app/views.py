from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Blog
from .models import Subscriber


from .forms import BlogForm, AuthorForm

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


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()  
            return redirect('blog_list')  
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()  # Save the new author to the database
            return redirect('index')  # Redirect to an author list page (or another page)
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})



def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def error_404(request, exception):

    return render(request, '404.html')