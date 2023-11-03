from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model

# Create your models here.


class Thing(Model):
    name = models.CharField(default="", unique=True, blank=False, max_length=30)
    description = models.CharField(default="", unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(default=0 , validators=[MaxValueValidator(100), MinValueValidator(0)])
