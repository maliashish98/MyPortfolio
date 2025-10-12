from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html',)

def about(request):
    return render(request, 'portfolio/about.html',)

def skills(request):
    return render(request, 'portfolio/skills.html',)

def projects(request):
    return render(request, 'portfolio/projects.html',)

def contact(request):
    return render(request, 'portfolio/contact.html',)