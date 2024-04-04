from django.db import models

# Create your models here.
GENDER = (("male","male"),("female","female"))
class Records(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=100,choices = GENDER)
    def __str__(self):
        return (f"{self.name}")