from django.contrib import admin
from .models import Contributor, Project, Issue, Comment

# Register your models here.


class SuperAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


models = [Contributor, Project, Issue, Comment]
admin.site.register(models, SuperAdmin)
