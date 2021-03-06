from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from ..models import Game, GamePlay

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Game

class GameSaveSerializer(ModelSerializer):
    #
    id = HashidSerializerCharField(source_field='plqst.Game.id')

    class Meta:
        model = Game
        fields = [
            'id',
            'game_data',
        ]


class GameSerializer(ModelSerializer):
    id = HashidSerializerCharField(source_field='plqst.Game.id')
    class Meta:
        model = Game
        fields = [
            'id',
            'game_data',
        ]


class GamePlaySerializer(ModelSerializer):
    game_id = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='plqst.Game.id'), read_only=True)

    class Meta:
        model = GamePlay
        fields = [
            'game_id',
            'player',
            'gameplay_uid',
        ]
