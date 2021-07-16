from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('add/<int:food_id>/', views.add_order, name='add_order'),
    path('', views.order_detail, name='order_detail'),
    path('remove/<int:food_id>/', views.remove_order, name='remove_order'),
    path('trash/<int:food_id>/', views.trash_item, name='trash_order')
]