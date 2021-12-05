from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail

def home(request):
    context = {
        "headers":Header.objects.all()[:1],
        "categories":Category.objects.all(),
        "projects": Projects.objects.all(),
        "testimonials":Testimonial.objects.all(),
        "address":Address.objects.all()[:1],
        "products":Product.objects.all()[1:]

    }

    return render(request,"index.html",context)

def subscription(request):
    if request.method == "POST":
        email = request.POST.get("sub_email")
        created = Subscribe.objects.create(
            email = email
        )
        if created:
            messages.success(request,"Thank You For Subcription")
            return redirect("home")
    return redirect("home")
        

def feedback_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = "+91"+request.POST.get("mobile")
        feedback = request.POST.get("feedback")
        message = request.POST.get("message")
        create  = Feadback.objects.create(
            name = name,
            contact_no = phone,
            feedback = feedback,
            message = message
        )
        if create:
            messages.success(request,"Thank You For Feedback")
    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = "91"+request.POST.get("mobile")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(
                name = name,
                email = email,
                mobile_number = phone,
                subject = subject,
                message = message
        )

        send_mail(f"Name - {name}, Email - {email}, Phone Number - {phone}, Subject- {subject}",message,"urbanspacerealtors.rkl@gmail.com",["hr.rsdastudio@gmail.com"])
        messages.success( request,"Thank you for contacting us")
        return redirect("home")
    return redirect("home")