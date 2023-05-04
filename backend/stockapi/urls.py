from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, FirmView, BrandView, ProductView, SaleView, PurchaseView


router = routers.DefaultRouter()
router.register("category", CategoryView)
router.register("firm", FirmView)
router.register("brand", BrandView)
router.register("product", ProductView)
router.register("sale", SaleView)
router.register("purchase", PurchaseView)

urlpatterns = [

]

urlpatterns += router.urls
