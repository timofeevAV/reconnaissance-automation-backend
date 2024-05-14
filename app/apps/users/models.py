from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    lastName = models.CharField(max_length=128)
    firstName = models.CharField(max_length=128)
    middleName = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=128)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['lastName', 'firstName', 'middleName', 'role']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_name(self):
        return f'{self.lastName} {self.firstName} {self.middleName}'
