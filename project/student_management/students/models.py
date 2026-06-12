from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.roll()