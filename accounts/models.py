from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    address = models.TextField(max_length=200)
    contact = models.CharField(max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["address", "contact"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_employee = models.BooleanField(default=True)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_customer = models.BooleanField(default=True)