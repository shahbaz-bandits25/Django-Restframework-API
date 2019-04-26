from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=10)
    fname=models.CharField(max_length=10)
    year=models.IntegerField()
   
    def __str__(self):
     return self.name
