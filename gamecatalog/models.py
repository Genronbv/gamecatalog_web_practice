# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.TextField()
    company =  models.ForeignKey(Company, related_name='developed_by')

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

    class Meta:
        unique_together = ("game", "platform")