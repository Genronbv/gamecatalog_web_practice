# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.TextField()
    company =  models.ForeignKey(Company, related_name='developed by')

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
    RATING_CHOICES = ((1,'one'), (2, 'two'), (3, 'three'), (4,'four'),(5,'five'),(6,'six'),\
                      (7,'seven'),(8,'eight',(9,'nine'),(10,'ten')))
    class Meta:
        unique_together = ("game","user")