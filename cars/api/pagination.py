from rest_framework.pagination import LimitOffsetPagination

class CustomUserCarPagination(LimitOffsetPagination):
    default_limit = 100