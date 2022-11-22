from django.contrib import admin

# Register your models here.
from .models import Result

# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
admin.site.register(Result)