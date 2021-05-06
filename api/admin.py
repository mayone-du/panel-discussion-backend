from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Topic, Comment

admin.site.register(User, UserAdmin)
admin.site.register(Topic)
admin.site.register(Comment)