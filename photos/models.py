from django.db import models
import pyperclip

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Photo(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category =models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(upload_to = 'photos/')

    @classmethod
    def display_photos(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos

    @classmethod
    def single_photo(cls):
        photo = cls.objects.get()
    @classmethod
    def copy_image(cls):
        download = cls.objects.get(name)
        pyperclip.copy(download.photo_image)
        return download
