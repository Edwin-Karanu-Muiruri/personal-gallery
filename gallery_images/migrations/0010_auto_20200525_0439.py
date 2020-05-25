# Generated by Django 3.0 on 2020-05-25 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_images', '0009_images_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to='gallery_images.Category'),
        ),
    ]
