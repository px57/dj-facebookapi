"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'get_my_profile/', 
        views.get_my_profile, 
        name='facebookapi__get_my_profile'
    ),
    path(
        'connect/', 
        views.connect, 
        name='facebookapi__connect'
    ),
]