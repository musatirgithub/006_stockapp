from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Firm, Brand, Product, Sale, Purchase
from .serializers import CategorySerializer, FirmSerializer, BrandSerializer, ProductSerializer, SaleSerializer, PurchaseSerializer

# Create your views here.


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
