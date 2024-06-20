from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_view'),
    path('register/', views.register, name='user_register'),
    path('profile/', views.profile_view, name='user_profile'),
]