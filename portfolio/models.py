from django.db import models
from django.utils import timezone
# Create your models here.

#Skills Model
class Skill(models.Model):
    name = models.CharField(max_length=200)
    proficiency = models.IntegerField(help_text="Proficiency in % (1-100)")
    logo = models.ImageField(upload_to='logos/',blank=True,null=True)
    created_on = models.DateTimeField(default=timezone.now)

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo,'url'):
            return self.logo.url
        return '/static/portfolio/images/default-skill-image.png'

    def __str__(self):
        return self.name

#Projects model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    githublink = models.URLField(blank=True, null=True)
    livelink = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/',blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    @property
    def image_url(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
        return '/static/portfolio/images/default-project-image.png'
    
    def __str__(self):
        return self.title
    
#contact Model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.email}"