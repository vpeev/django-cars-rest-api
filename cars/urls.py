from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'brands', views.CarBrandViewSet, basename='brand')
router.register(r'models', views.CarModelViewSet, basename='model')
router.register(r'cars', views.UserCarViewSet, basename='car')
urlpatterns = router.urls
