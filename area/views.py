from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


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

            return render(request, 'areas/hood.html', {"hood": hood, "businesses": businesses, "posts": posts})
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

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    hoods = Hood.objects.filter(user=request.user).all()
    business = Business.objects.filter(user=request.user).all()
    return render(request, 'profiles/profile.html', {"profile": profile, "hoods": hoods, "business": business})

@login_required
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
            messages.success(
                request, 'You Have succesfully created a hood.Now proceed and join a hood')
        return redirect('home')
    else:
        form = CreateHoodForm()
    return render(request, 'areas/create_hood.html', {"form": form})    

def join(request, hoodId):

    hood = Hood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.filter(user_id=request.user).update(hood_id=hood)
    else:

        Join(user_id=request.user, hood_id=hood).save()

    messages.success(
        request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('home')    

def search(request):

    if request.GET['search']:
        hood_search = request.GET.get("search")
        hoods = Hood.search_hood(hood_search)
        message = f"{hood_search}"

        return render(request, 'areas/search.html', {"message": message, "hoods": hoods})

    else:
        message = "You Haven't searched for any hood"
        return render(request, 'areas/search.html', {"message": message})    

def exitHood(request, hoodId):

    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.get(user_id=request.user).delete()
        messages.error(
            request, 'You have succesfully exited this Neighbourhood.')
        return redirect('home')        

def create_post(request):

    if Join.objects.filter(user_id=request.user).exists():
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.posted_by = request.user
                post.hood = request.user.join.hood_id
                post.save()
                messages.success(
                    request, 'You have succesfully created a Post')
                return redirect('home')
        else:
            form = PostForm()
        return render(request, 'createpost.html', {"form": form})        