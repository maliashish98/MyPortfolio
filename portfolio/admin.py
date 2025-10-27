from django.contrib import admin
from .models import Project, Skill, Contact, Resume

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email', 'message')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    readonly_fields = ('uploaded_at',)

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
