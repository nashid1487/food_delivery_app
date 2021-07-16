from django.db import models
from food_delivery.models import Food


# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Order'
        ordering = ['date_added']

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.food.price * self.quantity

    def __str__(self):
        return self.food
