from django.contrib.auth.models import AbstractUser
from shared_resources.models import SoftDeleteModel

# Create your models here.

class User(AbstractUser, SoftDeleteModel):
    pass
