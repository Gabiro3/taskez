from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    avatar = models.ImageField(null=False, default='avatar.svg')


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
class Groups(models.Model):
    name = models.CharField(max_length=200, null=True)
    logo = models.ImageField(null=False, default='group.png')
    participants = models.ManyToManyField(User, related_name='groupons')

class Task(models.Model):
    title = models.CharField(max_length=120, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.CharField(max_length=120, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title