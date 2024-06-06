from django.urls import path, include
from .views import SignupPageView
from django.contrib.auth import views as auth_views
from .views import MyPasswordChangeView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup', ),
    # path('password/change/', MyPasswordChangeView.as_view(), name='account_change_password'),
    path('', include('django.contrib.auth.urls')),
]
