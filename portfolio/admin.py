from django.contrib import admin
from .models import Project, Skill, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email', 'message')

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
