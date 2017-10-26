from django.db import models

# Create your models here.
class Paper(models.Model):
    doi = models.CharField(max_length=200)
    title = models.CharField(max_length=500)

class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
