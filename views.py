from django.shortcuts import render
from kernel.http import Response

def get_my_profile(request):
    """
    This function returns the profile of the current user
    """
    res = Response()
    return res.success()

def connect(request):
    """
    This function connects the current user to facebook
    """
    res = Response()
    return res.success()
