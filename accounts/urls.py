from django.urls import path, include
from .views import SignupPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup', ),
]
