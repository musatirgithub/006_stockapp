from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CreatedUpdated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.TextField()

    def __str__(self) -> str:
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    image = models.TextField()

    def __str__(self) -> str:
        return self.name


class Product(CreatedUpdated):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products_category")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="products_brand")
    stock = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.brand} {self.name}"


class Purchase(CreatedUpdated):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True)


class Sale(CreatedUpdated):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True)
