from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.contrib import messages

from checkout.models import Order, OrderItem
from .forms import RegistrationForm, ProfileEditForm, UserEditForm
from .tokens import account_activation_token
from .models import Profile

User= get_user_model()


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.set_password(user_form.cleaned_data['password'])
            #user becomes active only after activating tokens
            user.is_active = False
            # Save the User object
            user.save()
            #send one time activation email
            current_site = get_current_site(request)
            subject = 'Account Confirmation'
            sender = settings.DEFAULT_FROM_EMAIL
            message = render_to_string('accounts/account_activation_email.html', {
                'user':  user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes( user.pk)).decode(),
                'token':account_activation_token.make_token( user),
            })
            print( message)
            # https://stackoverflow.com/questions/40655802/how-to-implement-email-user-method-in-custom-user-model
            # email = EmailMessage(subject, message,sender, [user.email])
            # print(email)
            # email.send()
            user.email_user(subject=subject, message=message)
            return HttpResponse('Please confirm your email address to complete the registration.')
  
    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/register.html',{'user_form': user_form})

def activate(request, uidb64, token, backend='accounts.authentication.EmailAuthBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, 'accounts.authentication.EmailAuthBackend')
        return redirect('login')
    else:
        return render(request, 'accounts/account_activation_invalid.html')

@login_required
def accounts_settings(request):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/settings.html', {'orders':orders})

@login_required
def accounts_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('/')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accounts/edit.html', {'user_form': user_form,'profile_form': profile_form})
   


 




