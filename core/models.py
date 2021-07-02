# from django.contrib.auth import default_app_config
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField

# PRONOUN_OPTIONS = (
#     ("she/her/hers", "she/her/hers"),
#     ("he/him/his", "he/him/his"),
#     ("they/them/theirs", "they/them/theirs")
# )


class User(AbstractUser):
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    pass

# class UserAccountManager(BaseUserManager):
#     def create_user(self, username, email, first_name, last_name, password=None):
#         if not email:
#             raise ValueError('You must provide an email address')

#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, first_name=first_name, last_name=last_name)

#         user.set_password(password)
#         user.save()

#         return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

#     def get_full_name(self):
#         return self.first_name + self.last_name

#     def get_short_name(self):
#         return self.first_name

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


class Session(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.CharField(max_length=100, null=True, blank=True)
    end_time = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    session_status = models.BooleanField(default=False)
    number_of_registrants_allowed = models.IntegerField(default=8)
    facilitator = models.CharField(max_length=225, null=True)
    facilitator_email = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title + ' ' + '(' + self.start_date + '-' + self.end_date + ')'


class SessionRegistrant(models.Model):
    first_name = models.CharField(max_length=225, null=True, blank=True)
    last_name = models.CharField(max_length=225, null=True, blank=True)
    pronouns = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=225, null=True, blank=True)
    comment = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=False)
    session = models.ForeignKey(
        Session, related_name='session_registrants', on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Announcement(models.Model):
    title = models.CharField(max_length=600, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date_to_disappear = models.CharField(
        max_length=225, null=True, blank=True)
    status = models.BooleanField(default=False)
