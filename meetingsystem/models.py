from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    employeeID = models.CharField(max_length=20)


class Meeting(models.Model):
    owner = models.CharField(max_length=20)
    room = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    employees = ArrayField(models.CharField(max_length=20))
    accepted = ArrayField(models.CharField(max_length=20))
    declined = ArrayField(models.CharField(max_length=20))
    isActive = models.BooleanField(default=True)


class Schedule(models.Model):
    employeeID = models.CharField(max_length=20, primary_key=True, unique=True)
    blocks = ArrayField(JSONField())
