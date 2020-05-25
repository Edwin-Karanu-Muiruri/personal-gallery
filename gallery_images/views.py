from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.

def index(request):
    '''
    View function to render index page
    '''
    title = " Personal Gallery"
    images = Image.display_all_images()
    return render(request, "index.html", {"title": title, "images":images})
