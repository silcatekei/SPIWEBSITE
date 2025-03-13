# myapp/models.py
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    previous_school = models.CharField(max_length=100)

    def __str__(self):
        return self.name