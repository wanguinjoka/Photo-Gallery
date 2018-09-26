from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category =models.ForeignKey(Category)
