from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User)
admin.site.register(models.CarBrand)
admin.site.register(models.CarModel)
admin.site.register(models.UserCar)