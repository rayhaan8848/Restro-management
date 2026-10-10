
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ("CUSTOMER", "Customer"),
        ("STAFF", "Staff"),
        ("ADMIN", "Admin"),
    ]

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="CUSTOMER"
    )

    def __str__(self):
        return self.username
