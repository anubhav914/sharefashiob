from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	followers = models.IntegerField(default = 0)

def set_email_as_unique():
    """
    Sets the email field as unique=True in auth.User Model
    """
    email_field = dict([(field.name, field) for field in AbstractUser._meta.fields])["email"]
    setattr(email_field, '_unique', True)

set_email_as_unique()