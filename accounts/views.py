from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.

def user_register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            User.objects.create_user(
                username = data['user_name'] ,
                email = data['email'] ,
                first_name = data['first_name'],
                last_name = data['last_name'] ,
                password = data['password_2']
            )
            messages.success(request , 'ثبت نام شما با موفقیت انجام شد'  ,'success')
            return redirect('home:home')
    else :
        form = UserRegisterForm()
    return render(request , 'accounts/register.html',{'form':form})




def user_login(request) :
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            user = authenticate(request ,
                                username = data['user'] , password = data['password'])
            if user is not None :
                login(request , user)
                messages.success(request , 'خوش آمدید' , 'primary')
                return redirect('home:home')
            else:
                messages.error(request , 'نام کاربری یا رمز عبور اشتباه است' , 'danger')

    else :
        form = UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'به امید دیدار' , 'info')
    return redirect('home:home')