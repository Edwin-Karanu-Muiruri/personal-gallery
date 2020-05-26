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

def image_search(request):
    '''
    View function to display results of the search
    '''
    title = "Search Results"
    if "category" in request.GET and request.GET["category"]:
        searched_category = request.GET.get("category")
        searched_images = Image.search_image(searched_category)
        message = f"{searched_category}"

        return render(request, 'search.html', {"message":message, "searched_images": searched_images,"title": title})


    else:
        message = "Please input a category to be searched"
        return render(request, 'search.html', {"message":message,"title": title})