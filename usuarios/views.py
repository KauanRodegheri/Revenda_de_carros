from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
# Create your views here.

class RegisterView(View):
     
    def get(self, request):
        user_form = UserCreationForm()
        return render(request, 'register.html', {'user_form': user_form})
    
    def post(self, request):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        return render(request, 'register.html', {'user_form': user_form})
    
class LoginView(View):

    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
    
    def post(self, request):
        usuario = request.POST['username']
        senha = request.POST['password']
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login(request, user)
                return redirect('cars_list')
       
        return render(request, 'login.html', {'login_form': login_form})
    
    
class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('cars_list')