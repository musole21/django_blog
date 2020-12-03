from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
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
    return render(request, 'accounts/profile.html', context={'status': None})