from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Header(models.Model):
    name            = models.CharField(max_length=20,verbose_name="name of header image")
    image           = models.ImageField(verbose_name="Header Image")
    header_title_1  = models.CharField(max_length=100,verbose_name="Title on Header Page",blank=True)
    header_title_2  = models.CharField(max_length=100,verbose_name=" Big Title on Header Page",blank=True)
    para            = models.CharField(max_length=300,verbose_name="Paragraph on Header Page",blank=True)
    date_created    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name    = models.CharField(max_length=200)
    slug    = models.SlugField(null=True)
    parent  = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Product(models.Model):
    name            = models.CharField(max_length=100,verbose_name="Name of Product")
    img             = models.ImageField(verbose_name="First Image")
    disc            = RichTextField(verbose_name="Decription")
    category        = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created    = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name


class Projects(models.Model):
    number          = models.PositiveIntegerField()
    project_name    = models.CharField(max_length=200,verbose_name="Project Name")
    img             = models.ImageField(verbose_name="First Image")
    disc            = RichTextField(verbose_name="Decription")
    category        = models.ForeignKey(Category,on_delete=models.CASCADE)
    filer_tag       = models.CharField(max_length=10,verbose_name="Filter Tag")
    date_created    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project_name
    
    
    class Meta:
        ordering = ['number']


class ProductImage(models.Model):
    name            = models.CharField(max_length=20,verbose_name="name of image",blank=True)
    img             = models.ImageField(verbose_name="Product Image")
    product         = models.ForeignKey(Product,on_delete=models.CASCADE)
    date_created    = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name

class ProjectImage(models.Model):
    name            = models.CharField(max_length=20,verbose_name="name of image",blank=True)
    img             = models.ImageField(verbose_name="Project Image")
    project         = models.ForeignKey(Projects,on_delete=models.CASCADE)
    date_created    = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    name            = models.CharField(max_length=100,verbose_name="Name")
    email           = models.EmailField(verbose_name="Email",blank=True)
    mobile_number   = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    subject         = models.CharField(max_length=200)
    message         = RichTextField(verbose_name="Message")
    date            = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-date"]


class Address(models.Model):
    location_line_1 = models.CharField(max_length=200,verbose_name="Address Line 1")
    location_line_2 = models.CharField(max_length=200,verbose_name="Address Line 2")
    location_line_3 = models.CharField(max_length=200,verbose_name="Address Line 3",blank=True)
    email           = models.EmailField(verbose_name="Email")
    mobile_number   = PhoneNumberField(verbose_name="Mobile Number")

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["pk"]


class Services(models.Model):
    symbol  =       models.CharField(max_length=255,blank=True,verbose_name="Icon")
    name    =       models.CharField(max_length=500,verbose_name="Name")
    dics    =       RichTextField(verbose_name="Content")
    number  =       models.PositiveIntegerField(verbose_name="Number")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['number']

class Testimonial(models.Model):
    name                =       models.CharField(max_length=255,verbose_name="Name")
    prop_img            =       models.ImageField(upload_to='realestate/testimonial',verbose_name="Project Image")
    prof                =       models.CharField(max_length=100,verbose_name="Profession",blank=True)
    disc                =       models.CharField(max_length=500,verbose_name="Review")


    def __str__(self):
        return self.name


class Feadback(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name")
    contact_no = PhoneNumberField(validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    feedback = models.CharField(max_length=100,verbose_name="Feedback")
    message = RichTextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name



class Subscribe(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.email
    class Meta:
        ordering = ["-date"]


class SocialMedia(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name Of Social Media Plateform",blank=True)
    url = models.URLField(verbose_name="Link Of Profile")
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.name


class Logo(models.Model):
    link = models.URLField(verbose_name="Redirection Link")
    logo = models.ImageField(verbose_name="logo")
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.id

    
class About(models.Model):
    desc = RichTextField(verbose_name="About Us")
    img = models.ImageField(verbose_name="Intro Image")
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date_created"]
    def __str__(self) -> str:
        return self.id





