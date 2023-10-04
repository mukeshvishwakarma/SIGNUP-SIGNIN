from django.db import models
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    location = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'usermodel'


class CustomUser(models.Model):
    mobile_no = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    candidate_id = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "users"
