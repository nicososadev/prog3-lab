from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
