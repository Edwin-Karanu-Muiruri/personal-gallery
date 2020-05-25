from django.db import models

# Create your models here.
    
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Recent','Recent'),
        ('Family','Family'),
        ('Friends','Friends'),
        ('Travel','Travel'),
        ('Food','Food'),
        ('Fashion','Fashion'),
        ('Sports','Sports'),
    ]
    category = models.CharField(max_length = 30,choices = CATEGORY_CHOICES, default = 'Recent')


    def __str__(self):
        return self.category

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE,default = 'id')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)

    def __str__(self):
        return self.image_name
    