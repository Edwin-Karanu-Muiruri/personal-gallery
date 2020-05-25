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
def image_search(request):
    '''
    Displays the search results page
    '''

    title = "Search results"
    if "category" in request.GET and request.GET["category"]:
        searched_category = request.GET.get("category")
        searched_images = Image.search_image(searched_category)
        message = f"{searched_category}"
        
        return render(request, 'search.html', {"message":message, "searched_images": searched_images,"title": title})


    else:
        message = "You haven't searched for anything"
        return render(request, 'search.html', {"message":message,"title": title})

def location_images(request,location):
    '''
    Function to display images per location 
    '''
    location_images = Image.filter_by_location(location)

    return render(request, 'location.html', { "location_images" :location_images, "location":location})
