from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
from .forms import *


# Create your views here.
def home(request):
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration_form.html', {'form': form})        
