from django.shortcuts import render, redirect

# Create your views here.

#view for the homepage
def home(request):
    return render(request,  'movies/home.html')
#view for the about page
def about(request):
    context = {}
    return render(request, 'movies/about.html', context)
