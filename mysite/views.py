from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        if User.objects.filter(username=email).exists():
            return HttpResponse("Email is already registered. Please log in.")
        my_user = User.objects.create_user(username=email, email=email, password=passw)
        my_user.first_name = uname
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=authenticate(request,username=email,password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid details")
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profilepage(request):
    return render(request,'profile.html')


@login_required(login_url='login')
def settings_view(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        privacy = request.POST.get('privacy') == 'on'  # checkbox

        # For demonstration purposes, store in session
        request.session['language'] = language
        request.session['privacy_mode'] = privacy

        messages.success(request, 'Settings updated successfully.')
        return redirect('setting')

    return render(request, 'settings.html', {
        'language': request.session.get('language', 'en'),
        'privacy_mode': request.session.get('privacy_mode', False),
    })
    return render(request, 'setting.html')

@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('signup')  # or homepage
    return redirect('settings')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change.html'
    success_url = reverse_lazy('login')



def contact(request):
    return render(request,'contact.html')   



def output(request):
    return render(request,'output.html')    




# Create your views here.
