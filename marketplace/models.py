from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed
from django.shortcuts import render
from group.models import Group
from datetime import datetime

from django.conf import settings
from django.urls import reverse
from member.models import Person

# Create your models here.
class prodProduct(models.Model):
    class Meta:
        db_table = 'prodProduct'
    productName = models.CharField(max_length=255, blank=True)
    productDesc = models.CharField(max_length=1500,blank=True)
    productCategory = models.CharField(max_length=255, blank=True)
    productPrice = models.DecimalField(max_digits=4, decimal_places=2)
    productPhoto = models.ImageField(upload_to ='images/', null=True)
    productRating = models.IntegerField(default=0)
    timePosted = models.DateTimeField(default=datetime.now, blank=True)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

# class productComment(models.Model):
#     class Meta:
#         db_table = 'productComment'    
#     Message = models.CharField(max_length=255, blank=True)
    
# class Products(models.Model):
#     class Meta:
#         db_table = 'Products'
#     Title = models.CharField(max_length=255, blank=True)
#     Message = models.CharField(max_length=1500,blank=True)
#     Photo = models.ImageField(upload_to ='images/')
#     Video = models.FileField(upload_to='media/', null=True)
#     Graph = models.FileField(upload_to='videomedia/')
#     Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

#     def showvideo(request):

#         lastvideo = video.objects.last()
#         videofile = lastvideo.videofile
    
#         form = SellForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()

#         context= {'videofile': videofile, 'form': form}

#         return render(request, 'SellProduct.html', context)
#     #def __str__(self):
#        # return self.Message + ": " + str(self.videofile)

# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super(ProductManager, self).get_queryset().filter(is_active=True)

# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)

#     class Meta:
#         verbose_name_plural = 'categories'

#     def get_absolute_url(self):
#         return reverse('store:category_list', args=[self.slug])

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, default='admin')
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', default='images/default.png')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#     products = ProductManager()

#     class Meta:
#         verbose_name_plural = 'Products'
#         ordering = ('-created',)

#     def get_absolute_url(self):
#         return reverse('store:product_detail', args=[self.slug])

#     def __str__(self):
#         return self.title