from rest_framework import viewsets

from . import models, serializers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = models.CarBrand.objects.all()
    serializer_class = serializers.CarBrandSerializer
    filterset_fields = ['name']

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = models.CarModel.objects.all()
    serializer_class = serializers.CarModelSerializer
    filterset_fields = ['name', 'car_brand__name']

class UserCarViewSet(viewsets.ModelViewSet):
    queryset = models.UserCar.objects.all()
    serializer_class = serializers.UserCarSerializer
    filterset_fields = ['user__username', 'car_brand__name', 'car_model', 'first_reg', 'odometer']
