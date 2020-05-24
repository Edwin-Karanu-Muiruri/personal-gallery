from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.image_name
    