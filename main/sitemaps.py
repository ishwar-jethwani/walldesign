from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from .models import *
from django.shortcuts import reverse



class Staticsitemaps(Sitemap):
    
    def items(self):
        return ['home','contact','feedback','subscribe']

    def location(self,item):
        return reverse(item)