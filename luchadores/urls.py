from django.urls import path
from .views import (
    LuchadorListView,
    LuchadorCreateView,
    LuchadorUpdateView,
    LuchadorDeleteView,
)

urlpatterns = [
    path('', LuchadorListView.as_view(), name='luchador_list'),
    path('nuevo/', LuchadorCreateView.as_view(), name='luchador_create'),
    path('editar/<int:pk>/', LuchadorUpdateView.as_view(), name='luchador_update'),
    path('eliminar/<int:pk>/', LuchadorDeleteView.as_view(), name='luchador_delete'),
]