from django.db import models
from django.contrib.auth.models import AbstractUser

PRONOUN_OPTIONS = (
    ("she/her/hers", "she/her/hers"),
    ("he/him/his", "he/him/his"),
    ("they/them/theirs", "they/them/theirs")
)

class User(AbstractUser):
    pass

class SessionRegister(models.Model):
    name = models.CharField(max_length=225)
    pronouns = models.CharField(max_length=100, choices=PRONOUN_OPTIONS, null=True)
    email = models.CharField(max_length=225, null=True, blank=True)
    comment = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Session(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    session_status = models.BooleanField(default=False)