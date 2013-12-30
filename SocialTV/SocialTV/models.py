from django.db import models

class Program(models.Model):
    name=models.CharField(
        max_length=255,
    )
    genre=models.CharField(
        max_length=255,
    )
    link=models.URLField(
        max_length=200,
    )
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):

        return ' '.join([
            self.name,     
        ])
class Metric(models.Model):
    name=models.CharField(
        max_length=255,
    )
    description=models.CharField(
        max_length=510,
    )
    def __str__(self):

        return ' '.join([
            self.name,
            self.description,     
        ])