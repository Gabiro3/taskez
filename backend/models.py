from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import date
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

class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=150, unique=True, null=True)
    avatar = models.ImageField(null=False, default='profile.png')
    preferences = models.CharField(max_length=120, null=True, default='Productivity')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


#--- TASKS MODEL ---

class Task(models.Model):
    host = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    priority = models.CharField(max_length=120, null=True)
    submission_date = models.CharField(max_length=300, null=True)
    uploaded = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True, default='Pending')
    workspace = models.ForeignKey('Activity', on_delete=models.CASCADE, null=True)
    completed = models.DateTimeField(null=True, blank=True)  # New field for completion timestamp

    class Meta:
        ordering = ['-uploaded']

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    tasks = models.ManyToManyField(Task, blank=True)
    category = models.CharField(max_length=100, null=True, default='Productivity')
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-uploaded']

class Group(models.Model):
    name = models.CharField(max_length=120, null=True)
    participants = models.ManyToManyField(Client, related_name='participants')
    admin = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, null=True)
    preferences = models.CharField(max_length=120, null=True)# Use JSONField to store preferences

    def __str__(self):
        return self.name
class Invitation(models.Model):
    invitor = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='invitor')
    invitee = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='invitee')
    accepted = models.BooleanField(null=True)

class Progress(models.Model):
    day = models.DateField(default=date.today, unique=True)
    success_rate = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.day} - Success Rate: {self.success_rate}%"