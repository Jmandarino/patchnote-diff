from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    Game,
    Item,
    ItemVersion,
    Patch
)

from .serializer import (
    GameSerializer,
    ItemSerializer,
    ItemVersionSerializer,
    PatchSerializer
)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemVersionViewSet(viewsets.ModelViewSet):
    queryset = ItemVersion.objects.all()
    serializer_class = ItemVersionSerializer

class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer
