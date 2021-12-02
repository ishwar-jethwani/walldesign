from django.contrib import messages
from django.shortcuts import render
from .models import *

def home(request):
    context = {
        "headers":Header.objects.all()[:1],
        "projects":Projects.objects.all(),
        "testimonials":Testimonial.objects.all(),
        "address":Address.objects.all()[:1],

    }
    if request.method == "POST":
        email = request.GET.get("sub_email")
        created = Subscribe.objects.create(
            email = email
        )
        if created:
            messages.success(request,"Thank You For Subcription")

    return render(request,"index.html",context)

