from rest_framework import serializers
from . import models 

class UserCarSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset = models.User.objects.all(),
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
        fields = '__all__'
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'created_at',
            'update_at',
            'deleted_at',
        )

