from django.urls import path
from . import views

app_name = 'food_delivery'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.FoodList.as_view(), name='menu')
]