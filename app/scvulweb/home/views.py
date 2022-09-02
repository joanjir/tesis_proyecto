from typing import re

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

def dashboard(request):
    return render(request, 'scvulweb/dashboard.html')
