from django.shortcuts imports render

def home(request):
    context = {
        'restaurant_name': 'Tasty Bites',
        'Welcome_message': 'Welcome to Our Restaurant! Enjoy delicious food and great vibes.'
    }
    return render(request, 'home.html', context)