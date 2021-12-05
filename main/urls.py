from django.urls import path
from .views import contact, home,feedback_form

urlpatterns = [
    path("",home,name="home"),
    path("feedback/",feedback_form,name="feedback"),
    path("contact/",contact,name="contact"),

]