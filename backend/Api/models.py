from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1500)
    salary = models.IntegerField()
    image = models.ImageField(upload_to="Employee_images/")

    def __str__(self):
        return self.name
