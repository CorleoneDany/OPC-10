from django.contrib.auth.models import BaseUserManager


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
