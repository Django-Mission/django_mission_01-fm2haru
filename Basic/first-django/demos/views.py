from cgitb import lookup
from unittest import result
from urllib import request
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def lotto(request):

    import random
    
    lotto_number = random.sample(range(1, 46), 7)
    lotto_number.sort()
    
    return render(request, 'lotto.html', {'lotto_number':lotto_number})
