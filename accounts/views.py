from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('food_delivery:home')
        else:
            messages.info(request,'Invalid Login')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first name']
        last_name = request.POST['last name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
                return redirect('accounts:login')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('accounts:register')
    return render(request, 'registrations.html')


def logout(request):
    auth.logout(request)
    return redirect('food_delivery:home')
