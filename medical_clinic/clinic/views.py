from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        # Login button has been pushed
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successfull login
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        # request.method = GET
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')
