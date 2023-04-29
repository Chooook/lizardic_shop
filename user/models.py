from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
