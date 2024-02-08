from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hospital.models import Patient
from django.db import transaction
from django.contrib.auth import login as auth_login



# Create your views here.
def login(request):
        
        if request.method == 'POST':
            username= request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')



def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if not all([first_name, last_name, username, email, password1, password2]):
            messages.error(request, 'Please fill all fields.')
            return redirect('register')
    
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register') 
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register') 
            else:
                try:
                    with transaction.atomic():
                        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                        user.save();
                        print('User created')
                        
                        patient = Patient.objects.create(
                        user=user,
                        name=f"{first_name} {last_name}",
                        email=email,
                        gender='', 
                        address='',
                        phone='',
                        illness='',
                        age=None, 
                    )
                        patient.save()

                        messages.success(request, 'Account created successfully')
                        auth_login(request, user)
                        return redirect('index')
                except Exception as e:
                    messages.error(request, 'Failed to create account. Error: {}'.format(e))
                    return redirect('register')
                                                
        else: 
            messages.info(request, 'Password not matching')
            return redirect('register') 

    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


