from django.db import models
from django.utils import timezone
from django.conf import settings


class BalanceGame(models.Model):
    date = models.DateTimeField()
    nickname = models.CharField(primary_key=True, max_length=50)

    for i in range(1,21):
        globals()[f'q{i}'] = models.PositiveSmallIntegerField(null=False)
    