from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(requests):
    if requests.method=='POST':
        form=UserRegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(requests,f'User profile has been created for {username}')
            return redirect('login')
            
    else:
        form=UserRegisterForm()

    return render(requests,'authentication/register.html',{'forms':form})