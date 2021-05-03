from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(blank=True, null=True)
  first_name = models.CharField(max_length=50 ,blank=True, null=True)
  last_name = models.CharField(max_length=50 ,blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  objects = BaseUserManager()

  USERNAME_FIELD = 'username'

  def __str__(self):
    return self.username


class Topic(models.Model):
  title = models.CharField(max_length=300)
  is_talking = models.BooleanField(default=False)
  is_closed = models.BooleanField(default=False)

  def __str__(self):
    return self.title