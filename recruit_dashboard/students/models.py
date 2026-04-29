from django.db import models

# Create your models here.

class Student(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Enrolled', 'Enrolled'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course_interest = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.name
