from rest_framework import serializers
from users.models import User
from cars import models 

class UserCarSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        many=False,
        slug_field='username'
    )
    car_brand = serializers.SlugRelatedField(
        queryset = models.CarBrand.objects.all(),
        many=False,
        slug_field='name'
    )
    class Meta:
        model = models.UserCar
        fields = (
            'id',
            'user',
            'car_brand',
            'car_model',
            'first_reg',
            'odometer',
            'created_at',
            'update_at',
            'deleted_at'
        )
        read_only_fields = ['update_at', 'deleted_at', 'created_at']

class CarModelSerializer(serializers.ModelSerializer):
    car_brand = serializers.SlugRelatedField(
        queryset = models.CarBrand.objects.all(),
        many=False,
        slug_field='name',
    )
    class Meta:
        model = models.CarModel
        fields = (
            'id',
            'name',
            'car_brand',
            'update_at',
            'deleted_at',
            'created_at'
        )
        read_only_fields = ['update_at', 'deleted_at', 'created_at']

class CarBrandSerializer(serializers.ModelSerializer):
    car_model = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )
    class Meta:
        model = models.CarBrand
        fields = (
            'id',
            'name',
            'car_model',
            'created_at',
            'update_at',
            'deleted_at',
        )
        read_only_fields = ['update_at', 'deleted_at', 'created_at']
