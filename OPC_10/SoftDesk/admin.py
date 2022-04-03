from django.contrib import admin
from .models import Contributor, Project, Issue, Comment, User
from django.contrib import admin
from .models import Contributor, Project, Issue, Comment, User

# Register your models here.


class SuperAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


models = [Contributor, Project, Issue, Comment, User]
admin.site.register(models, SuperAdmin)
