from django.contrib import admin
from . import models

admin.site.register(models.CarBrand)
admin.site.register(models.CarModel)
admin.site.register(models.UserCar)