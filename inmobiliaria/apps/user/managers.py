from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, name, email, password=None, active=True, staff=False, admin=False):
        if not email:
            raise ValueError('El email es requerido')
        
        if not password:
            raise ValueError('La contraseña es requerida')

        if not name:
            raise ValueError('Nombre es requerido')
        
        user = self.model(
            email = self.normalize_email(email)
        )

        user.name = name
        user.set_password(password)
        user.active = active
        user.staff = staff
        user.admin = admin

        user.save(using=self._db)

        return user

    def create_staffuser(self, name, email, password=None):
        user = self.create_user(
            name,
            email,
            password=password,
            staff=True
        )

        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(
            name,
            email,
            password=password,
            staff=True,
            admin=True
        )

        return user