from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
  def create_user(self, username, password):
    if not username:
      raise ValueError('username is must')
    
    user = self.model(username=username)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, password):
    user = self.create_user(username, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(blank=True, null=True)
  first_name = models.CharField(max_length=50, blank=True, null=True)
  last_name = models.CharField(max_length=50, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  objects = UserManager()

  USERNAME_FIELD = 'username'

  def __str__(self):
    return self.username


class Topic(models.Model):
  title = models.CharField(max_length=300)
  is_talking = models.BooleanField(default=False)
  is_closed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

class Comment(models.Model):
  text = models.CharField(max_length=100)
  nickname = models.CharField(max_length=15, blank=True, null=True)
  created_at = models.DateTimeField(auto_now=True)