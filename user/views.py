#from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import get_user, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Profile
from .decorators import class_login_required
from .utils import ProfileGetObjectMixin


# Login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Create this template in your app's templates directory
    #success_url = reverse_lazy('profile')  # Redirect to the home page after login

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html' 
    #success_url = reverse_lazy('home')
    next_page = reverse_lazy('home')  # Redirect to the home page after logout


class DisableAccount(View):
    success_url = settings.LOGIN_REDIRECT_URL # επιστροφή στην αρχική
    template_name = ('registration/user_confirm_delete.html')

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self, request):
        return TemplateResponse(request, self.template_name)

    @method_decorator(csrf_protect)
    @method_decorator(login_required) # cannot be an AnonymousUser
    def post(self, request):
        user = get_user(request) #grab the current User 
        user.set_unusable_password() # we disable the password,
        user.is_active = False # we disable the account
        user.save() # σὠζουμε
        logout(request) # τον πετάμε έξω
        return redirect(self.success_url) # επιστρέφουμε στο success_url δηλ. αρχική


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.save()    # σώζουμε τα στοιχεία του χρήστη για το login
            #login(request, user)  # κάνει αμέσων Login με τα στοιχεία του
            return redirect('thank_you')  # Redirect to thank you page or user's profile page
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

#class ThankYouView(View):
    template_name = 'registration/thank_you.html'

def thank_you(request):
    return render(request, 'registration/thank_you.html')

#def register(response):
   # return render(response, 'registration/register.html', {'form': form})
   # if response.method == 'POST':
   #     form = UserCreationForm(response.POST)
   #     if form.is_valid():
   #         form.save()
   #     else:
   #         form = UserCreationForm()
   # return render(response, 'registration/register.html', {'form': form})

@class_login_required
class ProfileDetail(ProfileGetObjectMixin, DetailView):
    model = Profile
    
@class_login_required
class ProfileUpdate(ProfileGetObjectMixin, UpdateView):
	fields = ('about', 'email', 'job', 'phone_number', 'picture',)
	model = Profile

class PublicProfileDetail(DetailView):
    model = Profile    