from django.urls import path

from . import views

urlpatterns = [
    # path('', views.helloWorld, name = 'helloWorld'),
    # path('about', views.about, name = 'about')
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('add_author/', views.add_author, name='add_author'),
    path('subscribe/', views.subscribe, name='subscribe'),
]