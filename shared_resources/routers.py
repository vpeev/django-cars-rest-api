from rest_framework.routers import DefaultRouter

from cars.api.viewsets import CarBrandViewSet, CarModelViewSet, UserCarViewSet
from users.api.viewsets import UserViewSet

router = DefaultRouter()
router.register(r'brands', CarBrandViewSet, basename='brand')
router.register(r'models', CarModelViewSet, basename='model')
router.register(r'cars', UserCarViewSet, basename='car')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
