from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('<int:menu_id>', views.menu, name='menu_id'),
]
