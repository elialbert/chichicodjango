from django.shortcuts import render_to_response, redirect
import logging

def home(request):
    return render_to_response('home.html')
