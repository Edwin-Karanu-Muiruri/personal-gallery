from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id = id).update(name = value)

class Location(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id = id).update(name = value)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Image(models.Model):
    image_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete = models.CASCADE,default = 'category')
    location = models.ForeignKey(Location, on_delete = models.CASCADE, default = 'location')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
    def delete_image():
        self.delete()

    
    