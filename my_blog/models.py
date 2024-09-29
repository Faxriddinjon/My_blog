from django.db import models

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='image/', blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    shortened=models.TextField()
    text=models.TextField()
