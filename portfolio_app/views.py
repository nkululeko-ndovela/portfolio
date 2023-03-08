from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm, CustomUserChangeForm
from .models import UserProfile

def map_view(request):
    profiles = UserProfile.objects.all()
    return render(request, 'portfolio_app/map.html', {'profiles': profiles})

@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'portfolio_app/profile.html', {'user_profile': user_profile})

@login_required
def edit_profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'portfolio_app/edit_profile.html', {'form': form})
