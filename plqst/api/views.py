from ..models import Game

from .serializers import GameSerializer

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from rest_framework import authentication, permissions, serializers

class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    parser_classes = (JSONParser,)
    def perform_create(self, serializer):

        game_data = self.request.data

        if self.request.user.is_authenticated:
            _ = serializer.save(game_data=game_data, game_owner=self.request.user)
        else:
            _ = serializer.save(game_data=game_data)
            self.request.session['temp_game_id'] = str(_)
            print(self.request.session)

        return Response(_)


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameUpdateAPIView(UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    parser_classes = (JSONParser,)

    def perform_update(self, serializer):
        # get the object itself
        instance = self.get_object()

        # modify fields during the update
        modified_instance = serializer.save()
        
