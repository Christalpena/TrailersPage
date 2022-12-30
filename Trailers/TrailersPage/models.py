from django.db import models

# Create your models here.
class TrailersInf(models.Model):
    title = models.TextField()
    category = models.TextField()
    year = models.IntegerField()
    director = models.TextField()
    actors = models.TextField()
    review =models.IntegerField()
    img_link = models.TextField()
    link = models.TextField()
