from rest_framework import serializers
from users.models import User
from cars.models import CarBrand, CarModel, UserCar

class UserCarSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        many=False,
        slug_field='username'
    )
    car_brand = serializers.SlugRelatedField(
        queryset = CarBrand.objects.all(),
        many=False,
        slug_field='name'
    )
    car_model = serializers.SlugRelatedField(
        queryset = CarModel.objects.all(),
        many=False,
        slug_field='name'
    )
    class Meta:
        model = UserCar
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
        queryset = CarBrand.objects.all(),
        many=False,
        slug_field='name',
    )
    class Meta:
        model = CarModel
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
        model = CarBrand
        fields = (
            'id',
            'name',
            'car_model',
            'created_at',
            'update_at',
            'deleted_at',
        )
        read_only_fields = ['update_at', 'deleted_at', 'created_at']
