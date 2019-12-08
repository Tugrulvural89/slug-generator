from django.db import models
import os
from django.db.models.signals import pre_save, post_save
import random
# Create your models here.
from .utils import unique_slug_generator

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug =  models.SlugField(blank=True, unique=True)
    descriptios = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    object = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
