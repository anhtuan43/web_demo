from django.urls import path
from . import views
app_name = "uploadModel"
urlpatterns = [
    path("", views.uploadFile),
    path("getFile/", views.getFile, name = "getFile")
]