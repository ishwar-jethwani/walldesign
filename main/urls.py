from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import TemplateView

sitemaps = {
    'static':Staticsitemaps,
}

urlpatterns = [
    path("",home,name="home"),
    path("subscription/",subscription,name="subscribe"),
    path("feedback/",feedback_form,name="feedback"),
    path("contact/",contact,name="contact"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("product_detail/<str:pk>/",product_detail,name="product_detail"),
    path("project_detail/<str:pk>/",project_detail,name="project_detail")

]