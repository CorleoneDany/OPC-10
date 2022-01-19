from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Contributor(models.Model):
    PERM_CHOICES = (
        ('C', 'Create'),
        ('R', 'Read'),
        ('U', 'Update'),
        ('D', 'Delete')
    )

    user_id = models.IntegerField()
    project_id = models.IntegerField()
    permission = models.CharField(choices=PERM_CHOICES, default='R')
    role = models.CharField()


class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    type = models.CharField()
    author_user_id = models.ForeignKey(to=User)


class Issue(models.Model):
    title = models.CharField()
    desc = models.CharField()
    tag = models.CharField()
    priority = models.CharField()
    project_id = models.IntegerField()
    status = models.CharField()
    author_user_id = models.ForeignKey(to=User)
    assignee_user_ud = models.ForeignKey(to=User)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    description = models.CharField()
    author_user_id = models.ForeignKey(to=User)
    issue_id = models.ForeignKey(to=Issue)
    created_time = models.DateTimeField(auto_now_add=True)
