
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomerUserManager(BaseUserManager):

    def normalize_email(self, email):
        return super().normalize_email(email).lower()

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")

        if email:
            email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["is_active"] = True
        extra_fields["role"] = "ADMIN"

        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
    # def create_superuser(self, username, email=None, password=True, **extra_fields):
    #         extra_fields.setdefault("is_staff", False)
    #         extra_fields.setdefault("is_superuser", False)
    #         extra_fields.setdefault("is_active", False)
    #         extra_fields.setdefault("role", "ADMIN")

    #         if extra_fields.get("is_staff") is not True:
    #             raise ValueError("super must jave is_staff=True")
    #         if extra_fields.get("is_superuser") is not True:
    #             raise ValueError("super must jave is_superuser=True")
            
    #         if email:
    #             email = self.normalize_email(email)
    #         user=self.model(username=username, email=email, **extra_fields)
    #         user.set_password(password)
    #         user.save(using=self._db)
    #         return user 
    

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
    objects=CustomerUserManager()
    def __str__(self):
        return self.username
