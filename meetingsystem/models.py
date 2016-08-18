from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    employeeID = models.CharField(max_length=20)


class Meeting(models.Model):
    owner = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    room = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField()
    employees = ArrayField(models.CharField(max_length=20))
    accepted = ArrayField(models.CharField(max_length=20))
    declined = ArrayField(models.CharField(max_length=20))
    isActive = models.BooleanField(default=True)


class Schedule(models.Model):
    employeeID = models.CharField(max_length=20, primary_key=True, unique=True)
    blocks = JSONField(default=list([]))


class Invite(models.Model):
    owner = models.CharField(max_length=20, db_index=True)
    meetingOwner = models.CharField(max_length=20)
    meetingId = models.IntegerField()
    title = models.CharField(max_length=120)
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField()
