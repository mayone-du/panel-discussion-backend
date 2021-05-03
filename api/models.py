from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True)

  USERNAME_FIELD = 'username'

  def __str__(self):
    return self.username


class Topic(models.Model):
  title = models.CharField(max_length=300)
  is_talking = models.BooleanField(default=False)
  is_closed = models.BooleanField(default=False)

  def __str__(self):
    return self.title