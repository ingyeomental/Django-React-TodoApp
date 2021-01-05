from django.db import models
from django.utils import timezone


class Nicknames(models.Model):
    nickname_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, unique=True)


class BalanceGame(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    nickname_id = models.ForeignKey(Nicknames, on_delete=True)
    q1 = models.PositiveSmallIntegerField()
    q2 = models.PositiveSmallIntegerField()
    q3 = models.PositiveSmallIntegerField()
    q4 = models.PositiveSmallIntegerField()
    q5 = models.PositiveSmallIntegerField()
    q6 = models.PositiveSmallIntegerField()
    q7 = models.PositiveSmallIntegerField()
    q8 = models.PositiveSmallIntegerField()
    q9 = models.PositiveSmallIntegerField()
    q10 = models.PositiveSmallIntegerField()
    q11 = models.PositiveSmallIntegerField()
    q12 = models.PositiveSmallIntegerField()
    q13 = models.PositiveSmallIntegerField()
    q14 = models.PositiveSmallIntegerField()
    q15 = models.PositiveSmallIntegerField()
    q16 = models.PositiveSmallIntegerField()
    q17 = models.PositiveSmallIntegerField()
    q18 = models.PositiveSmallIntegerField()
    q19 = models.PositiveSmallIntegerField()
    q20 = models.PositiveSmallIntegerField()
