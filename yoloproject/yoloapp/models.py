from django.db import models

# Create your models here.

class ImagePost(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name