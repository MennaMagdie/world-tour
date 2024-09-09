from django.urls import path
from . import views


# Define a list of url patterns
# AKA list of all urls the user wants to navigate to
urlpatterns = [
    path('', views.index)
]
