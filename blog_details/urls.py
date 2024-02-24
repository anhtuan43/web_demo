from django.urls import path
from . import views
app_name = "blog_details"
urlpatterns = [
    path("", views.postDetail, name = "blog_details"),

]