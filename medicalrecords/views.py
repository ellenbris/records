from django.shortcuts import render, redirect
from .models import Records

# Create your views here.

# Render page 
def index(request): 
    record = Records.objects.all()

    # save new data
    if  request.method == 'POST': 
        new_record = Records (
            title = request.POST['title']
        )
        new_record.save()
        return redirect('/')

    return render(request, 'index.html', {'records':record})