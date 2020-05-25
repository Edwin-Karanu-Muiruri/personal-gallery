from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    View function to render the index page
    '''
    return render(request,"index.html")