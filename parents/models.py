from django.db import models
from django.urls import reverse


class Parent(models.Model):
    def __str__(self):
        return str(self.id)
    pass


class Child(models.Model):
    name = models.TextField(default='')
    points = models.BigIntegerField(default=0)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.name[:30]}(parent {self.parent}): {self.points} points)'


class Task(models.Model):
    text = models.TextField()
    points = models.BigIntegerField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.text[:30]}{self.child}: {self.points} points)'
