from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BalanceGameSerializer, NicknameSerializer
from .models import BalanceGame, Nicknames


class NicknamesView(viewsets.ModelViewSet):
    serializer_class = NicknameSerializer
    queryset = Nicknames.objects.all()
    

class BalanceGameView(viewsets.ModelViewSet):
    serializer_class = BalanceGameSerializer
    queryset = BalanceGame.objects.all()