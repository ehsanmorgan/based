from django.db import models

# Create your models here.



class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=300000)






    def __str__(self):
        return self.title