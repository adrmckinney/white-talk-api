from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

PRONOUN_OPTIONS = (
    ("she/her/hers", "she/her/hers"),
    ("he/him/his", "he/him/his"),
    ("they/them/theirs", "they/them/theirs")
)

class User(AbstractUser):
    pass


class Session(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    session_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' ' + '(' + self.start_date + '-' + self.end_date + ')'

class SessionRegistrant(models.Model):
    first_name = models.CharField(max_length=225, null=True, blank=True)
    last_name = models.CharField(max_length=225, null=True, blank=True)
    pronouns = models.CharField(max_length=100, choices=PRONOUN_OPTIONS, null=True)
    email = models.CharField(max_length=225, null=True, blank=True)
    comment = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, related_name='session_registrants', on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name