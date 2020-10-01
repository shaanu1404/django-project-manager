from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"
urlpatterns = [
    path('users/', views.all_users, name="all_users"),
    path('users/<int:id>/', views.user_details, name="user_details"),
    path('login/', views.AuthLogin.as_view(), name="login"),
    path('register/', views.register_user_view, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
]