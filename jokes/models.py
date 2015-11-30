from django.db import models
from django.contrib.auth import models as auth_models


class Joke(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField()
    date_entered = models.DateTimeField('date entered')
    entered_by = models.ForeignKey(auth_models.User)
