from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class SoftDeleteModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.deleted_at = timezone.now()
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.id is not None:
            self.update_at = timezone.now()
        super().save(*args, **kwargs)

class User(AbstractUser, SoftDeleteModel):
    def __str__(self):
        return self.username

class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE, related_name='car_model')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.car_brand.name} {self.name}'

class UserCar(SoftDeleteModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='car')
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE, related_name='user_car')
    car_model = models.CharField(max_length=100)
    first_reg = models.CharField(max_length=8)
    odometer = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s {self.car_brand.name} {self.car_model}"