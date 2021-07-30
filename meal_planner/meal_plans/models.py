from django.db import models

class breakfast(models.Model):
    breakfast = models.CharField(max_length=50)
    lunch = models.CharField(max_length=50)
    dinner = models.CharField(max_length=50)
