from django.contrib import admin

# Register your models here.

#注册User模块
from . import  models
admin.site.register(models.User) #注册User模块