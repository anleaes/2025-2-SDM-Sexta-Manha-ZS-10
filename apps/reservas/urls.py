from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'reservas'

router = routers.DefaultRouter()
router.register('', views.ReservaViewSet, basename='reservas')

urlpatterns = [
    path('', include(router.urls)),
]