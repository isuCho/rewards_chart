from django.db import models
from django.urls import reverse


class Parent(models.Model):
    pass


class Child(models.Model):
    name = models.TextField(default='')
    points = models.BigIntegerField(default=0)
    parent = models.ForeignKey(Parent, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.name[:30]}: {self.points} points)'
