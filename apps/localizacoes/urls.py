from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'localizacoes'

router = routers.DefaultRouter()
router.register('', views.LocalizacaoViewSet, basename='localizacoes')

urlpatterns = [
    path('', include(router.urls)),
]