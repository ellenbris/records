from django.shortcuts import render

# Create your views here.

# Render page 
def index(request): 
    return render(request, 'index.html')