from django.urls import path
from . import views
from dashboard import views as dashboard_views
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/", dashboard_views.profile, name="profile"),
]