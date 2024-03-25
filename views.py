from django.shortcuts import render

from gpm.http.decorators import load_response
from gpm.http import Response

from facebookapi.rules.stack import FACEBOOKAPI_RULESTACK

@load_response(
    stack=FACEBOOKAPI_RULESTACK,
    json=True,
    load_params=True,
)
def get_my_profile(request):
    """
    This function returns the profile of the current user
    """
    res = Response()
    return res.success()

@load_response(
    stack=FACEBOOKAPI_RULESTACK,
    json=True,
    load_params=True,
)
def connect(request):
    """
    This function connects the current user to facebook
    """
    res = Response()
    return res.success()
