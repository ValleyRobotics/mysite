from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    github = models.CharField(max_length=100)
    image = models.FileField()


class Image(models.Model):
    name = models.CharField(max_length=500)
    imageFile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)