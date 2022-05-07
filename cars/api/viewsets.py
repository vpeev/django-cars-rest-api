from rest_framework import viewsets
from cars.models import CarBrand, CarModel, UserCar
from .serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer
from .pagination import CustomUserCarPagination

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filterset_fields = ['name']

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filterset_fields = ['name', 'car_brand__name']

class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    pagination_class = CustomUserCarPagination # Custom paginaion because I expect more objects here than in the other models
    filterset_fields = ['user__username', 'car_brand', 'car_model__name', 'first_reg', 'odometer']
