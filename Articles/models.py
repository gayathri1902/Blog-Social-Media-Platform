from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class article_table(models.Model):
    name= models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateField()
    genre=models.CharField(max_length=100)
    likes=models.IntegerField(default=0)
    email=models.CharField(max_length=100,default=123)
    def __str__(self):
        return f'{self.title}'

    
