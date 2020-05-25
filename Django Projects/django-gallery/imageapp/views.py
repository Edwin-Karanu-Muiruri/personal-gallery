from django.shortcuts import render
from .models import Category,Location,Image

# Create your views here.
def index(request):
    '''
    View function to render the index page
    '''
    title = "My Gallery"
    images = Image.display_all_images()
    locations = Location.display_all_locations()
    return render(request,"index.html", {"title":title, "images":images, "locations":locations})