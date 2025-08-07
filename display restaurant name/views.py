from django.conf import settings
from django.shortcuts import render

def homepage_view(request):
    context = {
        'restaurent_name': settings.restaurent_name
    }
    return render(request, 'home.html', contex)