from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'categoria'

router = routers.DefaultRouter()
router.register('', views.CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls)),
]