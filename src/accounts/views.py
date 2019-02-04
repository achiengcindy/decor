from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model

from .forms import RegistrationForm
User= get_user_model()


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.set_password(user_form.cleaned_data['password'])
            user.is_active = False
            # Save the User
            # object
            user.save()
            return redirect('/')
            

    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/register.html',{'user_form': user_form})

