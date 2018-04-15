# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Game(models.Model):
    name = models.TextField()
    company = models.ForeignKey(Company, related_name='developed by')


class Company(models.Model):
    name = models.TextField()


class Platform(models.Model):
    name = models.TextField()


class Genre(models.Model):
    name = models.TextField()


class GameRelease(models.Model):
    game = models.ForeignKey(Game)
    date = models.DateField()
    platform = models.ForeignKey(Platform)
    cover = models.ImageField(upload_to='img/covers', black='true')

    class Meta:
        unique_together = ("game", "platform")


class GameReview(models.Model):
    game = models.ForeignKey(Game, related_name='review of')
    user = models.ForeignKey(User, related_name='reviewed by')
    RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), \
                      (7, 'seven'), (8, 'eight', (9, 'nine'), (10, 'ten')))
    rating = models.PositiveSmallIntegerField('Rating (0-10)', blank=False, default=3, choices=RATING_CHOICES)

    class Meta:
        unique_together = ("game", "user")
