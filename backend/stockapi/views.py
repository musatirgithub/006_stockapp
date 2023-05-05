from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .models import Category, Firm, Brand, Product, Sale, Purchase
from .serializers import CategorySerializer, FirmSerializer, BrandSerializer, ProductSerializer, SaleSerializer, PurchaseSerializer

# Create your views here.


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]


class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data["user_id"] = self.request.user.id
        serializer.is_valid(raise_exception=True)
        ##################################################################
        # serializer.validated_data["user_id"] = self.request.user.id
        ##################################################################

        ##################################################################
        sale_quantity = int(request.data["quantity"])
        item = Product.objects.get(id=int(request.data["product_id"]))
        if item.stock - sale_quantity >= 0:
            item.stock -= sale_quantity
            item.save()
        else:
            data = {
                "message": f"You have only {item.stock} {item.brand} {item.name}s."}
            headers = self.get_success_headers(serializer.data)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST, headers=headers)

        ##################################################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        ##################################################################
        new_quantity = int(request.data["quantity"])
        old_quantity = instance.quantity
        item = Product.objects.get(id=instance.product_id)
        if item.stock - (new_quantity - old_quantity) >= 0:
            item.stock -= new_quantity - old_quantity
            item.save()
        else:
            data = {
                "message": f"You don't have enough {item.brand.name} {item.name}"}
            return Response(data=data)

        ##################################################################
        self.perform_update(serializer)

        return Response(serializer.data)


class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        purchase = request.data
        print(purchase)
        item = Product.objects.get(id=purchase["product_id"])
        print(item)
        item.stock += purchase["quantity"]
        item.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        #######################################################
        new_amount = int(request.data["quantity"])
        old_amount = instance.quantity
        item = Product.objects.get(id=instance.product_id)
        item.stock += new_amount - old_amount
        item.save()
        #######################################################
        self.perform_update(serializer)

        return Response(serializer.data)
