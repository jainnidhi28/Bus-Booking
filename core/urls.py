from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import UserViewSet, create_customer

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/create-customer/", create_customer, name="create-customer"),
]