from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Manpower(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="manpower/")

    def __str__(self):
        return self.title


class Service(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title


class Enquiry(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    message = models.TextField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    manpower = models.ForeignKey(
        Manpower,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


