from django.contrib.postgres.fields import JSONField
from django.db import models
from patchnotes.models import BaseModel


class Game(BaseModel):
    title = models.CharField(max_length=64, help_text='the title for the game patchnote\'s')


class Item(BaseModel):
    name = models.CharField(max_length=250, help_text='name of the patch item we are keeping track of')
    game = models.ForeignKey('Game', on_delete=models.CASCADE,
                                help_text='FK reference to the game this item is a part of')


class ItemVersion(BaseModel):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    stats = JSONField(help_text='dictionary to keep track of item changes')


class Patch(BaseModel):
    date = models.DateTimeField(help_text='The date the patch was created')
    version_number = models.CharField(max_length=15, help_text='a string representation of a patch version')
    items = models.ManyToManyField('Item', blank=True, related_name='patch_items')
