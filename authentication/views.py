from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def home(request,*args, **kwargs):
    return HttpResponse(f"Hello {request.user}!!")