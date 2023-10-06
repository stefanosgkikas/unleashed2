from django.urls import path
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import ProfileDetail, PublicProfileDetail, ProfileUpdate, DisableAccount, register, thank_you

urlpatterns = [
    #path('login/', views.CustomLoginView.as_view(), name='login'),
    #path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    #path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    #path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('disable_account/', DisableAccount.as_view(), name='disable'),
    path('register/', register, name='register'),
    path('thank_you/', thank_you, name='thank_you'),
    path('profile/', ProfileDetail.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdate.as_view(), name='profile_update'),
    path('users/<slug>/', PublicProfileDetail.as_view(), name='public_profile'),
]






