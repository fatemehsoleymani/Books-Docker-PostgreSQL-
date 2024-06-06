from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from allauth.account.views import PasswordChangeView


class MyPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('home')
    success_message = "Password Changed Successfully"



class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


