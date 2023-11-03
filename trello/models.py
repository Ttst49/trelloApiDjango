from django.contrib.auth.models import User
from django.db import models


# Create your models here

class WorkspaceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Visibility(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class List(models.Model):
    cards = models.ManyToManyField(Card, related_name='cards')


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='members')
    is_starred = models.BooleanField(default=False)
    lists = models.ManyToManyField(List, related_name='lists')
    visibility = models.ForeignKey(Visibility, on_delete=models.CASCADE)


class Workspace(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(WorkspaceType, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
