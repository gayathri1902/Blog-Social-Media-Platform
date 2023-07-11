from django.db import models

# Create your models here.

class signup_table(models.Model):
    email= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    pswd=models.CharField(max_length=100,default=123)
    rpswd=models.CharField(max_length=100,default=123)
    def __str__(self):
        return f'{self.name}'