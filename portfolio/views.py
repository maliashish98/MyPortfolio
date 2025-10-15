from django.shortcuts import render
from .models import Skill,Project

# Create your views here.
def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    contexts = {
        'skills':skills,
        'projects':projects
    }
    return render(request, 'portfolio/index.html', contexts)
