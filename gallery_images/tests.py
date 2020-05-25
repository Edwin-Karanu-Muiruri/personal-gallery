from django.test import TestCase
from .models import Category,Images,Location
from unittest import skip

# Create your tests here.
class CategoryTestClass(TestCase):
    '''
    Category class tests
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.nature = Category(name = "nature")
        self.nature.save_category()
    
    def tearDown(self):
        '''
        Clears database after each test
        '''
        Category.objects.all().delete()

    def test_category_instance(self):
        '''
        This will test whether the new location created is an instance of the Location class
        '''
        self.assertTrue(isinstance(self.nature, Category))

    def test_save_category_method(self):
        '''
        This tests whether new loaction is added to the db 
        '''
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

    def test_delete_category(self):
        '''
        This tests whether category is deleted
        '''
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
