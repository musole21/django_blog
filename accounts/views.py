from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def sign_up(request):
    if request.method == 'GET':
        registration_form = UserRegistrationForm()
    elif request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user_name = registration_form.cleaned_data.get('username', None)
            messages.success(request, user_name)
            messages.warning(request, 'Your session data will be collected.')
            return redirect('blog:home')

    return render(request, 'accounts/sign_up.html', {'form': registration_form })

@login_required
def profile(request):
    if request.method == "GET":
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    elif request.method == "POST":
        user_form = UserUpdateForm( request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Successfully updated!')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/profile.html', context=context)