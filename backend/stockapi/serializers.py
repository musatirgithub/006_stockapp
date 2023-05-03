from rest_framework import serializers
from .models import Category, Firm, Brand, Product, Sale, Purchase


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "address",
            "image",
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "image",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "brand",
            "stock",
            "created",
            "updated",
        )


class SaleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Sale
        fields = (
            "id",
            "name",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "quantity",
            "price",
            "total_price",
            "created",
            "updated",
        )


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Purchase
        fields = (
            "id",
            "name",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "quantity",
            "price",
            "total_price",
            "created",
            "updated",
        )
