from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="resources/")
    release_time = models.DateTimeField()

    def __str__(self):
        return self.title