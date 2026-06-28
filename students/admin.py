from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Student, Course, StudentProfile  # add StudentProfile




admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentProfile)