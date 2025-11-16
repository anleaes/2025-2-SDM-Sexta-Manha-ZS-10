from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'clientes'

router = routers.DefaultRouter()
router.register('', views.ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls)),
]