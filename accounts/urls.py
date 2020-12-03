from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', account_views.sign_up, name='sign_up'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', account_views.profile, name='profile')
]


