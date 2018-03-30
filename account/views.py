from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserLoginForm, UserRegisterForm




def home(request):
    print(4545)
    return render(request, 'Homepage.html')

def register_view(request):
    title= "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('account/Loggedin.html')
    return render(request, 'account/registration.html', {"form": form})


def logout_view(request):
    logout(request)
    return render(request, 'Homepage.html')


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'account/Loggedin.html')

    return render(request, 'account/Login.html')
