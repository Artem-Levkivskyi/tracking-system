from django.db import models
from django.contrib.auth.models import UserManager


class TrackMart(models.Model):
    track_id = models.CharField(max_length=20)
    track_date = models.DateTimeField()
    point_id = models.CharField(max_length=5)
    status_id = models.CharField(max_length=3)

    def __str__(self):
        return self.track_id


class Track(models.Model):
    track_id = models.CharField(max_length=20)
    track_date = models.DateTimeField()
    point_id = models.ForeignKey('TrackPoint', on_delete=models.CASCADE)
    status_id = models.ForeignKey('Statuses', on_delete=models.CASCADE)
    is_actual_track = models.BooleanField(max_length=20)
    is_actual_status = models.BooleanField(max_length=20)

    objects = UserManager()

    def __str__(self):
        return self.track_id

    def publish(self):
        self.save()


class Statuses(models.Model):
    status_id = models.CharField(max_length=3)
    english = models.CharField(max_length=50)
    ukrainian = models.CharField(max_length=50)
    russian = models.CharField(max_length=50)

    objects = UserManager()

    def __str__(self):
        return self.status_id


class TrackPoint(models.Model):
    point_id = models.CharField(max_length=5)
    country_short = models.ForeignKey('Country', on_delete=models.CASCADE)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)

    objects = UserManager()

    def __str__(self):
        return self.point_id


class Country(models.Model):
    country_short = models.CharField(max_length=3)
    english = models.CharField(max_length=50)
    ukrainian = models.CharField(max_length=50)
    russian = models.CharField(max_length=50)

    objects = UserManager()

    def __str__(self):
        return self.country_short


class City(models.Model):
    city_id = models.CharField(max_length=5)
    english = models.CharField(max_length=50)
    ukrainian = models.CharField(max_length=50)
    russian = models.CharField(max_length=50)

    objects = UserManager()

    def __str__(self):
        return self.english
