from django.shortcuts import render

def contact_us_view(request):
    contact_info = {
        "phone": "+91 234 567 90",
        "email": "info@example.com",
        "address": "123/456 Main Road Street, Kanpur, india"
    }
    return render(request,"contact_us.html", {"contact": contact_info})