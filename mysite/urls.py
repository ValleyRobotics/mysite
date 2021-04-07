from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns = [
    path("", views.myapp_index, name="myapp_index"),
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
]