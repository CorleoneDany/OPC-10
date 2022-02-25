from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """Create a new user."""
        user = User(email=email, password=password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """Create a new superuser."""
        user = User(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    """Remodel the users."""

    username = None
    email = models.EmailField(max_length=64, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Contributor(models.Model):
    """Model the contributors."""

    PERM_CHOICES = (
        ('C', 'Create'),
        ('R', 'Read'),
        ('U', 'Update'),
        ('D', 'Delete')
    )

    ROLE = (
        ('AUTHOR', 'Author'),
        ('CONTRIBUTOR', 'Contributor')
    )

    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="contributor_user")
    project_id = models.IntegerField()
    permission = models.CharField(
        max_length=64, choices=PERM_CHOICES, default='R')
    role = models.CharField(max_length=64, choices=ROLE)


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
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="project_author")


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
    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE,
        related_name="issue_project")
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="issue_author")
    assignee_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="issue_assignee")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Model the commentaries."""

    description = models.CharField(max_length=64)
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="comment_author")
    issue_id = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE,
        related_name="comment_issue")
    created_time = models.DateTimeField(auto_now_add=True)
