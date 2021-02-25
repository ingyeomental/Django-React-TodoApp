from rest_framework import serializers
from .models import BalanceGame, Nicknames


class NicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nicknames
        fields = (
            'nickname_id',
            'nickname',
        )


class BalanceGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceGame
        fields = (
            'nickname_id', 
            'datetime', 
            'q1', 
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
            'q9',
            'q10',
            'q11',
            'q12',
            'q13',
            'q14',
            'q15',
            'q16',
            'q17',
            'q18',
            'q19',
            'q20',
            )