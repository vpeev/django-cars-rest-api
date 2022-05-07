from django.conf import settings
from django.db import models
from shared_resources.models import SoftDeleteModel

# Create your models here.

class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE, related_name='car_model')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.car_brand.name} {self.name}'

class UserCar(SoftDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='car')
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE, related_name='car', blank=True, null=True)
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, related_name='car')
    first_reg = models.CharField(max_length=8)
    odometer = models.IntegerField()

    def save(self, *args, **kwargs):
        self.car_brand = self.car_model.car_brand
        super(UserCar, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s {self.car_brand} {self.car_model.name}"