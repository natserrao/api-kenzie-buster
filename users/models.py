from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthdate = models.DateField(blank=True)
    is_employee = models.BooleanField(blank=True, default=False)
