from django.db import models

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


class Resume(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")