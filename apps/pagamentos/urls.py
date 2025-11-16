from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'pagamentos'

router = routers.DefaultRouter()
router.register('', views.PagamentoViewSet, basename='pagamentos')

urlpatterns = [
    path('', include(router.urls)),
]