from django.db import models

# Create your models here.

class ImagePost(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class BookList(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PetList(models.Model):
    number = models.CharField(max_length=20)
    imgurl = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    kind = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    area = models.CharField(max_length=20)
    feature = models.CharField(max_length=20)

    def __str__(self):
        return self.number