from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user form to create the new user
            user = user_form.save()
            
            # Create a profile instance but do not save to the database yet
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Automatically log the user in
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)

            # Redirect to home page after successful registration and login
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def upload_resume(request):
    # Ensure Profile exists for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('upload_resume')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/upload_resume.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')
