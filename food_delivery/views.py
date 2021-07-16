from django.shortcuts import render
from django.views import generic, View
from . models import Food

# Create your views here.


def home(request):
    return render(request, 'home.html')


class FoodList(generic.ListView):
    queryset = Food.objects.filter(available=True).order_by('name')
    template_name = 'menu.html'
    paginate_by = '9'
