from django.db import models
from django.contrib.auth.models import AbstractUser

PNOPTIONS = (
    ("she/her/hers", "she/her/hers"),
    ("he/him/his", "he/him/his"),
    ("they/them/theirs", "they/them/theirs")
)

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    name = models.CharField(max_length=225)
    pronouns = models.CharField(max_length=100, choices=PNOPTIONS, null=True)
    email = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)