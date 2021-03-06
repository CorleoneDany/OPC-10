# sourcery skip: avoid-builtin-shadow
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class User(AbstractUser):
    """Remodel the users."""

    username = None
    email = models.EmailField(max_length=64, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()


class Project(models.Model):
    """Model the projects."""

    PROJECT_TYPE_CHOICES = (
        ('BE', 'back-end'),
        ('FE', 'front-end'),
        ('IOS', 'IOS'),
        ('ANDROID', 'Android')
    )

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=PROJECT_TYPE_CHOICES)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="project_author")


class Contributor(models.Model):
    """Model the contributors."""

    ROLE = (
        ('AUTHOR', 'Author'),
        ('CONTRIBUTOR', 'Contributor')
    )

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="contributor_user")
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributor_project")
    permission = models.CharField(max_length=64)
    role = models.CharField(max_length=64, choices=ROLE)


class Issue(models.Model):
    """Model the issues."""

    PRIORITY_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    )

    STATUS_CHOICES = (
        ('TO-DO', 'To Do'),
        ('IN-PROGRESS', 'In Progress'),
        ('DONE', 'Done')
    )

    TAGS = (
        ('BUG', 'Bug'),
        ('IMPROVEMENT', 'Improvement'),
        ('TASK', 'Task')
    )

    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)
    tag = models.CharField(max_length=64, choices=TAGS)
    priority = models.CharField(max_length=64, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE,
        related_name="issue_project")
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="issue_author")
    assignee = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="issue_assignee")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Model the commentaries."""

    description = models.CharField(max_length=64)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="comment_author")
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE,
        related_name="comment_issue")
    created_time = models.DateTimeField(auto_now_add=True)
