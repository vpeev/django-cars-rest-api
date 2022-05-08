from rest_framework import serializers
from cars.api.serializers import UserCarSerializer
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    cars = UserCarSerializer(
        source='car',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
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
            'cars',
        )

