from django.db import models
from django.urls import reverse


# Create your models here.
from django.db.models import DecimalField

Category = (
    ('appetizers','Appetizers'),
    ('snacks','Snacks'),
    ('Lunch', 'lunch'),
    ('Desserts','desserts'),
    ('drinks','Drinks'),
)


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True)
    category = models.CharField(choices=Category, max_length=100, default=None)
    available = models.BooleanField(default=True)

    # class Meta:
    #     db_table = 'food'
    #

    def get_url(self):
        return reverse('food_delivery:menu', args=self.id)

    def __str__(self):
        return '{}'.format(self.name)


