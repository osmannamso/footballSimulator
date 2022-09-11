from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=255)


class Season(models.Model):
    name = models.CharField(max_length=255)


class Club(models.Model):
    name = models.CharField(max_length=255)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Game(models.Model):
    a_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    b_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
