from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    GameViewSet,
    ItemViewSet,
    ItemVersionViewSet,
    PatchViewSet
)

router = routers.DefaultRouter()

router.register(r'games', GameViewSet)
router.register(r'items', ItemViewSet)
router.register(r'itemversions', ItemVersionViewSet)
router.register(r'patches', PatchViewSet)



urlpatterns = [
    url(r'^', include(router.urls))
]