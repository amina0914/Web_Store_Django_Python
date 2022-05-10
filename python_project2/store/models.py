
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="no item type")
    name = models.CharField(max_length=100, default="no item name")
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    description = models.TextField(default="no description")
    likes = models.ManyToManyField(User, related_name="store_products")
    size = models.CharField(max_length=100, default="no size")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    address = models.CharField(max_length=500, default="no address")
    status = models.CharField(max_length=100, default="new")
    flags = models.ManyToManyField(User, related_name="flag_products")

    def total_likes(self):
        return self.likes.count()

    def total_flags(self):
        return self.flags.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.name)
