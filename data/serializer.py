from rest_framework import serializers

from .models import (
    Game,
    Item,
    ItemVersion,
    Patch
)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVersion
        fields = '__all__'


class PatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patch
        fields = '__all__'