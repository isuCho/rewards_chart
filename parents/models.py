from django.db import models


class Child(models.Model):
    name = models.TextField()
    points = models.BigIntegerField(default=0)

    def __str__(self):
        return f'({self.name[:30]}: {self.points} points)'
