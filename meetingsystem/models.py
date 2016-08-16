from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    employeeID = models.CharField(max_length=20)


class Schedule(models.Model):
    employeeID = models.CharField(max_length=20, primary_key=True, unique=True)
    blocks = ArrayField(JSONField())
