from django.test import TestCase
from .models import Category,Images,Location
from unittest import skip

# Create your tests here.
class CategoryTestClass(TestCase):
    '''
    Category class tests
    '''
    def setUp(self):
        self.nature = Category(name = "nature")
        self.nature.save_category()
    
    def tearDown(self):
        Category.objects.all().delete()

    def test_category_instance(self):
        self.assertTrue(isinstance(self.nature, Category))

    def test_save_category_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

    def test_delete_category(self):
        self.nature.save_category()
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),1)
        self.nature.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),0)

    
    def test_update_category(self):
        '''
        Tests whether the category name is updated
        '''
        self.nature.save_category()
        self.nature.update_category(self.nature.id,'natural')
        new_update = Category.objects.get(name = "natural")
        self.assertEqual(new_update.name, 'natural')

class ImageTestClass(TestCase):
    '''
    Image tests class
    '''

    def setUp(self):
        self.nature = Category( name= "nature")
        self.nairobi = Location(name = "nairobi")
        self.flower = Image(image = "image", name ='flower', description = 'beautiful', category= self.nature, location= self.nairobi)

        self.nature.save_category()
        self.nairobi.save_location()
        self.flower.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.flower, Image))


    def test_save_image_method(self):
        self.flower.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_display_images(self):
        self.flower.save_image()
        self.assertEqual(len(Image.display_all_images()), 1)

    def test_delete_images(self):
        self.flower.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.flower.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_image_description(self):
        self.flower.save_image()
        self.flower.update_image_description(self.flower.id,'pink')
        new_update = Image.objects.get(name = "flower")
        self.assertEqual(new_update.description, 'pink')


    def test_get_image_by_id(self):
        self.flower.save_image()
        image = Image.get_image_by_id(self.flower.id)
        self.assertEqual(image.name, self.flower.name)

    def test_search_image(self):
        self.nature.save_category()
        self.flower.save_image()
        images = Image.search_image("nature")
        self.assertTrue(len(images) > 0)

    
    def test_search_location(self):
        self.nairobi.save_location()
        self.flower.save_image()
        images = Image.filter_by_location("nairobi")
        self.assertTrue(len(images) > 0)