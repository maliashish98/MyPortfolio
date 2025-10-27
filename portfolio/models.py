from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
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


 #Resume Model
class Resume(models.Model):
    title = models.CharField(max_length=100, default='Aashish Mali - Resume')
    file = models.FileField(upload_to='resumes/')   
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk and Resume.objects.exists():
            raise ValidationError("Only one resume can exist at a time. Please delete the old one before uploading a new one.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_at.strftime('%Y-%m-%d')}"
    
    @property
    def file_url(self):
        if self.file and hasattr(self.file,'url'):
            return self.file.url
        return None
    
    