from django.contrib import admin
from .models import ImagePost, BookList, PetList

# Register your models here.
admin.site.register(ImagePost)
admin.site.register(BookList)
admin.site.register(PetList)