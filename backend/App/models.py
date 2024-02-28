from django.db import models
from django.utils.text import slugify
import random

# Create your models here.


class Status(models.Model):
    State = models.CharField(max_length=200)

    def __str__(self):
        return self.State


class Task(models.Model):
    Task_title = models.CharField(max_length=250)
    Slug = models.SlugField(max_length=250, null=True, blank=True)
    Content = models.TextField(max_length=1000, null=True, blank =True)
    status = models.ForeignKey(Status,  on_delete=models.CASCADE)

    def Slugify_title(self):
        random_int = random.randint(0,5000000) #generate random integer from 0 - 5000000
        if self.Slug is None:
            slug = slugify(f"{self.Task_title} {random_int}")
            self.Slug = slug
        return

    def Retrive_state(self):
        return f"task is {self.status}"

    def save(self, *args, **kwargs):
        self.Slugify_title()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.Task_title
