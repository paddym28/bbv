from unicodedata import name
from django.db import models

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    message = models.TextField()
    
    def __str__(self):
        return str(self.name)


    
    
        