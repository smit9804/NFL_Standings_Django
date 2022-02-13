from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    division = models.CharField(max_length=20)
    overall_wins = models.IntegerField()
    overall_losses = models.IntegerField()
    conf_wins = models.IntegerField()
    conf_losses = models.IntegerField()
    primary_color = models.CharField(max_length=20)
    secondary_color = models.CharField(max_length=20)
