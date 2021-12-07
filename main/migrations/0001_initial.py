# Generated by Django 3.2.9 on 2021-12-07 04:43

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='About Us')),
                ('img', models.ImageField(upload_to='', verbose_name='Intro Image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_line_1', models.CharField(max_length=200, verbose_name='Address Line 1')),
                ('location_line_2', models.CharField(max_length=200, verbose_name='Address Line 2')),
                ('location_line_3', models.CharField(blank=True, max_length=200, verbose_name='Address Line 3')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Mobile Number')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')])),
                ('subject', models.CharField(max_length=200)),
                ('message', ckeditor.fields.RichTextField(verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Feadback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')])),
                ('feedback', models.CharField(max_length=100, verbose_name='Feedback')),
                ('message', ckeditor.fields.RichTextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name of header image')),
                ('image', models.ImageField(upload_to='', verbose_name='Header Image')),
                ('header_title_1', models.CharField(blank=True, max_length=100, verbose_name='Title on Header Page')),
                ('header_title_2', models.CharField(blank=True, max_length=100, verbose_name=' Big Title on Header Page')),
                ('para', models.CharField(blank=True, max_length=300, verbose_name='Paragraph on Header Page')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Redirection Link')),
                ('logo', models.ImageField(upload_to='', verbose_name='logo')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Product')),
                ('img', models.ImageField(upload_to='', verbose_name='First Image')),
                ('disc', ckeditor.fields.RichTextField(verbose_name='Decription')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=255, verbose_name='Icon')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('dics', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('number', models.PositiveIntegerField(verbose_name='Number')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name Of Social Media Plateform')),
                ('url', models.URLField(verbose_name='Link Of Profile')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('prop_img', models.ImageField(upload_to='realestate/testimonial', verbose_name='Project Image')),
                ('prof', models.CharField(blank=True, max_length=100, verbose_name='Profession')),
                ('disc', models.CharField(max_length=500, verbose_name='Review')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('project_name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('img', models.ImageField(upload_to='', verbose_name='First Image')),
                ('disc', ckeditor.fields.RichTextField(verbose_name='Decription')),
                ('filer_tag', models.CharField(max_length=10, verbose_name='Filter Tag')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='name of image')),
                ('img', models.ImageField(upload_to='', verbose_name='Project Image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='name of image')),
                ('img', models.ImageField(upload_to='', verbose_name='Product Image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
