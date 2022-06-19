from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
from .forms import *


# Create your views here.
def home(request):

    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Hood.objects.get(pk=request.user.join.hood_id.id)
            posts = Posts.objects.filter(hood=request.user.join.hood_id.id)
            businesses = Business.objects.filter(
                hood=request.user.join.hood_id.id)

            return render(request, 'hoods/hood.html', {"hood": hood, "businesses": businesses, "posts": posts})
        else:
            neighbourhoods = Hood.objects.all()
            return render(request, 'index.html', {"neighbourhoods": neighbourhoods})
    else:
        neighbourhoods = Hood.objects.all()
        return render(request, 'index.html', {"neighbourhoods": neighbourhoods})

        
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

def profile(request):
    return render(request, 'profiles/profile.html')       

def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
 
    return render(request, 'profiles/edit_profile.html', context)       
