from django.db import models

# Create your models here.


class Thing:
    name = models.TextField()
    description = models.TextField()
    quantity = models.TextField()
