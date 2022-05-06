from rest_framework import viewsets

from users.models import User
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

