# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

admin.site.register(models.Series)
admin.site.register(models.Company)
admin.site.register(models.Genre)
admin.site.register(models.Game)
admin.site.register(models.Platform)
admin.site.register(models.GameRelease)
admin.site.register(models.GameReview)
