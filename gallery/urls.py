from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoryPage),
    path('<str:tag>/', views.albumPage),
    path('<int:pk>', views.imagePage),
]