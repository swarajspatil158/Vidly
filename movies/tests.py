from django.test import TestCase

class genre(models.Model):
    name = modelds.CharField(max_length = 225)

class Movie(models.Model):
    title = modelds.CharField(max_length = 225)
    release_year = modelds.IntegerField()
    number_in_stock = modelds.IntegerField()
    daily_rate = modelds.FloatField()
    genre = models.ForeignKey(genre, on_delete = models.CASCADE)

