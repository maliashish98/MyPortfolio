from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill,Project
from .forms import ContactForm

# Create your views here.
def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()

    #handel contact form submission
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject=f"Portfolio Contact from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            messages.success(request, 'Thank you for your message!, I will get back to you soon.')
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = ContactForm()

    contexts = {
        'skills':skills,
        'projects':projects,
        'form':form
    }
    return render(request, 'portfolio/index.html', contexts)
