from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path("", views.home, name = "home"),
    path("register/", views.registerUser.as_view(), name = "registerUser"),
    path("login/", views.loginUser.as_view(), name = "loginUser"),
    path('logout/', views.logoutUser, name = "logout"), 
    path('private/', views.privatePage.as_view(), name = "privatePage"),
]