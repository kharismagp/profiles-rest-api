from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User harus memiliki alamat email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name) 

ddref

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model untuk users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']



    def get_full_name(self):
        """mendapatkan full name user"""
        return self.name

    def get_short_name(self):
        """mendapatkan short name user"""
        return self.name

    def __str__(self):
        """return representation dari user"""
        return self.email
