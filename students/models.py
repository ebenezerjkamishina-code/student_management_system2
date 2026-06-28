from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    
    def _str_(self):
        return self.name

class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'), 
        ('Graduated', 'Graduated'),
        ('Dropped', 'Dropped'),
    ]
    
    CLASS_CHOICES = [
        ('Year 1', 'Year 1'),
        ('Year 2', 'Year 2'), 
        ('Year 3', 'Year 3'),
    ]
    
    full_name = models.CharField(max_length=200)
    reg_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    class_level = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Year 1')
    courses = models.ManyToManyField(Course, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.reg_number} - {self.full_name}"
    



    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=50, unique=True)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.reg_number

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'studentprofile'):
        StudentProfile.objects.create(user=instance, reg_number=instance.username)
# Create your models here.
