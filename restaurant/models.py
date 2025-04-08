from django.db import models
from django.contrib.auth.models import User
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField()
    time = models.TimeField()
    guests = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"
class Review(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
