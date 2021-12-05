from django.urls import path
from .views import contact, home,feedback_form,subscription

urlpatterns = [
    path("",home,name="home"),
    path("subscription/",subscription,name="subscribe"),
    path("feedback/",feedback_form,name="feedback"),
    path("contact/",contact,name="contact"),

]